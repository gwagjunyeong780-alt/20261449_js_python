# aa = [0,0,0,0,0,0,0,0,0,0] 
# hap = 0
# aa[0] = int(input("1번째 숫자 : ")) ## 사용자에게 첫번째 숫자 입력 요구
# aa[1] = int(input("2번째 숫자 : "))
# aa[2] = int(input("3번째 숫자 : "))
# aa[3] = int(input("4번째 숫자 : "))
# aa[4] = int(input("5번째 숫자 : "))
# aa[5] = int(input("6번째 숫자 : "))
# aa[6] = int(input("7번째 숫자 : "))
# aa[7] = int(input("8번째 숫자 : "))
# aa[8] = int(input("9번째 숫자 : "))
# aa[9] = int(input("10번째 숫자 : "))

# hap = aa[0] + aa[1] + aa[2] + aa[3] + aa[4] + aa[5] + aa[6] + aa[7] + aa[8] + aa[9]


# print("합계 ==> %d" % hap)



# bb = []
# cc = []

# value = 0

# for i in range (0,200) :
#     bb.append(value)
#     value+=3

# for i in range (0,200) :
#     cc.append(bb[99-i])

# print("cc[0]에는 %d이, cc[199]에는 %d이 입력됩니다.")



# mylist = [30,10,20]
# print("현재 리스트 : %s" %mylist)

# mylist.append(40)
# print("append(40) 후의 리스트 : %s" % mylist)

# print("pop()으로 추출한 값 : %s" % mylist.pop())
# print("pop 후의 리스트 : %s" % mylist)

# mylist.sort()
# print("sort() 후의 리스트 : %s" %mylist)

# mylist.reverse()
# print("reverse() 후의 리스트 : %s" %mylist)

# print("20 값의 위치 : %d" %mylist.index(20))

# mylist.insert(2,222) ## 2번쨰 자리에 222 삽입
# print("insert(2,222) 후의 리스트 :%s" %mylist)


# list1 = []
# list2 = []

# value = 0

# for i in range (0,4) :
#     for k in range (0,5) :
#         list1.append(value)
#         value += 3
#     list2.append(list1)
#     list1 = []

# for i in range (0,4) :
#     for k in range (0,5) :
#         print ("%3d" % list2[i][k], end=" ")
#     print("")




# ss = 'python is easy. 그래서 programming이 재미있습니다. ^^'
# print(ss.upper())
# print(ss.lower())
# print(ss.swapcase())
# print(ss.title())



inStr = "<<<파<<이>>썬>>>" 
outStr = ""

for i in range(0,len(inStr)) :
    if inStr[i] != '<' and  inStr[i] != '>' :
        outStr += inStr[i]

print("원래 문자열 ==>" + '[' + inStr + ']')
print("공백 삭제 문자열 ==>" + '[' + outStr + ']')
