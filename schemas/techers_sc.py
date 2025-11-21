from pydantic import BaseModel
from typing import List
from schemas.courses import Subjects

class Teachers(BaseModel):
    teacher_id: str
    name: str
    qualification: str
    is_dean_hod: bool
    assigned_subjects: List[Subjects]
    no_of_subjects_per_day: int

class Department(BaseModel):
    dept_name: str
    teachers: List[Teachers]