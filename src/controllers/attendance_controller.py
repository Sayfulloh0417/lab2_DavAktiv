from src.models.attendance_log import AttendanceLog


class AttendanceController:
    """Tashqi so'rovni qabul qilib, servisga uzatadi."""

    def __init__(self, service):
        self.service = service

    def mark(self, employee_id, direction):
        return self.service.register(AttendanceLog(employee_id, direction))

    def summary(self):
        return {"came": self.service.count_came()}
