validity = []


def decimal_to_binary(num):
    while num!=1 and num>0:
        if num%2 == 0:
            validity.append(False)
            num = int(num/2)
        else:
            validity.append(True)
            num = int((num-1)/2)
    
    if num == 0:
        validity.append(False)
    else:
        validity.append(True)

def binary_to_decimal(num):
    final=0
    if num == 1:
        return(1)
    else:
        bin = list(num)
        for j in range(0,len(bin)):
            if int(bin[j])== 1 or 0:
                final = final+int(bin[j])*pow(2,len(bin)-j-1)
                return final
            else:
                return 'this is not binary'
    

def display2():
    a = input('enter binary: ')
    print(binary_to_decimal(a))


def display():
    w =''
    tem = len(validity)
    for i in range(0,tem):
        if validity[tem-1] == True:
            w = w+'1'
        else:
            w= w+'0'
        tem-=1
    print(w)
        

def main():
    q = int(input("enter 1 for decimal to binary \n enter 2 for binary to decimal \n"))
    if q == 1:
        a = int(input('enter decimal: '))
        decimal_to_binary(a)
        display()
    elif q ==2:
        display2()
    
    else:
        print('invalid input')

main()