/* 
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]
*/

package timebasedkeyvaluestore

import (
	"testing"
)

func TestCase1(t *testing.T) {
	tmap := Constructor()
	tmap.Set("foo", "bar", 1)
	output := []string{}
	output = append(output, tmap.Get("foo", 1))
	output = append(output,tmap.Get("foo", 3))
	tmap.Set("foo", "bar2", 4)
	output = append(output,tmap.Get("foo", 4))
	output = append(output,tmap.Get("foo", 5))

	expected := []string{
		"bar",
		"bar",
		"bar2",
		"bar2",
	}

	for index,ouput_element := range(output) {
		expected_element := expected[index]
		if ouput_element != expected_element {
			t.Errorf("Expected : %s ; Got : %s\n",expected_element, ouput_element)
		}
	}

	
}