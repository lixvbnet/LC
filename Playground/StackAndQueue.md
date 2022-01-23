## Stack & Queue

```go
package main

import "fmt"

func main() {
	stack_test()
	fmt.Println("========================")
	queue_test()
}

func stack_test() {
	stack := []int{}
	// push
	stack = append(stack, 3)
	stack = append(stack, 5)
	stack = append(stack, 6)
	stack = append(stack, 10)
	fmt.Println(stack)

	// pop
	for len(stack) > 0 {
		x := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		fmt.Println(stack, x)
	}
	fmt.Println("stack is empty")
}

func queue_test() {
	queue := []int{}

	// enqueue
	queue = append(queue, 3)
	queue = append(queue, 5)
	queue = append(queue, 6)
	queue = append(queue, 10)
	fmt.Println(queue)

	// dequeue
	for len(queue) > 0 {
		x := queue[0]
		queue = queue[1:]
		fmt.Println(queue, x)
	}
	fmt.Println("queue is empty")
}
```

Output

```
[3 5 6 10]
[3 5 6] 10
[3 5] 6
[3] 5
[] 3
stack is empty
========================
[3 5 6 10]
[5 6 10] 3
[6 10] 5
[10] 6
[] 10
queue is empty
```

