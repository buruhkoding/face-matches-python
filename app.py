from flask import Flask, request, jsonify
from config import Config
from database.db import db
from routes.attendance_route import attendance_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(attendance_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
