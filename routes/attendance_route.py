from flask import Blueprint, request, jsonify
from services.attendance_service import attendance

attendance_bp = Blueprint('attendance_bp', __name__)

@attendance_bp.route('/attendance', methods=['POST'])
def attendance_route():
    data = request.get_json()
    try:
        new_attendance = attendance(data)
        return jsonify({ "message": "Attendance success", "attendance": new_attendance.check_in}), 200
    except Exception as e:
        return jsonify({ "error": str(e) }), 400
