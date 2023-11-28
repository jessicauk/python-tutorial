class Role:
    """Class for managing role data."""

    _last_id = 0

    def __init__(self, role_name) -> None:
        self.role_name = role_name
        self._role_id = self.__class__._last_id

    def get_role_name(self) -> str:
        """Returns the role name."""
        return self.role_name

    def set_role_name(self, role_name: str):
        """Sets the role name."""
        self.role_name = role_name
