from django.contrib.auth.models import Group


def is_bank_employee(user) -> bool:
    return True if user.groups.filter(name='bank_employees') else False
