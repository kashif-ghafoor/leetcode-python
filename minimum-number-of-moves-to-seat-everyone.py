seats = [2, 2, 6, 6]
students = [1, 3, 2, 6]

seats.sort()
students.sort()
number = 0
for seat, student in zip(seats, students):
    number += abs(seat-student)

print(number)
