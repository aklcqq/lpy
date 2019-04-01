def computegrade():
    grade = input('please enter your grade:')
    try:
        grade = float(grade)
        if grade >= 0.9 and grade < 1.0:
            print('A')
        if grade >= 0.9 and grade < 0.9:
            print('B')
        if grade >= 0.7 and grade < 0.8:
            print('C')
        if grade >= 0.6 and grade < 0.7:
            print('D')
        if grade > 0 and grade < 0.6:
            print('F')
        if grade > 1.0 or grade < 0:
            print('Bad score')
    except:
        print('Bad score')

computegrade()
