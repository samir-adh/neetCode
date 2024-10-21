# Definition for singly-linked li: class ListNode:
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        return None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        current = head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev

    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        head = list1
        current = head
        next = 2
        while list1 is not None or list2 is not None:
            if list1 is None:
                current.next = list2
            if list2 is None:
                current.next = list1
            if next == 2:
                current.next = list2
                next = 1
                list2 = list2.next
            if next == 1:
                current.next = list1
                next = 2
                list1 = list1.next
            current = current.next
        return head


def listToListNode(l: list) -> Optional[ListNode]:
    if len(l) == 0:
        return None
    head = ListNode(l[0], next=None)
    current = head
    for i in l[1:]:
        next = ListNode(i, None)
        current.next = next
        current = next
    return head


def listNodeToList(l: Optional[ListNode]) -> list:
    if l is None:
        return []
    res = []
    current = l
    while current is not None:
        res.append(current.val)
        current = current.next
    return res


def print_list_node(listNode: ListNode):
    string = "["
    current = listNode
    while current is not None:
        string += str(current.val) + ","
        current = current.next
    string += "]"
    print(string)


def test_reverse_list():
    test_cases = [
        ([], []),
        ([0], [0]),
        ([1, 2, 3, 4],
         [4, 3, 2, 1])
    ]
    for t in test_cases:
        input = t[0]
        expected = t[1]
        res = Solution().reverseList(listToListNode(input))
        res = listNodeToList(res)
        assert res == expected


def test_merge_list():
    test_cases = [
        ([1, 3, 5, 7],
         [2, 4, 6, 8],
         [1,2,3,4,5,6,7,8])
    ]
    for t in test_cases:
        list1,list2,expected = t
        list1,list2 = listToListNode(list1),listToListNode(list2)
        res = Solution().mergeList(list1,list2)
        res = listNodeToList(res)
        assert res == expected
