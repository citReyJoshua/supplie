# Choices for the user model

SINGLE = 'SI'
WIDOW = 'WI'
MARRIED = 'MA'
DIVORCED = 'DI'
CHOICES_STATUS = (
    (SINGLE, 'Single'),
    (WIDOW, 'Widow/er'),
    (MARRIED, 'Married'),
    (DIVORCED, 'Divorced'),
)

MALE = 'M'
FEMALE = 'F'
NOT_SPECIFIED = 'NS'

CHOICES_GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (NOT_SPECIFIED, 'Not Specified'),
)
