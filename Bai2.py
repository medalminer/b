def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giai_thua(n - 1)

n = int(input("Nhập một số nguyên không âm: "))
if n < 0:
    print("Vui lòng nhập một số nguyên không âm.")
else:
    print(f"Giai thừa của {n} là: {giai_thua(n)}")