words = {
	3:"Fizz", 
	5:"Buzz",
}

for i in range(1, 101):
	output = ""
	for number in words:
		if i % number == 0:
			output += words[number]
	if output == "":
		output = i
	print(output)