total_units = []
total_credits_get = []
while True:
    enter = input("Enter course number, units, and grade, separated by spaces\n")
    # ECS10 4 B-
    if enter == '':
        break
    index = enter.find(' ')
    grade_of_the_course = enter[index+1]
    total_units.append(grade_of_the_course)
    letter_grade = enter[index+3]
    if letter_grade == 'A':
        if enter[index+4] == '-':
            point_for_grade = 3.7
        else:
            point_for_grade = 4
    elif letter_grade == 'B':
        if enter[index+4] == '+':
            point_for_grade = 3.3
        elif enter[index+4] == '-':
            point_for_grade = 2.7
        else:
            point_for_grade = 3
    elif letter_grade == 'C':
        if enter[index+4] == '+':
            point_for_grade = 2.3
        elif enter[index+4] == '-':
            point_for_grade = 1.7
        else:
            point_for_grade = 2
    elif letter_grade == 'D':
        if enter[index+4] == '+':
            point_for_grade = 1.3
        elif enter[index+4] == '-':
            point_for_grade = 0.7
        else:
            point_for_grade = 1
    elif letter_grade == 'F':
        if enter[index+4] == '+':
            point_for_grade = 3.3
        else:
            point_for_grade = 0
    weighted_points = grade_of_the_course * point_for_grade
    total_credits_get.append(weighted_points)
GPA = int(sum(total_credits_get)) / int(sum(total_units))
print('The GPA is', GPA)
    
    

        
    
        
    
    
