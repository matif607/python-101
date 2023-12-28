from simple_deepcopy import my_deepcopy
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "teacher"]],
    "J-P": ["Roberts", ["Programmer", "teacher"]],
}

copy_1  = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"][1].append("Cashier")
jp_list = original["J-P"]
jp_list[1].append("Courier")

print(original)
print(copy_1)
print(copy_2)