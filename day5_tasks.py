student_data = {
    "Ankush": {"Math": 91, "Science": 96, "English": 84},
    "Riya": {"Math": 92, "Science": 88, "English": 91},
    "Kabir": {"Math": 92, "Science": 88, "English": 92}
}
def total_score(total_marks,marks):
    return total_marks + marks

def average_score(score,subjects):
    return score/subjects if subjects else 0

def update_top_performers(total_marks,student, highest_total, top_performers):
    if total_marks > highest_total:
        highest_total = total_marks
        top_performers = [student]
    elif total_marks == highest_total:
        top_performers.append(student)
    return highest_total,top_performers

def process_data():
    if not student_data:
        print('No Data Present!')
        return
    highest_total = 0
    top_performers = []
    student_totals = {}
    for student, subjects in student_data.items():
        total_marks = 0
        for score in subjects.values():
            total_marks = total_score(total_marks,score)
        student_totals[student] = total_marks
        avg = average_score(total_marks,len(subjects))
        grade = assign_grade(avg)
        print(f"{student}: Total {total_marks}, Average {avg}, Grade {grade}")
        highest_total, top_performers = update_top_performers(total_marks,student,highest_total,top_performers)
    print("Top Performer: ", top_performers)
    math_top_performer, science_top_performer, english_top_performer = subject_toppers(student_data)  
    print(f"Toppers in Math: {math_top_performer}, Science: {science_top_performer} and English: {english_top_performer}") 
    print(f"Student's Ranking: ")
    generate_ranking(student_totals)

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg < 60:
        return "D"
    else:
        print("Invalid Data!")

def subject_toppers(student_data):
    math_highest = float('-inf')
    math_top_performer =  []
    science_highest = float('-inf')
    science_top_performer = []
    english_highest = float('-inf')
    english_top_performer = []
    for student,marks in student_data.items():
        score = marks["Math"]
        if score > math_highest:
            math_highest = score
            math_top_performer = [student]
        elif score == math_highest:
            math_top_performer.append(student)
        score = marks["Science"]
        if score > science_highest:
            science_highest = score
            science_top_performer = [student]
        elif score == science_highest:
            science_top_performer.append(student)
        score = marks["English"]
        if score > english_highest:
            english_highest = score
            english_top_performer = [student]
        elif score == english_highest:
            english_top_performer.append(student)
    return math_top_performer,science_top_performer,english_top_performer

def generate_ranking(student_totals):
    sorted_students = sorted(student_totals.items(), key = lambda x: x[1], reverse = True)
    rank = 0
    prev_score = None
    for i, (student,score) in enumerate(sorted_students):
        if score != prev_score:
            rank = i+1
        print(f"Rank {rank}: Student {student}")
        prev_score = score

def main():
    process_data()  

main()      