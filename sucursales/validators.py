from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

TYPE_CHOICES = (
    ('P', 'Principal'),
    ('G', 'General'),
)

def validateNumber(value):
    if value.isdigit() == False:
        raise ValidationError(
            _('%(value)s no numerico'),
            params={'value': value},
        )