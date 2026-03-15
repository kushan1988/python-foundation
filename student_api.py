from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Student Analyzer API"}

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

@app.post("/process-data")
async def process_data(student_data: dict):
    if not student_data:
        raise HTTPException(status_code=400, detail="No data provided")
    highest_total = 0
    top_performers = []
    student_totals = {}
    results = {}
    for student, subjects in student_data.items():
        total_marks = 0
        for score in subjects.values():
            total_marks = total_score(total_marks,score)
        student_totals[student] = total_marks
        avg = average_score(total_marks,len(subjects))
        grade = assign_grade(avg)
        results[student] = {
            "total": total_marks,
            "average": round(avg,2),
            "grade": grade
        }
        highest_total, top_performers = update_top_performers(total_marks,student,highest_total,top_performers)
    ranking = generate_ranking(student_totals)
    math_top_performer, science_top_performer, english_top_performer = subject_toppers(student_data) 
    return {
        "summary": results,
        "totals": student_totals,
        "top_performers": top_performers,
        "rankings": ranking,
        "subject_toppers": {
            "Math": math_top_performer,
            "Science": science_top_performer,
            "English": english_top_performer
        }
    }

def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

def subject_toppers(student_data):
    math_highest = float('-inf')
    math_top_performer =  []
    science_highest = float('-inf')
    science_top_performer = []
    english_highest = float('-inf')
    english_top_performer = []
    for student,marks in student_data.items():
        score = marks.get("Math",0)
        if score > math_highest:
            math_highest = score
            math_top_performer = [student]
        elif score == math_highest:
            math_top_performer.append(student)
        score = marks.get("Science",0)
        if score > science_highest:
            science_highest = score
            science_top_performer = [student]
        elif score == science_highest:
            science_top_performer.append(student)
        score = marks.get("English",0)
        if score > english_highest:
            english_highest = score
            english_top_performer = [student]
        elif score == english_highest:
            english_top_performer.append(student)
    return math_top_performer,science_top_performer,english_top_performer

def generate_ranking(student_totals):
    sorted_students = sorted(student_totals.items(), key = lambda x: x[1], reverse = True)
    rankings = []
    rank = 0
    prev_score = None
    for i, (student,score) in enumerate(sorted_students):
        if score != prev_score:
            rank = i+1
        rankings.append({
            "rank": rank,
            "student": student,
            "score": score
        })
        prev_score = score
    return rankings