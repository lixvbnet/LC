## References

- https://vbnetvbnet.github.io/LeetCode/#/./%E4%B8%93%E9%A2%98%E6%80%BB%E7%BB%93/Basics



## 2-D Slice

Create an `m * n` slice.

```go
arr := make([][]int, m)
for i := range arr {
  arr[i] = make([]int, n)
}
```



## Graph: edges to adjacency list

> Each `edges[i] = [ui, vi]` denotes a bi-directional edge between vertex `ui` and vertex `vi`.

```go
adj := make([][]int, n)
for _, edge := range edges {
  x, y := edge[0], edge[1]
  adj[x] = append(adj[x], y)
  adj[y] = append(adj[y], x)  // Don't forget!
}
```



## strings.Split 

> ⚠️ Note: `strings.Split("")` results in array with 1 element `[""]` 
>
> ```go
> A := strings.Split("", ",")
> fmt.Printf("%q\n", A)		// [""]
> ```



## Extend a slice

Add a `0` at both sides of the slice `heights` 

```go
heights = append(append([]int{0}, heights...), 0)
```

> This is equivalent to following code:
>
> ```go
> newHeights := make([]int, len(heights)+2)
> for i := range heights {
>     newHeights[i+1] = heights[i]
> }
> heights = newHeights
> ```



## Slice Insert

> https://stackoverflow.com/questions/46128016/insert-a-value-in-a-slice-at-a-given-index 

Since Go 1.21 release, you can use `slices.Insert` 

```go
result = slices.Insert(slice, index, value)
```

To write our own version:

```go
func main() {
	nums := []int{1, 2, 3}
	nums = insert(nums, 1, 9)
	fmt.Println(nums)
}

// 0 <= i <= len(a)
func insert(a []int, i int, v int) []int {
	if i == len(a) { // nil or empty slice or after last element
		return append(a, v)
	}
	// copy all required elements to one index higher to make room for the new element
	a = append(a[:i+1], a[i:]...) // i < len(a)
	// set the element at the index, using a single assignment
	a[i] = v
	return a
}
```

> Note: you may be tempted to use `A = append(append(A[:i], v), A[i:]...)` , but it is WRONG!! Because `append([:i], v)` would overwrite `A[i]` and so `A[i:]` woud be a "dirty" slice!!



## Check Int32 Overflow

```go
// complicated way to write this:
if result > math.MaxInt32 / 10 || (result == math.MaxInt32 / 10 && digit > math.MaxInt32 % 10)

// it can be simplified to
if result > (math.MaxInt32 - digit) / 10
// want to check if result * 10 + digit > math.MaxInt32,
// but since *10 and +digit both could overflow, so move them to right side

// to check underflow, just change it to
if result < (math.MinInt32 - digit) / 10	// here digit is negative (num % 10)
```

For example, solution for [LC 7. Reverse Integer](https://leetcode.com/problems/reverse-integer/) :

```go
func reverse(x int) int {
    result := 0
    for x != 0 {
        digit := x % 10
        x /= 10
        if result > (math.MaxInt32 - digit) / 10 {
            return 0
        }
        if result < (math.MinInt32 - digit) / 10 {
            return 0
        }
        result = result * 10 + digit
    }
    return result
}
```

