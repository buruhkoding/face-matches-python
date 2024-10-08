from models import Attendence
from database.db import db

def attendance(data) :
    new_attendance = Attendence(
        attendance_id = data['attendance_id'],
        employee_id = data['employee_id'],
        attendance_date = data['attendance_date'],
        check_in = data['check_in'],
        check_out = data['check_out'],
        latitude = data['latitude'],
        longitude = data['longitude'],
        photo_attendance = data['photo_attendance'],
    )

    db.session.add(new_attendance)
    db.session.commit()
    return new_attendance
