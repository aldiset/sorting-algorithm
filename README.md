# Sorting Algorithms

This repository contains implementations of various sorting algorithms in Python. Each algorithm is explained briefly along with example code.

## Algorithms

1. Selection Sort

    Explanation:
    - Selection Sort works by dividing the input list into two parts: the sorted portion at the beginning and the unsorted portion at the end.
    - In each iteration, the algorithm finds the minimum (or maximum) element from the unsorted portion and swaps it with the first element of the unsorted portion, effectively expanding the sorted portion by one element.
    - This process is repeated until the entire list becomes sorted.
    - Selection Sort has a time complexity of O(n^2) in all cases, making it inefficient for large input sizes.

    Example usage:
    ```python
    def selection_sort(arr):
        # Implementation goes here

    arr = [64, 25, 12, 22, 11]
    sorted_arr = selection_sort(arr)
    print(sorted_arr)
    ```

2. Bubble Sort

    Explanation:
    - Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
    - In each pass, the largest (or smallest) element "bubbles" up to its correct position at the end (or beginning) of the list.
    - The process is repeated until the list becomes fully sorted.
    - Bubble Sort has a time complexity of O(n^2) in the worst and average cases, making it inefficient for large lists. However, it has the advantage of having a best-case time complexity of O(n) when the list is already sorted.

    Example usage:
    ```python
    def bubble_sort(arr):
        # Implementation goes here

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bubble_sort(arr)
    print(sorted_arr)
    ```

3. Insertion Sort

    Explanation:
    - Insertion Sort works by maintaining a sorted portion at the beginning of the list and repeatedly inserting elements from the unsorted portion into the correct position within the sorted portion.
    - It iterates through the list, comparing each element with the elements in the sorted portion and shifting them to the right to make space for the new element.
    - Insertion Sort is efficient for small lists or partially sorted lists and has a best-case time complexity of O(n) when the list is already sorted. However, it has a worst-case and average-case time complexity of O(n^2).

    Example usage:
    ```python
    def insertion_sort(arr):
        # Implementation goes here

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)
    ```

4. Merge Sort

    Explanation:
    - Merge Sort is a divide-and-conquer algorithm that divides the list into two halves, recursively sorts them, and then merges the sorted halves to produce the final sorted list.
    - It repeatedly divides the list until each sublist contains only one element, and then merges them by comparing the elements in a sorted manner.
    - Merge Sort has a time complexity of O(n log n) in all cases, making it efficient for large lists. It is also stable and guarantees a consistent performance.

    Example usage:
    ```python
    def merge_sort(arr):
        # Implementation goes here

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print(sorted_arr)
    ```

5. Quick Sort

    Explanation:
    - Quick Sort is another divide-and-conquer algorithm that selects a pivot element and partitions the list into two sublists, one with elements smaller than the pivot and another with elements larger than the pivot.
    - It recursively sorts the sublists by selecting a new pivot and partitioning until the entire list becomes sorted.
    - Quick Sort has an average time complexity of O(n log n) and is generally faster in practice compared to other sorting algorithms. However, it has a worst-case time complexity of O(n^2) when the pivot selection is poor.

    Example usage:
    ```python
    def quick_sort(arr):
        # Implementation goes here

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = quick_sort(arr)
    print(sorted_arr)
    ```

6. Heap Sort

    Explanation:
    - Heap Sort utilizes a binary heap data structure to sort the list.
    - It first builds a max heap (for sorting in ascending order) or a min heap (for sorting in descending order) from the input list.
    - The algorithm repeatedly extracts the root element (the maximum or minimum) from the heap and places it in the sorted portion of the list.
    - Heap Sort has a time complexity of O(n log n) in all cases and is considered an efficient sorting algorithm. It also has the advantage of being an in-place sorting algorithm.

    Example usage:
    ```python
    def heap_sort(arr):
        # Implementation goes here

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = heap_sort(arr)
    print(sorted_arr)
    ```

7. Counting Sort

    Explanation:
    - Counting Sort is a non-comparison-based sorting algorithm that works well when the range of input values is small.
    - It counts the frequency of each distinct element in the input list and then uses the counts to determine the sorted order.
    - Counting Sort has a time complexity of O(n + k), where n is the number of elements in the input list and k is the range of input values. It is efficient for sorting integers with a small range.

    Example usage:
    ```python
    def counting_sort(arr):
        # Implementation goes here

    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = counting_sort(arr)
    print(sorted_arr)
    ```
