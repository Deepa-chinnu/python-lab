number = [3, 5]
text = ["Fizz", "Buzz"]

for i in range(1, 101):
	output = ""
	for j in range(len(number)):
		if i % number[j] == 0:
			output += text[j]
	if output == "":
		output = i
	print(output)
