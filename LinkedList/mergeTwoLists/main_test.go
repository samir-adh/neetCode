package main

import (
	"fmt"
	"testing"
)

type testCase struct {
	list1    *ListNode
	list2    *ListNode
	expected *ListNode
}

func TestMergeTwoLists(t *testing.T) {
	var testCases = []testCase{
		{array2list([]int{1, 2, 3}),
			array2list([]int{1, 3, 4}),
			array2list([]int{1, 1, 2, 3, 3, 4})},
		{array2list([]int{}),
			array2list([]int{}),
			array2list([]int{})},
		{array2list([]int{}),
			array2list([]int{0}),
			array2list([]int{0})},
	}
	for index, testCase := range testCases {
		var result = mergeTwoLists(testCase.list1, testCase.list2)
		var expected = testCase.expected
		var errorMsg = fmt.Sprintf("Expected : %s, got : %s\n", listToString(expected), listToString(result))
		for result != nil && expected != nil {
			if result.Val != expected.Val {
				t.Error(errorMsg)
			}
			result = result.Next
			expected = expected.Next
		}
		if !(result == nil && expected == nil) {
			t.Error(errorMsg)
		}
		t.Logf("Test case %d passed.\n", index)
	}
}
