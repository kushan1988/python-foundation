from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List
import pandas as pd
import io

app = FastAPI()

class Student(BaseModel):
    name: str
    marks: List[int]

students_db = []

@app.get("/")
def test():
    return{"message": "Data Uploader App"}

@app.post("/students/add")
def add_student(student: Student):
    students_db.append(student)
    return{"message": "Student added successfully", "student": student}

@app.post("/students/upload")
async def upload_csv(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

    df.columns = df.columns.str.strip().str.lower()

    required_columns = {"name","math","science","english"}
    if not required_columns.issubset(df.columns):
        raise HTTPException(status_code=400,detail="Invalid CSV format")
    
    for index,row in df.iterrows():
        student = Student(
            name = row["name"],
            marks = row[["math","science","english"]].to_list()
        )
        students_db.append(student)
    return{
        "message": "Student uploaded successfully",
        "total_students": len(students_db)
    }

@app.get("/students/{student_name}/analysis")
def analyze_student(student_name: str):
    for student in students_db:
        if student.name == student_name:
            total_marks = sum(student.marks)
            average = total_marks/len(student.marks)
            if average >= 90:
                grade = "A"
            elif average >= 75:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "D"
            return{
                "name": student.name,
                "total_marks": total_marks,
                "average": average,
                "grade": grade
            }
        return{
            "Error": "Student not found!"
        }

@app.get("/students",response_model=List[Student])
def get_students():
    return students_db