from member import Member

class Student(Member):

    def __init__(self, full_name: str, reason: str) -> None:
        """Creates a new student for the workshop

        Args:
            full_name (str): Full name of the student
            reason (str): Reason for attendance
        """
        super().__init__(full_name)
        self.reason = reason


