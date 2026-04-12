#Exercise 1
n = int(input())
print(n*2)
#Exercise 2
a , b = map(float, input().split())
N = a*b-(3.14*((a/2)**2))
print('%.2f'%N)
#Exercise 3
c = input()
if len(c) == 1:
    uidoi = ord(c)
    if 65 <= uidoi <= 90:
        print(chr(uidoi + 32))
    elif 97 <= uidoi <= 122:
        print(chr(uidoi - 32))
else:
    print('Nhập mm đi')
#Exercise 4:
c = input()
if len(c) == 1:
    cr7 = ord(c)
    if (65 <= cr7 <= 90) or (97 <= cr7 <= 122):
        print('{c} là kí tu alphabet')
    else:
        print('{c} không phải là kí tu alphabet')
#Exercise 5:
c2 = input()
print(chr(ord(c2)-32)+c2)
#Exercise 6:
a1 , b1 , c1 = map(float, input().split())
if (a1 > 0) and (b1 >0) and (c1 > 0) and (a1 + b1 > c1) and (a1 + c1 > b1) and (b1 + c1 > a1):
    n = (((a1 + b1 + c1)/2)*(((a1 + b1 +c1)/2) - a1)*(((a1 + b1 +c1)/2) - b1)*(((a1 + b1 +c1)/2) -c1))**1/2
    print('%.1f'%n)
else:
    print('“Khong phai 3 canh cua tam giac”')
#Exercise 7:
chuoi = input()
print(chuoi[4], chuoi[8])
#Exercise 8:

