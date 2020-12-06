inputFile = open('D6P1.txt', 'r')
FileLines = inputFile.readlines();

answeredQuestions = {}
groupSize = 0
answerCount = 0

def countUpAnswers(answeredQuestions, groupSize):
    answerCount = 0
    
    for question in answeredQuestions:
        if answeredQuestions[question] == groupSize:
            answerCount += 1
    return answerCount

for line in FileLines:
    if len(line) <= 1:
        answerCount += countUpAnswers(answeredQuestions, groupSize)
        
        answeredQuestions = {}
        groupSize = 0
        continue
    
    groupSize += 1
    
    for i in range(len(line)):
        question = line[i]
        
        if question.isspace():
            continue
        
        if question not in answeredQuestions:
            answeredQuestions[question] = 0
        
        answeredQuestions[question] += 1

if groupSize:
    answerCount += countUpAnswers(answeredQuestions, groupSize)

print(f"The amount of questions answered 'yes' is {answerCount}")
    