package timebasedkeyvaluestore

//We define TimeMapEntry structure to access data more easily
type TimeMapEntry struct {
	Timestamp int
	Value     string
}

type TimeMap struct {
	entries map[string][]TimeMapEntry // We use a hashamap to access the list of values for each key in o(1)
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
	left := 0
	right := len(entryList) - 1
	var value string // We use this variable to hold that last acceptable value

	/* 
	We use binary search to find the correct timestamp : the entry list
	is already sorted because timestamp are entered in ascending order 
	*/
	for right-left >= 0 {
		mid := (right + left) / 2 // `mid` is the middle index of the search space
		if timestamp == entryList[mid].Timestamp { // If we find the exact timestamp we can immediatly return the value
			return entryList[mid].Value
		} else if timestamp > entryList[mid].Timestamp { 
			/*
			If the target timestamp is greater than the current timestamp,
			the value is acceptable and we can put it in the `value` variable
			*/
			value = entryList[mid].Value
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return value
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Set(key,value,timestamp);
 * param_2 := obj.Get(key,timestamp);
 */
