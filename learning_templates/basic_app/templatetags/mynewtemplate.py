from django import tempalte

register = template.library()
@register.filter(name='cut')
def cut(value, arg):
	return value.replace(ard,'')

# register.filter('cut', cut)
