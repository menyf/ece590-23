# Project Report 1: Sorting

Students Name and NetID: 

- Yifan Men(ym129)
- Yuqiao Liang(yl543)


## Selection Sort
The main idea of selection sort that we have two array, one is sorted and the other is unsorted. We pick up the smallest element from the unsorted array and add it to the end of the sorted array. 
The time complexity of selection sort is $O(n^2)$
![](SelectionSort.png)


## Insertion Sort
The idea behind insertion sort is similar to selection sort. The difference is that in insertion sort, we pick the next element from the unsorted list instead of the smallest. Then we insert this element into the sorted array at the correct order(by assending order). The time complexity of selection sort is $O(n^2)$
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
Quick sort use the devide and conquer philosophy. First we need to choose one element as pivot. Then partition the array into two parts. On the left is everything smaller than pivot, on the right is everything bigger than pivot. After each partition, we will recursively call the partition process. 
![](QuickSort.png)

## Overall

![](log.png)

![](Python.png)

![](sorting.png)


