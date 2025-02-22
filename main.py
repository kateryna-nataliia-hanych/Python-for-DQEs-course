# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import random

l = []
size_of_list = 100

for i in range(0, size_of_list):
    l.append(random.randrange(1000))
print(l)

# l = random.sample(range(0, 1000), size_of_list)
# print(l)

for i in range(0, size_of_list):
    for j in range(size_of_list - i - 1):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print('Sorted list:\n', l)

list_even, list_odd = [], []  # or list_even = list_odd = []
even_sum, odd_sum = 0, 0  # even_sum = odd_sum = 0


for i in range(0, size_of_list):
    if l[i] % 2 == 0:
        list_even.append(l[i])
        even_sum += l[i]
    else:
        list_odd.append(l[i])
        odd_sum += l[i]

print('Even numbers list:\n', list_even)

print('Average for even numbers list:\n', round(even_sum / len(list_even)))

print('Odd numbers list:\n',list_odd)

print('Average for odd numbers list:\n', round(odd_sum / len(list_odd)))


