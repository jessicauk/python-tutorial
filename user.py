from role import Role


class User:
    """Class for managing user data."""

    _last_id = 0
    name = ""
    email = ""
    _password_hash = ""

    def __init__(self, name: str, email: str, role_name: str) -> None:
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            email (str): The email of the user.
            role_name (str): The role name of the user.
        """
        self._user_id = self.__class__._last_id
        self.name = name
        self.email = email
        self.role = Role(role_name)

    def set_name(self, name: str):
        """
        Set the name of the user.

        Args:
            name (str): The name of the user.
        """
        self.name = name

    def get_name(self) -> str:
        """
        Get the name of the user.

        Returns:
            str: The name of the user.
        """
        return self.name

    def set_email(self, email: str):
        """
        Set the email of the user.

        Args:
            email (str): The email of the user.
        """
        self.email = email

    def get_email(self) -> str:
        return self.email

    def set_role(self, role_name: str):
        self.role = Role(role_name)

    def get_role(self) -> Role:
        return self.role


user_1 = User("jessica", "jessica_0691@mail.com", "Student")

print(user_1.name)
print(user_1.email)
print(user_1.role.role_name)