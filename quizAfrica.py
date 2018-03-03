
# Creates number of quizzes with questions in random order

import random

# Empty dictionary
capitals = {}

# Get values to a dictionary from a csv file
with open('dictionary.csv', 'r') as dict:
    for line in dict:
        (key, val) = line.split(',')
        capitals[str(key)] = val


# Generate 35 quiz sheets:

for quizNum in range(35):

    # Create quiz sheets and answer keys sheets
    quizFile = open('quizSheet_%s.txt' % (quizNum + 1), 'w')
    quizAnswers = open('quizKey_%s.txt' % (quizNum + 1), 'w')
    quizFile.write('Name: \n\nDate: \n\n\n\n')
    quizFile.write((' ' * 20) + 'African Countries Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n\n')

    # Randomize capitals
    states = list(capitals.keys())
    random.shuffle(states)

    # Create questions
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # Generate wrong answers
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]

        # Shuffle correct and wrong options
        random.shuffle(answerOptions)

        # Write question text
        quizFile.write('%s. What is the capital of %s?\n\n' % (questionNum + 1, states[questionNum]))

        # Nested for loop to create answer options
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD'[i], answerOptions[i]))
            quizFile.write('\n\n')

        quizAnswers.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    quizAnswers.close()
