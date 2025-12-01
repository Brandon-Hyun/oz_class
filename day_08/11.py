# z_students = [
#     {"name": "백현우", "python": 4, "database": 3, "Django": 3, "AWS": 2},
#     {"name": "홍혜인", "python": 4, "database": 5, "Django": 2, "AWS": 4},
#     {"name": "윤은성", "python": 3, "database": 4, "Django": 4, "AWS": 1},
#     {"name": "홍수철", "python": 2, "database": 3, "Django": 1, "AWS": 5},
# ]
# print("이름", "총점", "평균", sep="\t")

# # oz_students 리스트의 각 학생에 대해 반복문을 실행합니다.
# for student in oz_students:
#     # 각 학생의 Python, Database, Django, AWS 능력 점수를 합산하여 총점을 계산합니다.
#     ability_sum = student["python"] + student["database"] + student["Django"] + student["AWS"]
#     # 총점을 4로 나누어 평균을 계산합니다.
#     ability_average = ability_sum / 4
    
#     # 학생의 이름, 총점, 평균을 탭(\t)으로 구분하여 출력합니다.
#     print(student["name"], ability_sum, ability_average, sep="\t")

def create_oz_students(name, python, database, django, AWS):
    return {
        "name": name,
        "python": python,
        "database": database,
        "Django": django,
        "AWS": AWS
    }

oz_students = [
    create_oz_students("백현우", 4,3,3,2),
    create_oz_students("홍혜인",4,5,2,4),
    create_oz_students("윤은성",3,4,4,1),
    create_oz_students("홍수철", 2,3,1,5)
]

print("이름  ", "총점", "평균", sep="|")

# oz_students 리스트의 각 학생에 대해 반복문을 실행합니다.
for student in oz_students:
    # 각 학생의 Python, Database, Django, AWS 능력 점수를 합산하여 총점을 계산합니다.
    ability_sum = student["python"] + student["database"] + student["Django"] + student["AWS"]
    # 총점을 4로 나누어 평균을 계산합니다.
    ability_average = ability_sum / 4
    
    # 학생의 이름, 총점, 평균을 탭(\t)으로 구분하여 출력합니다.
    print(student["name"], ability_sum, ability_average, sep="|")