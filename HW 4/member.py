class Member:

    def __init__(self, full_name: str) -> None:
        """Creates a new member for the workshop

        Args:
            full_name (str): Full nname of the member
        """
        self.full_name = full_name

    def introduce(self) -> str:
        """Allows the member to introduce themselves

        Returns:
            str: member's self introduction
        """
        return f"Hi, my name is {self.full_name}!"

    def __str__(self) -> str:
        """Return the member as a string

        Returns:
            str: member's full name
        """
        return self.full_name