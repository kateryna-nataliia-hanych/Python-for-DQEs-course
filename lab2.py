import random
import string

# generate random number of dicts in list
num_dicts = random.randrange(2, 11)
print(num_dicts)

list = []
for i in range(num_dicts):
    dict = {}
    # generate dictionary with random number of keys
    for key in range(random.randrange(1, 11)):
        dict[random.choice(string.ascii_lowercase)] = random.randrange(0, 101)

    list.append(dict)

    print(f"Random {i+1} dictionary", dict)
# list = [{'a': 5, 'b': 7, 'K':10, 'g': 11}, {'a': 3, 'c': 35, 'g': 42}, {'a': 10, 'c': 35, 'g': 52}]

print("List with random dictionaries:\n", list)

common_dict = {}
for index, dict in enumerate(list, 1):

    for key, value in dict.items():

        if key in common_dict:

            if value > common_dict[key][0]:
                common_dict[key] = (value, index)
            elif value == common_dict[key][0]:
                continue

        else:

            common_dict[key] = (value, index)

merged_dict = {k + f"_{v[1]}": v[0] for k, v in common_dict.items()}

print("Merged dictionary with updated keys and max value:\n", merged_dict)
