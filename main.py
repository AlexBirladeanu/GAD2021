my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

asc = sorted(my_list)
print("Ascending order:")
for i in asc:
    print(i)

desc = sorted(my_list, reverse=True)
print("Descending order:")
for i in desc:
    print(i)

odd_numbers = asc[::2]
print("Odd numbers:")
for i in odd_numbers:
    print(i)

even_numbers = asc[1::2]
print("Even numbers:")
for i in even_numbers:
    print(i)

print("Multiples of 3:")
for i in my_list:
    if i % 3 == 0:
        print(i)
