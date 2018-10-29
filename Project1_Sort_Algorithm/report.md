# Project Report 1: Sorting

Students Name and NetID: 

- Yifan Men(ym129)
- Yuqiao Liang(yl543)


## Selection Sort
![](SelectionSort.png)

## Insertion Sort
![](InsertionSort.png)

## Bubble Sort
![](BubbleSort.png)

The algorithm takes $O(n^2)$ time complexity. It is a deterministic sorting algorithm, any array can be sorted in this time complexity. 

This algorithm requries iterations through the array. By comparing the pairs of numbers, it makes the the pairs in an ascending order. Keep doing so until no more swaps are made. For each pass, the $k$th largest element gets placed at the $k$th iteration. So we only need to iterate through the first $n-k$ elements at each pass.

## Merge Sort
![](MergeSort.png)

The algorithm takes $O(nlogn)$ time complexity. It is a divide and conquer algorithm, any array can be sorted in this time complexity. 

This algorithm try to divide the array into two halves, so that the small part will be sorted. The base case of each subarray is 1-element or 2-element array. With two sorted subarray, it is easy to merge the two with a new array which is sorted.

## Quick Sort
![](QuickSort.png)

## Overall

![](log.png)

![](Python.png)

![](sorting.png)