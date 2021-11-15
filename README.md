# LeetCode

In this repository I'm going to solve some problems published on the [site](https://leetcode.com/problemset/all/). Problems are classified as: easy, medium, hard.

## 1. Two Sum (Easy)
Given an array of integers ```nums``` and an integer ```target```, return indices of the two numbers such that they add up to ```target```.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

**Input:** nums = [2,7,11,15], target = 9

**Output:** [0,1] (*Explanation: nums[0] + nums[1] == 9, we return [0, 1]*)

## 2. Add Two Numbers (Medium)

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order**, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Input:** l1 = [2,4,3], l2 = [5,6,4]

**Output:** [7,0,8] (*Explanation: 342 + 465 = 807*)

## 3. Longest Substring Without Repeating Characters (Medium)

Given a string ```s```, find the length of the **longest substring** without repeating characters.

Input: s = "abcabcbb"

Output: 3 (*Explanation: The answer is "abc", with the length of 3*)

## 4. Median of Two Sorted Arrays (Hard)

Given two sorted arrays ```nums1``` and ```nums2``` of size ```m``` and ```n``` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be ```O(log (m+n))```.

**Input:** nums1 = [1,3], nums2 = [2]

**Output:** 2.00000 (*Explanation: merged array = [1,2,3] and median is 2*)

## 5. (23.) Merge k Sorted Lists

You are given an array of ```k``` linked-lists ```lists```, each linked-list is sorted in ascending order.

**Input:** lists = [[1,4,5],[1,3,4],[2,6]]

**Output:** [1,1,2,3,4,4,5,6]
(Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6)

## 6. (25.) Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list *k* at a time and return its modified list.

*k*  is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of *k*  then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

**Input:** head = [1,2,3,4,5], k = 3

**Output:** [3,2,1,4,5]

## 7. Euler problem #8 Largest product in a series

[Here](https://projecteuler.net/problem=8) is the page with the problem discussed

## 8. Indexing_search
**Input (on the following lines)**:
* number of documents to process (n)
* n lines with multi-word documents (1 document per line) 
* number of queries to be processed (m)
* m lines with single word queries

**Output**:
* m lines (one for each query)
* in each line a list containing the numbers of documents in which a word from a given query occurred
* each list sorted by the frequency of occurrence of the query word in the given document
* If the query word did not occur in any document - return an empty list!




