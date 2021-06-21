"""collection of small Django utilities"""


def is_bank_employee(user) -> bool:
    """function - check if user is an employee"""
    return True if user.groups.filter(name='bank_employees') else False
