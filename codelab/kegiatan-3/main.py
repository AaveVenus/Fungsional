random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

def is_float(x):
    return isinstance(x, float)

def is_integer(x):
    return isinstance(x, int)

def is_string(x):
    return isinstance(x, str)

float_values = tuple(filter(is_float, random_list))
int_values = list(filter(is_integer, random_list))
str_values = list(filter(is_string, random_list))

def pecahan(value):
    ratusan = value // 100
    sisa = value % 100
    puluhan = sisa // 10
    satuan = sisa % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}

int_mapped = list(map(pecahan, int_values))

print("Data Float:", float_values)
print("Data Int:")
for item in int_mapped:
    print(item)
print("Data String:", str_values)
