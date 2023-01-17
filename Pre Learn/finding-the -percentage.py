if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks.keys():
        if i == query_name:
            sum = 0
            for j in student_marks[i]:
                sum += j
            print(format(sum/3.0, '.2f'))
