#Basic
for x in range(150 + 1):
    print(x)
#Multipes of 5
for x in range(5, 1000 + 1, 5):
    print(x)
#Counting the Dojo Way
for x in range(1, 100 + 1):
    if x % 5 == 0:
        print("Coding")
    if x % 10 == 0:
        print("Dojo")
    else:
        print(x)
#Whoa. That Sucker's Huge
sum = 0

for x in range(0, 500000+1):
    if x % 2 != 0:
        sum += x
        print(sum)
#Countdown by 4s
for x in range (2018, 0, -4):
        print(x)
#Flexible Counter
lowNum = 3
highNum =75
mult = 2

for x in range(lowNum,highNum +1):
    if x % mult == 0:
        print(x)