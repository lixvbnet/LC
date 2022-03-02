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

