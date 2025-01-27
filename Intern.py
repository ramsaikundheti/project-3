from collections import Counter
def count_vibgyor(input_string):
    target_string = "VIBGYOR"
    input_counts = Counter(input_string)
    min_count = float('inf')
    for char in target_string:
        if char in input_counts:
            min_count = min(min_count, input_counts[char])
        else:
            return 0  
    return min_count
input_string = "VBGYROIVGBYOGRIIVBGORYY"
result = count_vibgyor(input_string)
print(result)