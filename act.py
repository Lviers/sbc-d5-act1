"""n = input("Naa ba si boss?: ").lower()
print(n)


boss = False

while not boss :
    l = [1,2,3,4,5]
    if n == "naa":
        print(l),l.pop(0),print(l),l.pop(0),print(l),l.pop(0),print(l),l.pop(0),print(l),l.pop(0),print(l)
        boss = True
    elif n == "wala":
        print(l),l.pop(-1),print(l),l.pop(-1),print(l),l.pop(-1),print(l),l.pop(-1),print(l),l.pop(-1),print(l)
        boss = True
    else:
        print("Bruh")   
        boss = True   """ 

num1,num2,num3 = int(input("Enter Number: ")),int(input("Enter Number: ")),int(input("Enter Number: "))

n = input("Naa ba si boss?: ").lower()
print(n)

boss = False

while not boss :
    l = [num1,num2,num3]
    if n == "naa":
        print(l),l.pop(0),print(l),l.pop(0),print(l),l.pop(0)
        boss = True
    elif n == "wala":
        print(l),l.pop(-1),print(l),l.pop(-1),print(l),l.pop(-1),l.pop(-1)
        boss = True
    else:
        print("Bruh")   
        boss = True   