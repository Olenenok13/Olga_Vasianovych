import random
number=int(input("Введите цифру от 0 до 9:  "))
list=[random.randint(0,9) for x in range(10)]
print(list)
for index, element in enumerate(list):
    if element ==number:
        print("Ваша цифра-", element, ", под номером  :", index, "в списке")