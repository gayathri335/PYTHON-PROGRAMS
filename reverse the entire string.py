user_input=input("input:")
#convert the string into list for reverse operation
words=user_input.split()
#reverse the order of words in the list
reversed_words=list(reversed(words))
#join the reversed words into a single string
reversed_string=' '.join(reversed_words)
print("output:",reversed_string)
