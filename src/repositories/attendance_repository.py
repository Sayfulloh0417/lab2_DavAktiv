class AttendanceRepository:
    """Davomat yozuvlarini saqlash (hozircha xotirada)."""

    def __init__(self):
        self._logs = []

    def add(self, log):
        self._logs.append(log)

    def all(self):
        return list(self._logs)
