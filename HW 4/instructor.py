from member import Member

class Instructor(Member):

    def __init__(self, full_name: str, bio: str) -> None:
        """Creates a new instructor for the workshop

        Args:
            full_name (str): FUll name of the instructor
            bio (str): Instructor's bio
        """
        super().__init__(full_name)
        self.bio = bio
        self.skills = []

    def add_skill(self, skill: str):
        """Add a skill to the instructor

        Args:
            skill (str): skill to add
        """
        self.skills.append(skill)
