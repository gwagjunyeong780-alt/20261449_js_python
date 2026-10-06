##a = 9
##b = 2
##print (a//b) 
##print (a%b)
##print (a**b)

#a = 9
#a +=3
#print(a)
#a -=3
#print(a)
#a *=3
#print(a)
#a /=3
#print(a)
#a //=3
#print(a)
#a %=3
#print(a)
#a **=3
#print(a)

#print("관계 연산자")
#a = 3
#b = 9
#print (a ==b)
#print (a != b)
#print (a > b)
#print (a < b)
#print (a >= b)
#print (a<= b)

#s1,s2,s3 = "100","100.123","9999999999999999999999999"
#print(int(s1) + 1, float(s2) + 1, int(s3) + 1)

#money,c500,c100,c50,c10 = 0,0,0,0,0 ## 동전으로 교환할 돈과 500원,100원,50원,10원짜리 동전의 개수를 저장 할 변수를 초기화
#money = int(input("교환할 돈은 얼마?"))
#c500 = money // 500 ## 500원짜리 동전의 개수를 구함
#money %= 500 ##다시 money를 500으로 나눈 후 나머지값 저장
#c100 = money // 100 ##100원짜리 동전을, 42~43행에서 50웑짜리 동전을,44~45행에서 10원짜리 동전을 구함
#money %= 100 
#c50 = money //50
#money %= 50
#c10 = money //10
#money %= 10

#print("\n 500원짜리 ==> %d개" % c500)
#print(" 100원짜리 ==> %d개" % c100)
#print("50원짜리 ==> %d개" %c50)
#print("10원짜리 ==> %d개" %c10)
#print("바꾸지 못한 잔돈 ==> %d원 \n" % money)

#money2,c10000_2,c5000_2,c1000_2 = 0,0,0,0
#money2 = int(input("\n새로 교환할 돈은 얼마?"))
#c10000_2 = money2 // 10000
#money2 %= 10000
#c5000_2 = money2 // 5000
#money2 %= 5000
#c1000_2 = money2 // 1000
#money2 %= 1000

#print("\n10000원짜리 ==> %d개" % c10000_2)
#print("5000원짜리 ==> %d개" % c5000_2)
#print("1000원짜리 ==> %d개" % c1000_2)
#print("바꾸지 못한 잔돈 ==> %d원\n" % money2)

#a = 200

#if a < 100:
#    print ("100보다 작군요.")
#print("거짓이므로 이 문장은 안 보이겠죠?")

#print("프로그램 끝")

#a = int(input("정수를 입력하세요 : "))
#if a %2 == 0 :
#    print("짝수를 입력했군요.")
#else :
#    print("홀수를 입력했군요.")

#a = 75

#if a > 50 :
#    if a <100 :
#        print("50보다 크고 100보다 작군요.")
#    else :
#        print("와~ 100보다 크군요.")
#else :
#    print ("에고 50보다 작군요.")


score = int(input("점수를 입력하세요 : "))

if score >= 95:
    print("A+")
elif score >= 90:
    print("A0")
elif score >= 85:
    print("B+")
elif score >= 80:
    print("B0")
elif score >= 75:
    print("C+")
elif score >= 70:
    print("C0")
elif score >= 65:
    print("D+")
elif score >= 60:
    print("D0")
else:
    print("F")
print ("학점입니다. ^^")

