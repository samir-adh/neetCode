class TimeMap:
    def __init__(self):
        self.keymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keymap:
            self.keymap.update({key: [(timestamp, value)]})
        else:
            values = self.keymap.get(key)
            insert(values, timestamp, value)

    def get(self, key: str, timestamp: int) -> str:
        values = self.keymap.get(key)
        left = 0
        right = len(values) - 1
        while left < right:
            index = left + right // 2
            if values[index] > timestamp:
                right = index - 1
            elif values[index] < timestamp:
                left = index + 1
            else:
                return values[]


def insert(values: list, timestamp: int, value: str):
    left = 0
    right = len(values) - 1
    while left < right:
        index = left + right // 2
        if values[index] > timestamp:
            right = index - 1
        else:
            left = index + 1
    values.insert(left, (timestamp, value))
