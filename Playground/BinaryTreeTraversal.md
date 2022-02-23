# Binary Tree Traversal

Two traversal methods: **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** . And Depth-First Search includes `Preorder` Traversal, `Inorder` Traversal, and `Postorder` Traversal.



## [Preorder](https://leetcode.com/problems/binary-tree-preorder-traversal/) 

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
            result = append(result, p.Val)	// Add before going to children
            // push
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



## [Inorder](https://leetcode.com/problems/binary-tree-inorder-traversal/) 

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
            // pop
            node := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            p = node.Right
            result = append(result, node.Val)	// Add after all left children
        }
    }
    return result
}
```



## [Postorder](https://leetcode.com/problems/binary-tree-postorder-traversal/) 

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



## [BFS (Level Order Traversal)](https://leetcode.com/problems/binary-tree-level-order-traversal/) 

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

    queue := []*TreeNode{root}
    for len(queue) > 0 {
        levelSize := len(queue)
        lst := make([]int, 0, levelSize)
        for i := 0; i < levelSize; i++ {
            // poll
            node := queue[0]
            queue = queue[1:]
            lst = append(lst, node.Val)
            // offer
            if node.Left != nil {
                queue = append(queue, node.Left)
            }
            if node.Right != nil {
                queue = append(queue, node.Right)
            }
        }
        result = append(result, lst)
    }
    return result
}
```

