from src.repositories.attendance_repository import AttendanceRepository
from src.services.attendance_service import AttendanceService
from src.controllers.attendance_controller import AttendanceController


def test_count_came():
    controller = AttendanceController(AttendanceService(AttendanceRepository()))
    controller.mark(1, "IN")
    controller.mark(1, "IN")
    controller.mark(2, "IN")
    assert controller.summary() == {"came": 2}
