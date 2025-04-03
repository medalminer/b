def fibonacci(n):
    fib = [0] * (n + 1)
    fib[1] = 1
    if n > 1:
        fib[2] = 1
        
    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    
    return fib[n]

try:
    n = int(input("Nhập vào một số nguyên dương: "))
    if n < 1:
        print("Vui lòng nhập một số nguyên dương lớn hơn hoặc bằng 1.")
    else:
        result = fibonacci(n)
        print(f"Số Fibonacci thứ {n} là: {result}")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")