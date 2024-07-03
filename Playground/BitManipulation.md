## Bit Manipulation

```go
-i				// equivalent to ^i+1 (flip all bits of i and add 1)
i & -i		// get last 1-bit

i + (i & -1)		// add last 1-bit
i - (i & -1)		// remove last 1-bit, equivalent to i & (i-1)

i & (i-1)				// remove last 1-bit
```



