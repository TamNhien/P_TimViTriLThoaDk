L = list(map(int, input("Nhap vao ds cac so nguyen, cach nhau boi dau phay: ").split(',')))
print(next((i for i in range(1, len(L) - 1) if L[i] == L[i-1] * L[i+1]), -1))
