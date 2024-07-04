# Binary Tree Traversal

Two traversal methods: **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** . And DFS includes `Preorder`, `Inorder`, and `Postorder` Traversal.



## [94. Inorder](https://leetcode.com/problems/binary-tree-inorder-traversal/) 

Recusive approach is trivial:

```go
func inorderTraversal(root *TreeNode) []int {
    var result []int
    inorder(root, &result)
    return result
}

func inorder(root *TreeNode, result *[]int) {
    if root == nil {
        return
    }
    inorder(root.Left, result)
    *result = append(*result, root.Val)
    inorder(root.Right, result)
}
```

Iterative:

```go
func inorderTraversal(root *TreeNode) []int {
    var result []int
    var stack []*TreeNode
    p := root
    for p != nil || len(stack) > 0 {
        if p != nil {
            // push
            stack = append(stack, p)
            p = p.Left
        } else {
            // pop and visit
            node := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            p = node.Right
            result = append(result, node.Val)	// Add after all left children
        }
    }
    return result
}
```



## [144. Preorder](https://leetcode.com/problems/binary-tree-preorder-traversal/) 

> Let `p` start from `root`, if `p` is not nil, push to stack and move to `p.Left` ; otherwise pop a `node` from stack and move to `node.Right`.
>
> The only difference between `Preorder` and `Inorder` Traversal is when do we add node value to result.

```go
func preorderTraversal(root *TreeNode) []int {
    var result []int
    var stack []*TreeNode
    p := root
    for p != nil || len(stack) > 0 {
        if p != nil {
            // visit and push
            result = append(result, p.Val)	// Add before going to children
            stack = append(stack, p)
            p = p.Left
        } else {
            // pop
            node := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            p = node.Right
        }
    }
    return result
}
```



## [145. Postorder](https://leetcode.com/problems/binary-tree-postorder-traversal/) 

> Postorder Traversal is ***more tricky*** to implement.
>
> Here we add another variable `last` , pointing to last node we pop out from stack / or last node we add to result.

```go
func postorderTraversal(root *TreeNode) []int {
    var result []int
    var stack []*TreeNode
    p := root
    var last *TreeNode
    for p != nil || len(stack) > 0 {
        if p != nil {
            // push
            stack = append(stack, p)
            p = p.Left
        } else {
            // peek
            node := stack[len(stack)-1]
            // if right is not nil AND not visited, then move to right
            if node.Right != nil && node.Right != last {
                p = node.Right
            } else {
                // pop
                stack = stack[:len(stack)-1]
                last = node
                result = append(result, node.Val)
            }
        }
    }
    return result
}
```

> Another way to write this (more intuitive but need handle some corner case).
>
> ```go
> func postorderTraversal(root *TreeNode) []int {
>     var result []int
>     var stack []*TreeNode
>     p := root 
>     for p != nil || len(stack) > 0 {
>         if p != nil {
>             // push
>             stack = append(stack, p)
>             p = p.Left
>         } else {
>             // left is done, in case right is also done
>             if stack[len(stack)-1].Right == nil {
>                 var last *TreeNode  // avoid going down again
>                 for len(stack) > 0 && stack[len(stack)-1].Right == last {
>                     // pop
>                     last = stack[len(stack)-1]
>                     stack = stack[:len(stack)-1]
>                     result = append(result, last.Val)
>                 }
>                 if len(stack) == 0 {
>                     break
>                 }
>             }
>             // move to right
>             p = stack[len(stack)-1].Right
>         }
>     }
>     return result
> }
> ```



## [102. BFS (Level Order Traversal)](https://leetcode.com/problems/binary-tree-level-order-traversal/) 

```go
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func levelOrder(root *TreeNode) [][]int {
    var result [][]int
    if root == nil {
        return result
    }
    var q Queue
    q.Offer(root)
    for len(q) > 0 {
        levelSize := len(q)
        level := make([]int, levelSize)
        result = append(result, level)
        for i := 0; i < levelSize; i++ {
            node := q.Poll()
            level[i] = node.Val
            if node.Left != nil {
                q.Offer(node.Left)
            }
            if node.Right != nil {
                q.Offer(node.Right)
            }
        }
    }
    return result
}

type Queue []*TreeNode

func (q *Queue) Offer(x *TreeNode) {
    *q = append(*q, x)
}

func (q *Queue) Poll() *TreeNode {
    v := (*q)[0]
    *q = (*q)[1:]
    return v
}
```

