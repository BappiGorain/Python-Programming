with open("sample.txt","r") as f:
	content = f.read()
	words = content.split()
	print(words)
	count = 0
	for word in words:
		count+=1
	print(count)

