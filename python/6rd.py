# for _ in range(0, 3, 1):
#     print("안녕하세요? for 문을 공부 중입니다")
#
# for i in range(1, 100, 2):
#     print("%d" % i, end=" ")
#
# for i in range(2, 101, 2):
#     print("%d" % i, end=" ")


# i, hap = 0, 0
#
# for i in range(1, 11, 1):
#     hap = hap + i
#
# print("1에서 10까지의 합계 : %d" % hap)
#
#
# i, odd_sum = 0, 0
#
# for i in range(1, 101, 2):
#     odd_sum = odd_sum + i
#
# print("1부터 100까지 홀수의 합 : %d" % odd_sum)
#
#
# i, even_sum = 0, 0
#
# for i in range(2, 101, 2):
#     even_sum = even_sum + i
#
# print("1부터 100까지 짝수의 합 : %d" % even_sum)
#
#
# i , dan = 0,0
#
# dan = int(input("단을 입력하세요 : "))
#
# for i in range (1,10,1) : 
#     print("%d * %d = %2d" % (dan,i,dan * i)) 
#
# for i in range(2 , 10 , 1) :
#     print ("## %d단 ## " % i , end="\t")
# print ()

# for k in range(1, 10, 1):
#      for i in range(2, 10, 1):
#          print("%d * %d = %2d" % (i, k, i * k), end="\t")
#      print()
# for i in range(9 , 1 , -1) :
#     print ("## %d단 ## " % i , end="\t")
# print ()

# for k in range(9 , 0 , -1):
#      for i in range(9, 1, -1):
#          print("%d * %d = %2d" % (k, i, k * i), end="\t")
#      print()






# hap = 0

# for i in range(1, 11):
#     hap += i

# print("1에서 10까지의 합계 : %d" % hap)

# hap = 0
# a,b, = 0,0

# while True :
#     a = int(input("더할 첫 번째 수를 입력하세요 : "))
#     if a ==0 :
#         break
#     b = int(input("더할 두 번쨰 수를 입력하세요 : "))
#     hap = a + b
#     print ("%d +%d = %d" % (a,b,hap))

# print("0을 입력해 반복문을 탈출했습니다.")    

# hap, i = 0,0

# for i in range(1,101) :
#     if i %3 == 0 :
#         continue
#     hap += i

# print("1~100의 합계 (3의 배수 제외) : %d" % hap)


for i in range (1, 51):
    print("*" * i)

print ("##########################")


for i in range (49 , 0 , -2) :
    print(" " * ((51 - i )// 2) + "*" * i)

for i in range(1,51,2):
    print(" " * ((51 - i) // 2 )+ "*" * i )
