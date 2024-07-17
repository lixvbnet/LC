## kOnes

Given a string `s` and an integer `k` , where `s` only contains '0's and '1's. Find all substrings that starts with '1' and contains k '1's. Then return the substring whose represented integer is smallest.

**Example**:

Input: s = "1001101", k = 2

Output: "11"



## Solution

- Sliding Window	 $O(n)$ 

```go
package main

import (
	"fmt"
	"math"
	"strconv"
)

func main() {
	s := "0001011000101011"
	k := 3
	res := kOnes(s, k)
	fmt.Println(res)
	fmt.Println(smallestStr(&res))
}

func smallestStr(res *[]string) string {
	var minVal int64 = math.MaxInt
	var minStr string
	for _, str := range *res {
		val, _ := strconv.ParseInt(str, 2, 64)
		if val < minVal {
			minVal = val
			minStr = str
		}
	}
	return minStr
}

func kOnes(s string, k int) []string {
	var res []string
	cnt := 0
	j := 0
	for cnt < k {
		if s[j] == '1' {
			cnt++
		}
		j++
	}

	// window A[i..j) always has k 1's
	i := 0;
	for j < len(s) {
		var l int
		// find next 1
		for l = i; s[l] == '0'; l++ {}
		res = append(res, s[l:j])

		if s[j] == '1' {
			i = l+1		// remove a 1 from left before extending the window
		}
		j++
	}
	return res	
}
```

Output:

```
[1011 10110 101100 1011000 110001 1100010 1000101 10001010 10101]
1011
```



## Follow-up

If we change the problem to "Find all substrings that contains k '1's." , no necessarily starting with '1'.

- Sliding Window	$O(n^2)$ 

```go
package main

import (
	"fmt"
	"math"
	"strconv"
	"strings"
)

func main() {
	s := "0001011000101011"
	k := 3
	res := kOnes(s, k)
	fmt.Println(res)
	fmt.Println(smallestStr(&res))
}

func smallestStr(res *[]string) string {
	var minVal int64 = math.MaxInt
	var minStr string
	for _, str := range *res {
		if strings.HasPrefix(str, "0") {
			continue
		}
		val, _ := strconv.ParseInt(str, 2, 64)
		if val < minVal {
			minVal = val
			minStr = str
		}
	}
	return minStr
}

func kOnes(s string, k int) []string {
	var res []string
	cnt := 0
	j := 0
	for cnt < k {
		if s[j] == '1' {
			cnt++
		}
		j++
	}

	// window A[i..j) always has k 1's
	i := 0;
	for j < len(s) {
		// add to res
		l := i
		for l < j {
			res = append(res, s[l:j])
			if s[l] == '1' {
				break
			}
			l++
		}

		if s[j] == '1' {
			i = l+1		// remove a 1 from left before extending the window
		}
		j++
	}
	return res	
}
```

Output:

```
[0001011 001011 01011 1011 00010110 0010110 010110 10110 000101100 00101100 0101100 101100 0001011000 001011000 01011000 1011000 0110001 110001 01100010 1100010 1000101 10001010 00010101 0010101 010101 10101]
1011
```



