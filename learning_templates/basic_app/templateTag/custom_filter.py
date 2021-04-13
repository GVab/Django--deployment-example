from django import templates


register=template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    remove str or arg from value str
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
