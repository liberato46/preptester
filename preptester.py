import nltk
from nltk import word_tokenize, pos_tag

text=word_tokenize("For the first time in her life she had the chance to go out and explore the world around her.")
tagged_text=nltk.pos_tag(text)
print(tagged_text)

prep_list=[]
word_list=[]
for word in tagged_text:
	if word[1]=="IN":
		prep_list.append(word[0])
		index=len(prep_list)
		word_list.append("(%d)________"%index)
	
	else:
		word_list.append(word[0])
print("Please fill in the blanks:   ", " ".join(word_list))

index2=1
correct=0
for prep in prep_list:
	user_input=input ("Please type a preposition for blank space number (%d): "%index2)
	index2=index2+1
	if user_input==prep:
		correct=correct+1
		print("Your answer is correct!")
	else:
		print("Sorry. Wrong answer :-(")
print("FINAL RESULT: You had ", correct, " out of ", len(prep_list), " correct answers.")
