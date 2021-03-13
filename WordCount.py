sentence = input("Enter your sentence here:")
wordCount = 0
for i in sentence:
    if(i == ' '):
        wordCount = wordCount+1
print("Number of words in the sentence is ")
print(wordCount + 1)