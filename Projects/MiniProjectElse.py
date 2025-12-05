

def pythonQuiz():
    grade = 0
    print('1. which one is a data type')
    print("A. Fuction")
    print("B. Integer")
    print("C. Float")
    print("D. String")
    userAnwser = input()
    CorrectAnwser = 'a'
    if userAnwser == CorrectAnwser:
        grade +=1
        print('correct')
    else:
        print('Incorrect')
    print('2. What of the fowllowing is a string?')
    print("A. # ")
    print("B."" ")
    print("C. == ")
    print("D. + ")
    userAnwser = input()
    CorrectAnwser = 'B'
    if userAnwser == CorrectAnwser:
        grade +=1
        print('correct')
    else:
        print('incorrect')
        print("3. What of the following is a lists")
        print("A. () ")
        print("B. { } ")
        print("C. [] ")
        print("D. ++ ")
        userAnwser = input()
        CorrectAnwser = 'C'
        if userAnwser == CorrectAnwser:
            grade +=1
            print('correct')
        else:
            print('incorrect')

            print('Here is youur score: ' + str(grade) + ' /3')

            pythonQuiz()