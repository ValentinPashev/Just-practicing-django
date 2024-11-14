import re
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

regex_pattern = r'^[a-zA-Z0-9_]+$'

@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message_validation(self):
        return self.message

    @message_validation.setter
    def message_validation(self, value):
        if value is None:
            self.message = "Ensure this value contains only letters, numbers, and underscore."
        else:
            self.message = value

    def __call__(self, value):
        if not re.match(regex_pattern, value):
           raise ValidationError(self.message)