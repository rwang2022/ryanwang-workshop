
# SUMMARY OF TRIO DISCUSSION
# ...
# DISCOVERIES
# ...
# QUESTIONS
# ...
# COMMENTS
# ...

import random

pd1 = "pd1.txt"
with open(pd1) as file:
    list1 = []
    for line in file:
        list1.append(line.strip())
    # print(list1)

pd2 = "pd2.txt"
with open(pd2) as file:
    list2 = []
    for line in file:
        list2.append(line.strip())
    # print(list2)

list3 = list1 + list2

big_list = {
    "pd1" : list1,
    "pd2" : list2,
    "pd_all" : list3,
}

print("The random choice for pd1 is " + random.choice(big_list["pd1"]) + ".")
print("The random choice for pd2 is " + random.choice(big_list["pd2"]) + ".")
print("The random choice for both pds is " + random.choice(big_list["pd_all"]) + ".")
