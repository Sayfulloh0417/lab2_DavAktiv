from datetime import datetime


class AttendanceLog:
    def __init__(self, employee_id, direction, timestamp=None):
        self.employee_id = employee_id
        self.direction = direction  # "IN" yoki "OUT"
        self.timestamp = timestamp or datetime.now()
