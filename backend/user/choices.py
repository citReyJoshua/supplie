# Choices for the user model

SINGLE = 'SI'
WIDOW = 'WI'
MARRIED = 'MA'

CHOICES_STATUS = (
    (SINGLE, 'Single'),
    (WIDOW, 'Widow/er'),
    (MARRIED, 'Married'),
)

MALE = 'M'
FEMALE = 'F'
NOT_SPECIFIED = 'NS'

CHOICES_GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (NOT_SPECIFIED, 'Not Specified'),
)
