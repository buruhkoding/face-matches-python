from database.db import db

class Attendence(db.Model):
    __tablename__ = 'attendance'

    attendance_id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.employee_id'), nullable=False)
    attendance_date = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    check_in = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    check_out = db.Column(db.DateTime, nullable=True)
    latitude = db.Column(db.String(20), nullable=False)
    longitude = db.Column(db.String(20), nullable=False)
    photo_attendance = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Employee(db.Model):
    __tablename__ = 'employees'

    employee_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15))
    hire_date = db.Column(db.Date, nullable=False)
    job_title = db.Column(db.String(50))
    department_id = db.Column(db.Integer)
    profile_photo = db.Column(db.String(50))
    photo_attendance_1 = db.Column(db.String(50), nullable=False)
    photo_attendance_2 = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
