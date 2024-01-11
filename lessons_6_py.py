# a=[1,2,3]
# b=[1,2,3,4,5,6,7]

# for i in range (10):
#     for j in range (10):
#         for j in range(10):
#             print(f' {i,j}\t', '=', i*j)  
#     print ()


# a=10
# for i in range (1,a+1):
#             print("*" * i) 
        
# a=10
# for i in range (1,a+1):
#             print("*", end='_' ) 
        

# for j in range (3,0,-1):
#     for i in range (i,0,-1):
#         print('*',end ='\n' if i == 2 else " ") 
        
        
        
# for i in range(3,0,-1):
#     for j in range(i, 0, -1):
#         print("*", end = " ")
#         print()

# Домашнее задание №1
#Напишите программу, которая будет в лесенку выстраивать числа от произвольного положительного числа .

a= int(input('Введите положительное число- '))
s=''
for i in range (1,a+1):
    s+=str(i)
    print(s)


# Домашнее задание №2
#Постройте следующую картину. (квадратная таблица умножения)


print(" ", "1","2","3","4","5","6","7","8","9")
for x in range (1, 10):
    print(x, end=' ')
    for y in range (1,10):
        print(x*y, end=' ')
    print()