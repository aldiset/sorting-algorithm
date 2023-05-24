def heap_sort(arr):
    def heapify(arr, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child of root exists and is greater than the largest element
        if left < n and arr[i] < arr[left]:
            largest = left

        # Check if right child of root exists and is greater than the largest element
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Swap root if necessary
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    # Build max heap
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr