## Stack & Queue

```go
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



## Stack helper functions

```go
func main() {
	stack := []int{0,1,2,3,4,5}
	stackPush(&stack, 7)
	stackPush(&stack, 8)
	stackPush(&stack, 9)
	fmt.Println(stack)
	fmt.Println("-----------------------")
	
	stackPop(&stack)
	stackPop(&stack)
	fmt.Println(stack)
}

// stack helper functions
func stackPush(stack *[]int, x int) {
	*stack = append(*stack, x)
}

func stackPop(stack *[]int) int {
	n := len(*stack)
	top := (*stack)[n-1]
	*stack = (*stack)[:n-1]
	return top
}
```

Output

```
[0 1 2 3 4 5 7 8 9]
-----------------------
[0 1 2 3 4 5 7]
```



## Stack type definition

```go
func main() {
	var stack Stack = []int{0,1,2,3,4,5}
	stack.Push(7)
	stack.Push(8)
	stack.Push(9)
	fmt.Println(stack, "size:", len(stack))
	fmt.Println("-----------------------")

	stack.Pop()
	stack.Pop()
	fmt.Println(stack, "size:", len(stack))
	fmt.Println("-----------------------")
}

// stack type definition
type Stack []int

func (s *Stack) Push(x int) {
	*s = append(*s, x)
}

func (s *Stack) Pop() int {
	n := len(*s)
	top := (*s)[n-1]
	*s = (*s)[:n-1]
	return top
}

func (s *Stack) Peek() int {
	n := len(*s)
	return (*s)[n-1]
}

/* ----- optional methods ----- */
func (s *Stack) Size() int {
	return len(*s)
}

func (s *Stack) Empty() bool {
	return len(*s) == 0
}
```

