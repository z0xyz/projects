#This script is done
#However Beware that this might cause a problem for you because it works on the system
#! python3
#Random quiz generator
#Create quizzed with questions and answers) in a random order along with answer keys

# TODO

# -create 35 different quizzes																			(DONE)
# -Create 50 multiple-choice questions for each quiz , in random order									(DONE)
# -Provide the correct answer and three random wrong answers for each questions , in random order		(DONE)
# -Write the quizzes to 35 text files 																	(DONE)
# -Write the answer keys to 35 text quiz-files															(DONE)


# The coding

# # -Stores the states and their capitals in a dictionary	(DONE)
# -Call open() , write() , and close() for the quiz and answer key text findertools
# -User random.shuffle() to randomize the order of the questions and multiple-choice options

import os
import random

# The quiz data : States and their capitals 
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}


for quiz in range(1,36):
	#Create the quiz and answer key files

	# First phase : opening the files 
	quizFile = open("/media/usr/localdisk/python/python-projects/project-random-quiz/quiz-files/capital-quiz-{}".format(quiz) , "w")
	answerFile = open("/media/usr/localdisk/python/python-projects/project-random-quiz/quiz-files/capital-quiz-answer-{}".format(quiz) , "w")

	# Second phase : writing to the files 
	quizFile.write(f"This is the quiz number {quiz} ")
	quizFile.write("Name:\n\nDate:\n\nPeriod:\n\n")
	quizFile.write((" "*20) + "State capitals Quiz Form Number :{}\n\n\n".format(quiz))

	# Shuffle the order of states
	states = list(capitals.keys())
	random.shuffle(states)

	#Loop through all the 50 states , making a question for each .

	for questionNum in range(50):
		# Getting the correct answer 
		correctAnswer = capitals[states[questionNum]]
		# Getting the wrong answer
		allAnswers = list(capitals.values())
		del allAnswers[allAnswers.index(correctAnswer)]
		# The final four options
		wrongAnswers = random.sample(allAnswers , 3)
		answerOptions = wrongAnswers + [correctAnswer]
		random.shuffle(answerOptions)

		# Write the question and the answer to the quiz file
		quizFile.write(f"{questionNum} - what is the capital of the {states[questionNum]} in the United states of America ?\n")
		for i in range(4):
			quizFile.write(f"{'ABCD'[i]} . {answerOptions[i]} \n")

		# Writing to the quiz questions file 
		quizFile.write("\n")

		# Write the answers to the answer file
		answerFile.write(f"The answers for the quiz number ({quiz})\n\n\n")
		answerFile.write(f"The answer for the question ({questionNum}) is that ({correctAnswer}) is the captial of the state({states[questionNum]})\n")
		correctAnswerLetter  = "ABCD"[answerOptions.index(correctAnswer)]
		answerFile.write(f"It's number {correctAnswerLetter}")

quizFile.close()
answerFile.close()




