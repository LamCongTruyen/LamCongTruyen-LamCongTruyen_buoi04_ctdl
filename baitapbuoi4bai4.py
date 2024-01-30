letter1 = input("hãy nhập vào từ bạn muốn kiểm tra: ") #restful 
letter2 = input("hãy nhập vào từ bạn muốn kiểm tra: ") #fluster
#def checkAnagram(letter1,letter2):
#    if sorted(letter1) == sorted(letter2):
 #       print(f"{letter1} và {letter2} là hai từ đảo chữ ")
 #   else:
 #       print("đây không phải là hai từ đảo chữ")
#checkAnagram(letter1,letter2)

#LIST COMPREHENSION
checkAnagram = [True if sorted(letter1) == sorted(letter2) else False ]
print(checkAnagram)