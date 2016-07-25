from django.core.validators import RegexValidator, MaxValueValidator
import re


class SubCategoryURLValidator(RegexValidator):
    regex = re.compile(
        r'^(\w*)$', re.IGNORECASE) # without slashes
    message = u"Correct format: url_name, without slashes. Where url_name can contains letters and digits"

# class MaxLevelValidator(MaxValueValidator):
#     message = _(u'Ensure this value is less than or equal to %(limit_value)s.')
#     code = 'max_level_value'