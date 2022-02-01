## Binary Search

```go
package main

import "fmt"

func main() {
	nums := []int{-1, 2, 5, 8, 10, 12, 15}
	for _, v := range nums {
		fmt.Printf("index of %2d: %2d\n", v, binarySearch(nums, v))
	}
	fmt.Printf("index of %2d: %2d\n", 9, binarySearch(nums, 9))
}

func binarySearch(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		// Prevent (l + r) overflow
		m := l + (r - l) / 2
		if nums[m] == target {
			return m
		} else if nums[m] < target {
			l = m + 1
		} else {
			r = m - 1
		}
	}
	// End Condition: l > r
	return -1
}
```

Output

```
index of -1:  0
index of  2:  1
index of  5:  2
index of  8:  3
index of 10:  4
index of 12:  5
index of 15:  6
index of  9: -1
```

> - Initial Condition:` left = 0, right = n-1`
> - Termination: `left > right`
> - Searching Left: `right = mid-1`
> - Searching Right: `left = mid+1`
