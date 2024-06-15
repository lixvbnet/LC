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

