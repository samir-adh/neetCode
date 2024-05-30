class TimeMap:
    def __init__(self):
        self.pairs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.pairs:
            self.pairs[key] = []
        self.pairs[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        entries_list = self.pairs[key]
        entries_list_copy = entries_list.copy()
        num_entries = len(entries_list_copy)
        index = num_entries // 2
        while (num_entries == 1):
            current_timestamp = entries_list[index][1]
            if current_timestamp == timestamp:
                return 
            elif current_timestamp > timestamp:
                entries_list_copy = entries_list_copy[:index]
            else :
                entries_list_copy = entries_list_copy[index:]
            num_entries = len(entries_list_copy)
            index = num_entries // 2
        return entries_list[index][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
