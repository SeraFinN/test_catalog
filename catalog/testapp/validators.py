from django.core.validators import RegexValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import re


class SubCategoryURLValidator(RegexValidator):
    regex = re.compile(
        r'^(\w*)$', re.IGNORECASE) # without slashes
    message = u"Correct format: url_name, without slashes. Where url_name can contains letters and digits."


class CategoryRootImageValidator(object):
    message = u'Root category must have default image.'
    code = 'root_category'

    def __init__(self): pass
        #self.category_level = category_level

    def __call__(self, value, model_instance):
        assert False, model_instance
        params = {'category_level': model_instance.level}
        if model_instance.level == 1:
            raise ValidationError(
                self.message,
                code=self.code,
                params=params,
            )

# class MaxLevelValidator(MaxValueValidator):
#     message = _(u'Ensure this value is less than or equal to %(limit_value)s.')
#     code = 'max_level_value'