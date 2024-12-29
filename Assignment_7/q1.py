word = 'balloon'
newWord = ''
n = len(word)
for i in range(n-1):
	if word[i] != word[i+1]:
		newWord = newWord + word[i]
	else:
		newWord = newWord + '*'
if word[n-2] == word[n-1]:
	newWord = newWord + '*'
else:
	newWord = newWord + word[n-1]
print(newWord)
