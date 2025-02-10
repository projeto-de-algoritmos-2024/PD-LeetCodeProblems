## 474. Ones and Zeroes

![image](https://github.com/user-attachments/assets/7d162987-8952-48bd-b5e2-4142e8f8b7fe)

[Link para a questão](https://leetcode.com/problems/ones-and-zeroes/description/)

### Gravação

[Link para a gravação](https://www.youtube.com/watch?v=lz--Afk1h3Q)

#### Dificuldade: Média

### Enunciado

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 

Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100

### Submissões: 

![image](https://github.com/user-attachments/assets/4070c903-cc7a-4257-b478-3ccbf379a743)


![image](https://github.com/user-attachments/assets/79d0ccfe-0bbc-4f8e-90d2-7cdd2b032ec3)


