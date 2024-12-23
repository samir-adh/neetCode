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
	output = append(output, tmap.Get("foo", 3))
	tmap.Set("foo", "bar2", 4)
	output = append(output, tmap.Get("foo", 4))
	output = append(output, tmap.Get("foo", 5))

	expected := []string{
		"bar",
		"bar",
		"bar2",
		"bar2",
	}

	for index, ouput_element := range output {
		expected_element := expected[index]
		if ouput_element != expected_element {
			t.Errorf("Test case number %d failed : \n	Expected : %s ; Got : %s\n", index, expected_element, ouput_element)

		}
	}

}

/*
Last Executed Input
Use Testcase
["TimeMap","set","set","set","set","get"]
[[],["foo","bar",1],["foo", "toilet", 5],["foo", "bucket", 10],["foo","bar2",20],["foo",15]]
*/

func TestCase2(t *testing.T) {
	tmap := Constructor()
	tmap.Set("foo", "bar", 1)
	tmap.Set("foo", "toilet", 5)
	tmap.Set("foo", "bucket", 10)
	tmap.Set("foo", "bar2", 20)
	output := tmap.Get("foo", 15)

	expected := "bucket"

	if output != expected {
		t.Errorf("Expected : %s ; Got : %s\n", expected, output)

	}
}

/*
	["TimeMap","set","set","get","get","get","get","get"]

[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
Use Testcase
Expected
[null,null,null,"","high","high","low","low"]
*/
func TestCase3(t *testing.T) {
	tmap := Constructor()
	tmap.Set("love", "high", 10)
	tmap.Set("love", "low", 20)
	output := []string{}
	output = append(output, tmap.Get("love", 5))
	output = append(output, tmap.Get("love", 10))
	output = append(output, tmap.Get("love", 15))
	output = append(output, tmap.Get("love", 20))
	output = append(output, tmap.Get("love", 25))

	expected := []string{
		"",
		"high",
		"high",
		"low",
		"low",
	}

	for index, ouput_element := range output {
		expected_element := expected[index]
		if ouput_element != expected_element {
			t.Errorf("Test case number %d failed : \n	Expected : \"%s\" ; Got : \"%s\"\n", index+1, expected_element, ouput_element)
		}
	}
}
