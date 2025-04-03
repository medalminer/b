def so_nguyen_to(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while (i * i) <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

try:
    number = int(input("Nhập một số nguyên dương: "))
    if number < 1:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        if so_nguyen_to(number):
            print(f"{number} là số nguyên tố.")
        else:
            print(f"{number} không phải là số nguyên tố.")
except ValueError:
    print("Vui lòng nhập một số nguyên dương hợp lệ.")