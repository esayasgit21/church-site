
from django.forms import ValidationError


def file_size(value): # add this to some file where you can import it from
    limit = 1048576
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 1 MiB.')
    else:
        return value