from flask import jsonify
import face_recognition
import numpy as np
from models import Attendence, Room, Employee
from database.db import db
from geopy.distance import geodesic

def check_distance(data) :
    employee = Employee.query.filter_by(employee_id = data['employee_id']).first();
    room = Room.query.filter_by(room_id = employee.room_id).first()

    predefined_location = (room.latitude, room.longitude)
    current_location = (data['latitude'], data['longitude'])

    distance = geodesic(predefined_location, current_location).meters

    if distance > room.radius:
        return jsonify({ "message": "Out of range" }), 400
    
    return jsonify({ "message": distance }), 200

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
