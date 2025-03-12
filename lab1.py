

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


