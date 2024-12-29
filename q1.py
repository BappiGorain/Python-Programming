with open("sample.txt","r") as f:
	content = f.read()
	print(content)

with open("sample.txt","r") as f:
	content = f.readlines()
	print(content)
