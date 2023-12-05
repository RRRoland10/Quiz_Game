quiz = {
    'question1': {
        'question': 'Where is the HQ of the Red Bull F1 team?',
        'answer': 'Milton Keynes'
    },
    'question2': {
        'question': 'Who won the drivers championship in F1 in 2005?',
        'answer': 'Fernando Alonso'
    },
    'question3': {
        'question': 'Is there a track in the Netherlands?',
        'answer': 'Yes'
    },
    'question4': {
        'question': 'Who is the team leader of Mclaren F1?',
        'answer': 'Andrea Stella'
    },
    'question5': {
        'question': 'Who is the race engineer of Max Verstappen?',
        'answer': 'GP' 
    },
    'question6': {
        'question': 'Which company is the tyre supplier of F1?',
        'answer': 'Pirelli'
    },
    'question7': {
        'question': 'What is the engine supplier of Haas F1?',
        'answer': 'Ferrari'
    }
    
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('Answer?')

    if answer.lower() == value['answer'].lower():
        print('correct')
        score = score + 1
        print('Your score is: ' + str(score))

    else:
        print('Wrong!')  
        print('The answer is : ' + value('answer')) 
        print('Your score is : ' + str(score)) 
