print('Hope you will enjoy this game \n')
answer=input('Are you excited to play this game? [answer with (yes/no)]\n :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('\n\t1: A couple went for a picnic. They have 5 sons and each son have 7 sisters and each sister have 2 babies. In total how many people went for the picnic? (solutions to be written in words)\t')
    if answer.lower()=='two':
        score += 1
        print('\nYou have given the correct answer')
    else:
        print('\nWrong Answer, the correct answer is Two')
 
 
    answer=input('\n\t2: Which is called blue mountains? \t')
    if answer.lower()=='nilgiri':
        score += 1
        print('\nYou have given the correct answer')
    else:
        print('\nWrong Answer, the correct answer is Nilgiri')
 
    answer=input('\n\t3: Which is the largest Island? \t')
    if answer.lower()=='greenland':
        score += 1
        print('\nYou have given the correct answer')
    else:
        print('\nWrong Answer, the correct answer is GreenLand')
 
print(f'\nThankyou for playing this game with us. Out of 3 you have answered {score} correctly')
mark=(score/total_questions)*100
print('\nTotal Marks obtained:',mark)
print('\nHope to meet you soon in someother game')