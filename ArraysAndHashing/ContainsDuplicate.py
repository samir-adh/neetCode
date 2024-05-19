class Tree:
    def __init__(self, one_value: int) -> None:
        self.value = one_value
        self.left_child = 0
        self.right_child = 0

    def insert(self, one_value: int) ->None:
        node = self
        parent = None
        while node != 0:
            if one_value > node.value:
                if node.right_child == 0:
                    node.right_child = Tree(one_value)
                    return
                else:
                    node = node.right_child
            else:
                if node.left_child == 0:
                    node.left_child = Tree(one_value)
                    return
                else:
                    node = node.left_child

    def __contains__(self, item: int):
        node = self
        while node != 0:
            if item == node.value:
                return True
            elif item >= node.value:
                node = node.right_child
            else:
                node = node.left_child
        return False


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        table = Tree(nums[0])
        for i in nums[1:]:
            if i in table:
                return True
            else:
                table.insert(i)
        return False

if __name__ == "__main__":
    nums2 = [1, 2, 4, 8,4]
    print(Solution().containsDuplicate(nums=nums2))
