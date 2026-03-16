def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1  # Nie znaleziono

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)


# Test
tablica = [2, 5, 8, 12, 15, 18, 22, 27, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85]
print(binary_search_recursive(tablica, 55))  # Wynik: 13
