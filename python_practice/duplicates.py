# 3. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
# Hint: Use set() to store a number of values without duplicates. 



def remove_duplicates(input_list):
    unique_list = []
    seen = set()

    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)

    return unique_list

input_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
result = remove_duplicates(input_list)

result.reverse()
print(result)

                