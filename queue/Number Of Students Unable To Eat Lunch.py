# The school cafeteria offers circular and square sandwiches at lunch break,
# referred to by numbers 0 and 1 respectively. All students stand in a queue.
# Each student either prefers square or circular sandwiches.



# The number of sandwiches in the cafeteria is equal to the number of students.
# The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of
# the stack, they will take it and leave the queue.

# Otherwise, they will leave it and go to the queue's end.

# This continues until none of the queue students want to take the top
# sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

from typing import Dict,List

def countStudents(students: List[int], sandwiches: List[int]) -> int:
    # count number of student preferences
    map:Dict[int,int] = { 0:0, 1:0 }
    # count total num of students
    num_of_students = 0
    for i in students:
        if i == 0:
            map[0] += 1
        else:
            map[1] += 1
        num_of_students += 1


    # loop left -> right checking if there is a student willing to take sandwich
    for i in sandwiches:
        if i == 0:
            # decrement counts if there is a student
            if map[0] > 0:
                map[0] -= 1
                num_of_students -= 1
            # no matching student left - dead end, break loop
            else:
                break

        else:
            if map[1] > 0:
                map[1] -= 1
                num_of_students -= 1
            else:
                break

    # return num of un-feed students
    return num_of_students


students=[1,1,0,0]
sandwiches = [0,1,0,1]
countStudents(students,sandwiches)
