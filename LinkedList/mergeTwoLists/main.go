package main

import (
	"fmt"
	"strings"
)

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	var l = array2list([]int{1, 2, 3, 5, 5})
	println(listToString(l))
}

func array2list(array []int) *ListNode {
	var head = &ListNode{
		0,
		nil,
	}
	var current = head
	for _, val := range array {
		current.Next = &ListNode{
			val,
			nil,
		}
		current = current.Next
	}
	return head.Next
}

func listToString(list *ListNode) string {
	var strBuilder strings.Builder
	strBuilder.WriteString("[")
	for list != nil {
		strBuilder.WriteString(fmt.Sprintf("%d,", list.Val))
		list = list.Next
	}
	strBuilder.WriteString("]")
	return strBuilder.String()
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var head = &ListNode{
		0,
		nil,
	}
	var current = head
	for !(list1 == nil && list2 == nil) {
		if list1 == nil {
			current.Next = list2
			return head.Next
		}
		if list2 == nil {
			current.Next = list1
			return head.Next
		}
		if list1.Val < list2.Val {
			current.Next = list1
			list1 = list1.Next
			} else {
				current.Next = list2
				list2 = list2.Next
		}
		current = current.Next
	}
	return head.Next
}

