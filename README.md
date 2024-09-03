# Quick Sort Performance Analysis
This project implements the Quick Sort algorithm and profiles its performance using Python's cProfile. The sorting algorithm is tested on random arrays of sizes ranging from 1,000 to 10,000 elements, and the results are analyzed to verify the time complexity prediction.

## Project Structure
  -  sorter.py: Contains the implementation of the Quick Sort algorithm.
  -  main.py: Handles profiling of the sorting algorithm, data collection, and plotting results.

## Features
  -  Implementation of Quick Sort algorithm in Python.
  -  Profiling of the algorithm using cProfile to measure performance.
  -  Analysis of time complexity with graphical representation.
  -  Reflection on the relation between empirical data and theoretical time complexity.

## Quick Sort Algorithm
Quick Sort is a divide-and-conquer algorithm that sorts by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.

  -  Average Case Time Complexity: O(n log n)
  -  Worst Case Time Complexity: O(n^2) (occurs when the pivot selections are poor, such as always picking the smallest or largest element as the pivot)

## Performance Analysis

The graph above shows the time taken to sort arrays of various sizes using Quick Sort. The curve demonstrates that the sorting time grows slower than a quadratic algorithm, which aligns with Quick Sort's average-case time complexity of O(n log n).

## Reflections
The C Profile data closely matches the expected O(n log n) time complexity of Quick Sort. As the input size increases, the time taken to sort grows moderately, validating Quick Sort's efficiency for average cases. The results highlight the logarithmic component's influence, which tempers the growth in sorting time even as the array size increases significantly.
