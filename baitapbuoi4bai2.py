a = input('Hãy nhập vào mảng bạn muốn kiểm tra: ') #input [1,2,3,4,5] 
b = a[::-1]
if a == b:
    print(f"yes {a} is  A palindrome")
else:
    print("no")