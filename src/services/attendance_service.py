class AttendanceService:
    """Davomat bo'yicha biznes qoidalar."""

    def __init__(self, repository):
        self.repository = repository

    def register(self, log):
        self.repository.add(log)
        return log

    def count_came(self):
        ids = {l.employee_id for l in self.repository.all() if l.direction == "IN"}
        return len(ids)
