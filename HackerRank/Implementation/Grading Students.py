import os
import sys


def gradingStudents(grades):
    arr=[]
    def round(n):
        if n <38:
            return n
        else:
            r=n%5
            if r>2:
                return (n+5-r)
            return n
    for i in grades:
        arr.append(round(i))
    return arr

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
