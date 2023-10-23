number = [1,2,3,4,5]

def find_number(num):
    return num * 2

map_number = map(find_number, number) 
print(map_number)
for x in map_number:
    print(x)       