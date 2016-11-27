import nltk
from nltk import word_tokenize, pos_tag
import random 

print("\n            WELCOME TO PREP TESTER! \nUse Prep Tester to assess your knowledge of prepositions in English :-)\n")

file_path1="/Users/liberato/projetos/preptester/text1.txt"
file_path2="/Users/liberato/projetos/preptester/text2.txt"
file_path3="/Users/liberato/projetos/preptester/text3.txt"

file_path_list=[file_path1, file_path2, file_path3]

file_path=random.choice(file_path_list)
#print("\n*************File Path = \t", file_path) # uncomment to see which file path has been chosen.

file=open(file_path,'r+')
text=file.read()
#print("\n**************Text = \t", text)  #uncomment to see the text that was randomly chosen.

text=word_tokenize(text)

#text=word_tokenize("For the first time in her life she had the chance to go out and explore the world around her.")  #this line is for test purposes only.
tagged_text=nltk.pos_tag(text)
#print(tagged_text)  	#Uncomment this line to check tagging output so as to know
						# whether the words are being tagged correctly.


''' The following block of code:
	1. identifies prepositions in the chosen text,
	2. groups strings which are identified as prepositions into a list (prep_list),
	3. substitutes each preposition by an underline (_______),
	4. regroups (with "join") all the strings from the text into a list (word_list).
'''  
prep_list=[]
word_list=[]
for word in tagged_text:
	if word[1]=="IN" and len(prep_list)<5:
		prep_list.append(word[0].lower())
		index=len(prep_list)
		word_list.append("(%d)________"%index)
	
	else:
		word_list.append(word[0])
print("STEP 1: Read the following text and try to guess which preposition is missing in each underlined space:  --> \n\n", " ".join(word_list))


''' The following block of code:
	0. iterates through the list of prepositions (prep_list),
	1. asks for user input: users must fill in the blanks with their answers,
	2. compares user input to iterated prepositions (prep) = prepositions from prep_list,
	3. counts correct answers into the correct_count variable
	4. stores correct answers into a list (correct_answers)
	5. stores incorrect answers into another list (incorrect_answers)
''' 
index2=1
correct_count=0
correct_answers=[]
incorrect_answers=[]
for prep in prep_list:
	user_input=input ("\n\tNow fill in the blank with your typed answer to blank number (%d): ________"%index2)
	user_input=user_input.lower()
	if user_input==prep: 
		correct_answers.append((index2, prep))
		correct_count=correct_count+1
		#print("\tYour answer is correct!")
	else:
		#print("\tSorry. Wrong answer :-(")
		incorrect_answers.append((index2, user_input, prep))      
	index2=index2+1

print("\n             --> FINAL RESULT: You had ", correct_count, " out of ", len(prep_list), " correct answers.\n")
#print("\nGaps you answered correctly: 1(for), 2 (in)")
#print("\nGaps you answered incorrectly: 3 (at), 10 (in)")
#print("\nCorrect answer for gap (3): around")
#print("\nCorrect answer for gap (10): for\n")

for result in correct_answers:
	print("This is correct = ", "(", result[0], ")", result[1])

print()
for result in incorrect_answers:
	print("This is incorrect = ", "(", result[0], ")", result[1], "\tCorrect answer: ", result[2])


