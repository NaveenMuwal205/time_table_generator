from pydantic import BaseModel
from typing import List

class Subjects(BaseModel):
    subject_code: str
    subject_name: str
    no_of_hrs_per_week: int
    is_lab: bool = False

class Semesters(BaseModel):
    semesters: str
    subjects: List[Subjects]

class Courses(BaseModel):
    course_name: str
    specs: str
    semesters: List[Semesters]
