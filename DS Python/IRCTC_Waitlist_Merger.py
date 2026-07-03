list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

result = []
i = j = 0

while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result.append(list1[i])
        i += 1
    else:
        result.append(list2[j])
        j += 1

while i < len(list1):
    result.append(list1[i])
    i += 1

while j < len(list2):
    result.append(list2[j])
    j += 1

print("Merged List:", result)
