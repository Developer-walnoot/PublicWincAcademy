from helpers import random_koala_fact

__winc_id__ = "c0dc6e00dfac46aab88296601c32669f"
__human_name__ = "while"


def unique_koala_facts(x):
    y = 0
    list_x = []
    while y < x:
        item = random_koala_fact()
        if item not in list_x:
            list_x.append(item)
        else:
            item = random_koala_fact()
            if item not in list_x:
                list_x.append(item)
        y = y + 1
    return list_x


def all_facts():
    new_list = []
    counter = 0
    x = 120
    while counter < x:
        counter = counter + 1
        random_fact = random_koala_fact()
        random_fact_chance = random_koala_fact()
        if random_fact not in new_list:
            new_list.append(random_fact)
        elif random_fact in new_list:
            random_fact = random_koala_fact()
            if random_fact not in new_list:
                new_list.append(random_fact)
    return new_list


def num_joey_facts():
    all_koala_fact = all_facts()
    joeylist = [x for x in all_koala_fact if "joey" in x]
    return int(len(joeylist))


def koala_weight():
    all_facto = all_facts()
    teller = 0
    weight = [x for x in all_facto if "kg" in x]
    y = len(weight)
    counter = 0
    item = weight[counter]
    if y > 1:
        print("more then one")
    result = item.index("kg")
    if item[result] == "k" and result - 1 != " ":
        last_number_index = result - 1
        x = last_number_index
        last_number = item[x]
        while item[x] != " ":
            x = x - 1
            first_number_index = x
    first_number_index = first_number_index + 1
    return int(item[first_number_index : last_number_index + 1])


# This block is only executed if this script is run directly (python main.py)
# It is not run if you import this file as a module.
if __name__ == "__main__":
    print(unique_koala_facts(60))
    # print(koala_weight())
    # print
#    unique_koala_facts(x)
