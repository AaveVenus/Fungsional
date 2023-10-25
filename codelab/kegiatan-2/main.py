data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

def integer(char):
    return char.isdigit()

integer_values = []

for item in data:
    item_split = item.split()
    integers = list(filter(integer, item_split))
    integer_values.append(integers)

for item in integer_values:
    print(item)