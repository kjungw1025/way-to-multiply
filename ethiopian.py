import math
def mul():
    number1=int(input("첫번째 숫자를 입력하시오: "))
    number2=int(input("두번째 숫자를 입력하시오: "))
    number_total=0

    while number1>0:
        if number1%2!=0:
            number_total+=number2
        number1=number1//2
        number2=number2*2
        
    print(number_total)
mul()
