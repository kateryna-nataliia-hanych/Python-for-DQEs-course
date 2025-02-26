import random
import string

# generate random number of dicts in list
def generate_random_dicts(start, stop):
    num_dicts = random.randint(start, stop)
    print(num_dicts)

    list = []
    for i in range(num_dicts):
        # generate dictionary with random number of keys
        dict = {random.choice(string.ascii_lowercase): random.randint(0, 100) for _ in range(random.randint(1, 10))}

        print(f"Random {i + 1} dictionary", dict)

        list.append(dict)

    return list


def merging_dicts(list_dicts):
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
    return merged_dict


list = generate_random_dicts(2, 10)
merged_dict = merging_dicts(list)
print(f"List with random dictionaries:\n {list}")
print(f"Merged dictionary with updated keys and max value:\n {merged_dict}")