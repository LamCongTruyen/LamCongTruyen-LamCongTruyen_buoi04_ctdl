n = int(input("hãy nhập chuỗi nguyên cần đảo ngược: "))
total = 0
if n <0 :
    print("vui lòng nhập lại")
else:
    while(n > 0) :
        temp = n % 10
        total = total * 10 + temp
        n = n//10
print(f"số đảo ngược là : {total}")

#LIST COMPREHENSION:
#total = [i for i in str(n)[::-1]]
#print(total)




