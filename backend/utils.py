def get_marks_input():
    marks = input("Enter marks separated by space: ")
    return list(map(int, marks.split()))