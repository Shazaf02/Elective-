def skip_elements(elements):
    result = []
    for index, element in enumerate(elements):
    
        if index % 2 == 0:
            result.append(element)
    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) 
