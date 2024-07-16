## [919 · Meeting Rooms II](https://www.lintcode.com/problem/919/) 

**Description** 

Given an array of meeting time intervals consisting of start and end times `[[s1,e1],[s2,e2],...] (si < ei)`, find the minimum number of conference rooms required.

Note: (0,8),(8,10) is not conflict at 8

**Example** 

**Example1**

```
Input: intervals = [(0,30),(5,10),(15,20)]
Output: 2
Explanation:
We need two meeting rooms
room1: (0,30)
room2: (5,10),(15,20)
```

**Example2**

```
Input: intervals = [(2,7)]
Output: 1
Explanation: 
Only need one meeting room
```



## Idea

Sorting + Timeline. Count concurrent meetings at a given time.

- Start a meeting: count++
- End a meeting: count--  (**End a meeting first when there's a tie**: when a meeting starts and another meeting ends at the same time)

(Visualization from [Yt video](https://www.youtube.com/watch?v=FdzJmTCVyJU))

![meeting-rooms-ii](_image/meeting-rooms-ii.jpg) 



## Solution

- Sorting

```go
/**
 * Definition of Interval:
 * type Interval struct {
 *     Start, End int
 * }
 */

import "sort"

func MinMeetingRooms(intervals []*Interval) int {
    n := len(intervals)
    start := make([]int, n)
    end := make([]int, n)
    for i := range intervals {
        start[i] = intervals[i].Start
        end[i] = intervals[i].End
    }
    sort.Ints(start)
    sort.Ints(end)

    maxCount, count := 0, 0
    i, j := 0, 0
    for i < n {
        if start[i] < end[j] {
            count++
            i++
        } else {
            count--
            j++
        }
        maxCount = max(maxCount, count)
    }
    return maxCount
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
```

