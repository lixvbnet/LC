## `strings.Split` 

> ⚠️ Note: `strings.Split("")` results in array with 1 elem `[""]` 
>
> ```go
> A := strings.Split("", ",")
> fmt.Printf("%q\n", A)		// [""]
> ```



## Pointer as Function Parameter

```go
func main() {
	var result int
	change(&result)		// pass the pointer as parameter
	fmt.Println(result)
}

func change(result *int) {
	value := 3
    *result = value			// correct ("result" here is a pointer pointing to the variable defined in main function)
	// result = &value		// WRONG! because "value" is a local variable and only valid in this function
}
```



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

