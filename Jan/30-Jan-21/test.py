list1 = ["Hello", "take"] 
list2 = ["dear", "sir"]
lst = []
for i in list1:
	for j in range(len(list2)):
		lst.append(i + " " + list2[j])
print(lst)