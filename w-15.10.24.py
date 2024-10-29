# start

# # 1:
multiplied = None
number: float = float(input(" what is number ?"))
if number > 10:
    print(number - 10)
else:
    print(number * 10)

# # 2:
numbers: float = float(input(" what is numbers ?"))
numbers1: float = float(input(" what is numbers 1 ?"))
numbers2: float = float(input(" what is numbers 2 ?"))
if numbers + numbers1 + numbers2 > 100:
    print(numbers + numbers1 + numbers2)
else:
    print("The amount is less than - 100")
#
# # 3 "bonos":
# decimal_number: float = float(input(" what is numbers ?"))
# decimal_number1: float = float(input(" what is numbers ?"))
#
# # 4:
age: int = int(input(" what is age ?"))
if 0 < age < 120:
    print(age)
else:
    print("Incorrect age")

# 5:
three_digit_number: int = int(input(" what is  three digit number ?"))
a: bool = three_digit_number // 10
print(a % 10)

# 6:
n: int = int(input(" what us nummer n ?"))
for i in range(n, 0, -1):
    print(i, end=" ")
print()

# 7:
# for i in range(2):
#     n: int = int(input(" what us nummer n ?"))
#     if n  % 2==0:
#         for a in range(2, n+1, 2):
#             print(a)
#     if not n  % 2==0:
#         for b in range(1,n,3):
#             print(b)

n: int = int(input(" what us nummer n ?"))
nb: int = int(input(" what us nummer nb ?"))
if n and nb % 2 == 0:
    for a in range(n, nb + 1, 2):
        print(a)
if n and nb % 2 != 0:
    for b in range(n + 1, nb, 2):
        print(b)
# # while n and nb % 2==0:
# for i in range(n,nb+1,2):
#     # for i in range(i,2):
#     print(i)
# # for i in range(2):
#     n: int = int(input(" what us nummer n ?"))
#     for a in range(n,n,%2==0):
#         print(a)

# 8:
number_five_three: int = int(input("what is number five three ?"))
# while number_five_three %3==0 or 5==0:
#     for i in range(3 ,number_five_three,3):
#         print(i,end=" ")
# print()

while True:
    if number_five_three <= 0:
        continue
    if number_five_three % 3 == 0:
        for i in range(3, number_five_three, 3):
            print(i, end=" ")
    if number_five_three % 5 == 0:
        for a in range(5, number_five_three + 1, 5):
            print(a, end=" ")
        break
print()

# three: int =0
# five:int =0
# five_three:int=0
# while True:
#     if number_five_three <= 0:
#         continue
#     if number_five_three %3==0 :
#         three+=number_five_three
#         five_three+=three
#     if number_five_three %5==0 :
#         five+=number_five_three
#         five_three+=five
#     for i in range(3, five_three,3):
#         print(i)
#     break


# 9:
number_seven: int = int(input("what is number seven ?"))
for i in range(7, number_seven, 7):
    print(i, end=" ")
print()

# 11:
sum_num: int = 0
while True:
    num: int = int(input(" what is number ?"))
    if num == 0:
        break
    if num < 0:
        sum_num += num
print(sum_num)

# 12:
list_ten: list[int] = []
for a in range(10):
    n: int = int(input(" what this ...? "))
    list_ten.append(n)
    list_ten.sort(reverse=True)
print(list_ten)

# 13:
mona: int = 0
divider: int = 2
while True:
    series: int = int(input(" what is series ?"))
    if series == 0:
        break
    if series <= 1:
        continue
    divider: int = 2
    # for i in series:
    while divider <= series ** 0.5:
        if series % divider == 0:
            break
        divider += 1
    else:
        mona += 1

print(mona)

# 14:
sum_num: int = 0
count: int = 0
mona: int = 0
average: int = 0
for i in range(5):
    num_5: int = int(input("what is numbers 5 ? "))
    count += 1
    sum_num += num_5
    average: bool = sum_num / count
    if num_5 < average:
        mona += 1
print(average)
print(mona)

# 15:

num_1: int = int(input(" what is numbers 1 ? "))
num_2: int = int(input(" what is numbers 2 ? "))
division_num: bool = num_1 / num_2
print(division_num)

# # 16:
three_number: int = int(input("what is three_number ?"))
number_one: bool = three_number // 100
number_two: bool = three_number // 10
number_two1: bool = number_two % 10
number_three: bool = three_number % 10
sum_numbers: bool = number_one + number_two1 + number_three
if sum_numbers % 3 == 0:
    print("divisible in 3")
else:
    print(" not divisible in 3")

# 17:
word: str = str(input(" necklace ... ? "))
# ak:bool=word.join()
# word.join(word)
# print(word)
if word == word[::-1]:
    print("reversed")
else:
    print(" not reversed")

# stop
