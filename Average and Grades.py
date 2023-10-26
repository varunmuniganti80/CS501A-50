# CS175
# varun sri ram muniganti
#averageAndGrade

def getScore1():
    score1 = float(input('Enter score 1: '))
    return score1
def getScore2():
    score2 = float(input('Enter score 2: '))
    return score2
def getScore3():
    score3 = float(input('Enter score 3: '))
    return score3
def getScore4():
    score4 = float(input('Enter score 4: '))
    return score4
def getScore5():
    score5 = float(input('Enter score 5: '))
    return score5

def calcAverage(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    avg = total / 5
    return avg

def determineGrade(findAvg):
    if findAvg >= 90 and findAvg <= 100:
        grade = 'A'
        return grade
    elif findAvg >= 80 and findAvg <= 89:
        grade = 'B'
        return grade
    elif findAvg >= 70 and findAvg <= 79:
        grade = 'C'
        return grade
    elif findAvg >= 60 and findAvg <= 69:
        grade = 'D'
        return grade
    else:
        grade = 'F'
        return grade
        
def main():
    score1 = 0.0
    score2 = 0.0
    score3 = 0.0
    score4 = 0.0
    score5 = 0.0
    avg = 0.0

    score1 = getScore1()
    score2 = getScore2()
    score3 = getScore3()
    score4 = getScore4()
    score5 = getScore5()

    findAvg = calcAverage(score1, score2, score3, score4, score5)
    letterGrade = determineGrade(findAvg)

    print('Score Numeric Grade Letter Grade')
    print('------------------------------------------------')
    print('Score 1:', score1, '\t', determineGrade(score1))
    print('Score 2:', score2, '\t', determineGrade(score2))
    print('Score 3:', score3, '\t', determineGrade(score3))
    print('Score 4:', score4, '\t', determineGrade(score4))
    print('Score 5:', score5, '\t', determineGrade(score5))

    print('Final Average:', findAvg,',',letterGrade)
    
    repeat=str(input('Enter yes if you would like to do another calculation'))
    while repeat=='yes':
        getScore1()
        getScore2()
        getScore3()
        getScore4()
        getScore5()
        calcAverage(score1, score2, score3, score4, score5)
        determineGrade(findAvg)
        print('Score Numeric Grade   Letter Grade')
        print('------------------------------------------------')
        print('Score 1:', score1, '\t', determineGrade(score1))
        print('Score 2:', score2, '\t', determineGrade(score2))
        print('Score 3:', score3, '\t', determineGrade(score3))
        print('Score 4:', score4, '\t', determineGrade(score4))
        print('Score 5:', score5, '\t', determineGrade(score5))
        print('Final Average:', findAvg,',',letterGrade)
        
        repeat=str(input('Enter yes if you would like to do another calculation'))
    else:
        print('')
    
main()
