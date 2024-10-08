from flask import Blueprint, request, jsonify
from services.attendance_service import check_distance, attendance

attendance_bp = Blueprint('attendance_bp', __name__)

@attendance_bp.route('/attendance', methods=['POST'])
def attendance_route():
    data = request.get_json()

    required_params = ['attendance_id', 'employee_id', 'attendance_date', 'check_in', 'latitude', 'longitude', 'photo_attendance']
    
    try:
        # if not all(param in data and data[param] is not None for param in required_params):
            # return jsonify({"message": "Missing data"}), 400
        
        new_attendance = attendance(data)
        return new_attendance
        return jsonify({ "message": "Attendance success", "attendance": new_attendance.check_in}), 200
    except Exception as e:
        return jsonify({ "error": str(e) }), 400
