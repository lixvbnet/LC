## Stack & Queue

```go
func main() {
	stack_test()
	fmt.Println("========================")
	queue_test()
}

func stack_test() {
	var stack []int
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
	var queue []int

	// offer
	queue = append(queue, 3)
	queue = append(queue, 5)
	queue = append(queue, 6)
	queue = append(queue, 10)
	fmt.Println(queue)

	// poll
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



## Stack type definition

```go
func main() {
  var s Stack													// Create an Empty Stack
	//var s Stack = []int{0,1,2,3,4,5}	// Create a Stack with initial values
	s.Push(7)
	s.Push(8)
	s.Push(9)
	fmt.Println(s, "size:", len(stack))
	fmt.Println("-----------------------")

	s.Pop()
	s.Pop()
	fmt.Println(s, "size:", len(s))
	fmt.Println("-----------------------")
}


// Stack type definition
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

func (s *Stack) Top() int {
    return (*s)[len(*s)-1]
}


/* ----- optional methods ----- */
func (s *Stack) Size() int {
	return len(*s)
}

func (s *Stack) Empty() bool {
	return len(*s) == 0
}
```



## Queue type definition

```go
func main() {
	var q Queue														// Create an Empty Queue
	//var q Queue = []int{0,1,2,3,4,5}		// Create a Queue with initial values
	q.Offer(3)
	q.Offer(5)
	q.Offer(6)
	q.Offer(10)
	fmt.Println(q, "size:", len(q))
	fmt.Println("-----------------------")

	q.Poll()
	q.Poll()
	fmt.Println(q, "size:", len(q))
	fmt.Println("-----------------------")
}


// Queue type definition
type Queue []int

func (q *Queue) Offer(x int) {
	*q = append(*q, x)
}

func (q *Queue) Poll() int {
	x := (*q)[0]
	*q = (*q)[1:]
	return x
}

func (q *Queue) Peek() int {
	return (*q)[0]
}
```

