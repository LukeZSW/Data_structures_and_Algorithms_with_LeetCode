# Queues and Stacks

## Queue (FIFO)
In a FIFO data structure, the first element added to the queue will be processed first.

Problems|Solutions
---|---
[622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)|[Design_Circular_Queue.py](./Design_Circular_Queue.py)
### Queue and BFS
One common application of Breadth-first Search (BFS) is to find the shortest path from the root node to the target node. 
The processing order of the nodes is the exact same order as how they were added to the queue, which is First-in-First-out (FIFO). 
That's why we use a queue in BFS.<br>
[BFS_template](./BFS_Template.py)

Problems|Solutions
---|---
[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)|[Number_of_Islands.py](./Number_of_Islands.py)
[752. Open the Lock](https://leetcode.com/problems/open-the-lock/)|[Open_the_Lock.py](./Open_the_Lock.py)
[279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)|[Perfect_Squares.py](./Perfect_Squares.py)
[542. 01 Matrix](https://leetcode.com/problems/01-matrix/)|[01_Matrix.py](./01_Matrix.py)

## Stack (LIFO)
In a LIFO data structure, the newest element added to the queue will be processed first.

Problems|Solutions
---|---
[155. Min Stack](https://leetcode.com/problems/min-stack/submissions/)|[Min_Stack.py](./Min_Stack.py)
[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)|[Valid_Parentheses.py](./Valid_Parentheses.py)
[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)|[Daily_Temperatures.py](./Daily_Temperatures.py)
[150. Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/)|[Evaluate_Reverse_Polish_Notation.py](./Evaluate_Reverse_Polish_Notation.py)
[394. Decode String](https://leetcode.com/problems/decode-string/)|[Decode_String.py](./Decode_String.py)

### Stack and DFS
Similar to BFS, Depth-First Search (DFS) can also be used to find the path from the root node to the target node.
The processing order of the nodes is the exact opposite order as how they were added to the stack, which is Last-in-First-out (LIFO). 
That's why we use a stack in DFS.<br>
[DFS_template](./DFS_Template.py) (recursion and iteration)

Problems|Solutions
---|---
[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)|[Number_of_Islands.py](./Number_of_Islands.py#L40)
[733. Flood Fill](https://leetcode.com/problems/number-of-islands/)|[Flood_Fill.py](./Flood_Fill.py)
[841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)|[Keys and Rooms.py](./Keys_and_Rooms.py)

## Queue and Stack
Problems|Solutions
---|---
[232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)|[Implement_Queue_using_Stacks.py](./Implement_Queue_using_Stacks.py)
[225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)|[Implement_Stack_using_Queues.py](./Implement_Stack_using_Queues.py)