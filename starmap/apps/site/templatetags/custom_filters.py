from django import template

register = template.Library()

@register.filter(name='filter_month')
def replace_spaces(date_value):
    """Take memory force value dictionary and return current object value"""
    date_value = date_value.split(" ")[0]
    month = date_value.split("-")[1].lstrip('0')
    month_list = ['test', 'January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October','November', 'December']
    month_val = month_list[int(month)]
    return month_val


@register.filter(name='filter_day')
def replace_spaces(date_value):
    """Take memory force value dictionary and return current object value"""
    date_value = date_value.split(" ")[0]
    return date_value.split("-")[2].lstrip('0')


@register.filter(name='filter_year')
def replace_spaces(date_value):
    """Take memory force value dictionary and return current object value"""
    date_value = date_value.split(" ")[0]
    return date_value.split("-")[0]

@register.filter(name='filter_address')
def filter_address(address_val):
    """Take memory force value dictionary and return current object value"""
    return address_val.split(",")[0]+","+address_val.split(",")[1]

@register.filter(name='filter_country')
def filter_address(address_val):
    """Take memory force value dictionary and return current object value"""
    return address_val.split(",")[-1]