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
    for student, subjects in student_data.items():
        total_marks = 0
        for subject in subjects:
            total_marks = total_score(total_marks,subjects[subject])
        avg = average_score(total_marks,len(subjects))
        print(f"{student}: Total {total_marks}, Average {avg}")
        highest_total, top_performers = update_top_performers(total_marks,student,highest_total,top_performers)
    print("Top Performer: ", top_performers)

def main():
    process_data()  

main()      