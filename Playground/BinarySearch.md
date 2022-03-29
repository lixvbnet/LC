# Binary Search

> [704. Binary Search](https://leetcode.com/problems/binary-search/) 



## 🍺 Search Template - Find first xxx

==This abstraction covers almost ALL binary search problems==. Search result is 5 in following example.

| `i`               | 0    | 1    | 2    | 3    | 4    | ==5== | 6     | 7     | 8     |
| ----------------- | ---- | ---- | ---- | ---- | ---- | ----- | ----- | ----- | ----- |
| `nums[i]`         | 2    | 2    | 3    | 5    | 8    | 10    | 10    | 12    | 15    |
| `f(i)`: num >= 10 | *F*  | *F*  | *F*  | *F*  | *F*  | ==T== | ==T== | ==T== | ==T== |

> - `func Search(n int, f func(int) bool) int` 
>
> `Search` uses binary search to find and return the smallest index i in [0, n) at which f(i) is true, assuming that on the range [0, n), f(i) == true implies f(i+1) == true. That is, `Search` requires that `f` is false for some (possibly empty) prefix of the input range [0, n) and then true for the (possibly empty) remainder; **Search returns the first true index**. If there is no such index, `Search` returns n.
>
> - `func SearchInts(a []int, target int) int` 
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
        
        // (optional) return result if condition is met
        //if some_condition {
        //    return xxx
        //}
        
		if f(m) {
			r = m
		} else {
			l = m + 1
		}
	}
	return l
}
```





---

# Applications

## Binary Search

```go
func search(nums []int, target int) int {
    l, r := 0, len(nums)
    for l < r {
        // Prevent (l + r) overflow
        m := l + (r - l) / 2
        if nums[m] == target {
            return m
        }
        
        if nums[m] > target {
            r = m
        } else {
            l = m + 1
        }
    }
    // End Condition: l > r
    return -1	// return l if want insert position
}
```



## FindFirstPosition / FindInsertPosition

The following function searches sorted array `nums` and returns first position (leftmost) of `target` (or insert position if not found).

- Use Standard Library

```go
// sort.SearchInts(nums, target)
func findFirstPosition(nums []int, target int) int {
	return sort.SearchInts(nums, target)
}
// OR
// sort.Search(n, f)
func findFirstPosition(nums []int, target int) int {
	return sort.Search(len(nums), func(i int) bool {
		return nums[i] >= target
	})
}
```

- Write on our own

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
