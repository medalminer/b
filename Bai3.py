def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

try:
    user_input = input("Nhập các số nguyên (cách nhau bởi khoảng trắng): ")
    arr = list(map(int, user_input.split()))
    
    bubble_sort(arr)
    
    print("Mảng sau khi sắp xếp theo thứ tự tăng dần:", arr)
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ, cách nhau bởi khoảng trắng.")