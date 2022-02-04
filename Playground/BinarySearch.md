# Binary Search

> [Binary Search Templates](https://leetcode.com/explore/learn/card/binary-search/) ***modified here.***

Note: The "🍺 Final Template - Search" covers almost ALL binary search problems.



## Template #1

> Template #1 is used to search for an element or condition which can be determined by *==accessing a single index==* in the array.

**Key Attributes:** 

> - Most basic and elementary form of Binary Search
>
> - Search Condition can be determined **without** comparing to the element's neighbors (or use specific elements around it)
> - No post-processing required because at each step, you are checking to see if the element has been found. If you reach the end, then you know the element is not found

**Distinguishing Syntax:** 

> - Initial Condition: ` left = 0, right = n-1` 
> - Loop Condition: `left <= right` 
> - Termination: `left > right`
> - Searching Left: `right = mid-1`
> - Searching Right: `left = mid+1` 
> - Post-processing: Not required

```go
package main

import "fmt"

func main() {
	nums := []int{2, 3, 5, 8, 10, 12, 15}
	for _, v := range nums {
		fmt.Printf("index of %2d: %2d\n", v, binarySearch(nums, v))
	}
	for _, v := range []int{-2, 9, 20} {
		fmt.Printf("index of %2d: %2d\n", v, binarySearch(nums, v))
	}
}

func binarySearch(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		// Prevent (l + r) overflow
		m := l + (r - l) / 2
		if nums[m] == target {
			return m
		} else if nums[m] > target {
            r = m - 1
		} else {
			l = m + 1
		}
	}
	// End Condition: l > r
	return -1
}
```

Output

```
index of  2:  0
index of  3:  1
index of  5:  2
index of  8:  3
index of 10:  4
index of 12:  5
index of 15:  6
index of -2: -1
index of  9: -1
index of 20: -1
```



## Template #2

> Template #2 is an advanced form of Binary Search. It is used to search for an element or condition which requires *==accessing the current index and its immediate right neighbor's index==* in the array. ( such as comparing `A[m]` with `A[m+1]` )

**Key Attributes:** 

> - An advanced way to implement Binary Search.
> - Search Condition needs to access the element's immediate right neighbor
> - Use the element's right neighbor to determine if the condition is met and decide whether to go left or right
> - ==Guarantees Search Space is at least 2 in size at each step==
> - Post-processing required. Loop/Recursion ends when you have 1 element left. Need to assess if the remaining element meets the condition.

**Distinguishing Syntax:** 

> - Initial Condition: `left = 0, right = n-1` 
> - Loop Condition: `left < right` 
> - Termination: `left == right`
> - Searching Left: `right = mid`
> - Searching Right: `left = mid+1` 
> - Post-processing: **Required** 

```go
func binarySearch(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l < r {
		// Prevent (l + r) overflow
		m := l + (r - l) / 2
		if nums[m] == target {
			return m
		} else if nums[m] > target {
            r = m
		} else {
			l = m + 1
		}
	}
	// Post-processing:
	// End Condition: l == r
	if nums[l] == target {
		return l
	}
	return -1
}
```



## Template #3

> Template #3 is another unique form of Binary Search. It is used to search for an element or condition which requires *==accessing the current index and its immediate left and right neighbor's index==* in the array.

**Key Attributes:** 

- An alternative way to implement Binary Search
- Search Condition needs to access element's immediate left and right neighbors
- Use element's neighbors to determine if condition is met and decide whether to go left or right
- ==Gurantees Search Space is at least 3 in size at each step==
- Post-processing required. Loop/Recursion ends when you have 2 elements left. Need to assess if the remaining elements meet the condition.

**Distinguishing Syntax:** 

- Initial Condition:` left = 0, right = n-1` 
- Loop Condition: `left + 1 < right` 
- Termination: `left + 1 == right`
- Searching Left: `right = mid`
- Searching Right: `left = mid` 
- Post-processing: **Required** 

```go
func binarySearch(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l + 1 < r {
		// Prevent (l + r) overflow
		m := l + (r - l) / 2
		if nums[m] == target {
			return m
		} else if nums[m] > target {
			r = m
		} else {
            l = m
		}
	}
	// Post-processing:
	// End Condition: l + 1 == r
	if nums[l] == target {
		return l
	}
	if nums[r] == target {
		return r
	}
	return -1
}
```



## FindFirstPosition / FindInsertPosition

The following function searches sorted array `nums` and returns first position (leftmost) of `target` (or insert position if not found).

```go
func findFirstPosition(nums []int, target int) int {
	l, r := 0, len(nums)
	for l < r {
		m := l + (r - l) / 2
		if nums[m] >= target {
			r = m
		} else {
			l = m + 1
		}
	}
	return l
}
```

It can also be written as:

```go
func findFirstPosition(nums []int, target int) int {
	l, r := 0, len(nums)-1
	for l <= r {
		m := l + (r - l) / 2
		if nums[m] >= target {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l
}
```

And we can also use Go standard library:

```go
// sort.SearchInts(nums, target)
func findFirstPosition(nums []int, target int) int {
	return sort.SearchInts(nums, target)
}
// OR
// sort.Search(nums, f)
func findFirstPosition(nums []int, target int) int {
	return sort.Search(len(nums), func(i int) bool {
		return nums[i] >= target
	})
}
```



## 🍺 Final Template - Search

==This abstraction covers almost ALL binary search problems==.

> - `func Search(n int, f func(int) bool) int` 
>
> `Search` uses binary search to find and return the smallest index i in [0, n) at which f(i) is true, assuming that on the range [0, n), f(i) == true implies f(i+1) == true. That is, `Search` requires that `f` is false for some (possibly empty) prefix of the input range [0, n) and then true for the (possibly empty) remainder; **Search returns the first true index**. If there is no such index, `Search` returns n.
>
> - `func SearchInts(a []int, x int) int` 
>
> ```go
> func SearchInts(nums []int, target int) int {
> 	return Search(len(nums), func(i int) bool { return nums[i] >= target })
> }
> ```
>
> `SearchInts` searches for `target` in a sorted slice of ints and returns the index as specified by Search. The return value is the index to insert `target` if it is not present (it could be len(nums)). The slice must be sorted in ascending order.

Apart from using `sort.Search` from the standard library, we can also write our own search function:

```go
func search(n int, f func(int) bool) int {
	l, r := 0, n
	for l < r {
		m := l + (r - l) / 2
		if f(m) {
			r = m
		} else {
			l = m + 1
		}
	}
	return l
}
```

It can also be written as:

```go
func search(n int, f func(int) bool) int {
	l, r := 0, n-1
	for l <= r {
		m := l + (r - l) / 2
		if f(m) {
			r = m - 1
		} else {
			l = m + 1
		}
	}
	return l
}
```





