student_data = {
    "Ankush": {"Math": 91, "Science": 96, "English": 84},
    "Riya": {"Math": 92, "Science": 88, "English": 91},
    "Kabir": {"Math": 92, "Science": 88, "English": 92}
}
average_marks = 0
max_count = 0
top_performer = []
#total/average Marks
if not student_data:
    print('No Data Present!')
else:
    for x, obj in student_data.items():
        total_marks = 0
        for y in obj:
            total_marks += obj[y]
        average_marks = total_marks/len(obj)
        print(f"Test Results: {x}: Total Marks {total_marks} and Average {average_marks}")
        if total_marks > max_count:
            max_count = total_marks
            top_performer.clear()
            top_performer.append(x)
        elif total_marks == max_count:
            top_performer.append(x)
    print(f"Top Performer: {top_performer}")
        