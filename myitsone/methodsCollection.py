from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create username validation
def isValidUsername(value):
        if ' ' in value:
            raise ValidationError(
                _("%(value)s contains spacing"),
                params={"value": value},
            )
