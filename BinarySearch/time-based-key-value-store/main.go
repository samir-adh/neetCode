package timebasedkeyvaluestore

type TimeMapEntry struct {
	Timestamp int
	Value     string
}

type TimeMap struct {
	entries map[string][]TimeMapEntry
}

func Constructor() TimeMap {
	instance := TimeMap{
		make(map[string][]TimeMapEntry),
	}
	return instance
}

func (this *TimeMap) Set(key string, value string, timestamp int) {
	newEntry := TimeMapEntry{
		Timestamp: timestamp,
		Value:     value,
	}
	entryList, ok := this.entries[key]
	if !ok {
		entryList = []TimeMapEntry{}
	}
	this.entries[key] = append(entryList, newEntry)
}

func (this *TimeMap) Get(key string, timestamp int) string {
	entryList, keyExists := this.entries[key]
	if !keyExists { // If the key doesn't exists we return an empty string
	return ""
}
	searchSpace := make([]TimeMapEntry, len(entryList)) 
	copy(searchSpace, entryList) // We copy the entry list as we don't want to cause any change in the original
	// if len(searchspace) == 1 {           // case where there is only one element in the entry list
	// 	entry := searchspace[0]
	// 	if entry.timestamp < timestamp { // if `entry.timestamp` is greater than `timestamp` we return an empty string
	// 		return ""
	// 	} else { // otherwise we can return the value
	// 		return searchspace[0].value
	// 	}
	// }

	/* We use binary search to find the correct timestamp : the entry list
	is already sorted because timestamp are entered in ascending order */
	mid := len(searchSpace) / 2 // `mid` is the middle index of the entry list
	for len(searchSpace) > 1 {
		if searchSpace[mid].Timestamp == timestamp {
			return searchSpace[mid].Value
		} else if searchSpace[mid].Timestamp > timestamp {
			searchSpace = searchSpace[:mid]
		} else {
			/* Notice that we keep the element at index `mid` in `searchSpace`.
			If the exact timestamp is not present in the entry list this allow
			us to return the element with the largest timestamp inferior to `timestamp` */
			searchSpace = searchSpace[mid:]
		}
	}

	// Now we check
	if searchSpace[0].Timestamp <= timestamp {
		return searchSpace[0].Value
	} else {
		return ""
	}

}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
