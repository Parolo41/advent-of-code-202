inputFile = open('D6P1.txt', 'r')
FileLines = inputFile.readlines();

answeredQuestions = []
answerCount = 0

for line in FileLines:
    if len(line) <= 1:
        answeredQuestions = []
        continue
    
    for i in range(len(line) - 1):
        question = line[i]
        
        if question not in answeredQuestions:
            answeredQuestions.append(question)
            answerCount += 1

print(f"The amount of questions answered 'yes' is {answerCount}")
    