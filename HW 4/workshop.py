from member import Member
from instructor import Instructor
from student import Student

class Workshop:

    def __init__(self, date: str, subject: str) -> None:
        """Creates a new workshop

        Args:
            date (str): date of the workshop
            subject (str): subject of the workshop
        """
        self.date = date
        self.subject = subject
        self.instructors = []
        self.students = []

    def add_participant(self, participant: Member):
        """Adds a participant to the workshop

        Args:
            participant (Member): participant object

        Raises:
            ValueError: if object is not of type Member
        """
        if(isinstance(participant, Instructor)):
            self.instructors.append(participant)

        elif (isinstance(participant, Member)):
            self.students.append(participant)

        else:
            raise ValueError("Object must be of type Member")
        

    def print_details(self):
        """Prints details about the workshop
        """
        instructors = ", ".join(str(inst) for inst in self.instructors)
        students = ", ".join(str(stu) for stu in self.students)
        print(f"Workshop: {self.subject}. Date: {self.date}. Instructors: {instructors}. Students: {students}")