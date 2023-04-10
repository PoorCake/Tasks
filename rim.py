slov = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1
}
a = (input("Введите число от 1 до 1000: "))
num = 0
i = 0
while i<len(a)-1:
    if slov[a[i]]<slov[a[i+1]]:
        num -= slov[a[i]]
    else:
        num += slov[a[i]]
    i+=1
num += slov[a[i]]
print(num)