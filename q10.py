with open("sample.txt","r") as f:
	content = f.read()
	vowels = []
	vowel = ['a','e','i','o','u']
	for ch in content:
		if ch in vowel:
			vowels.append(ch)
print(vowels)
