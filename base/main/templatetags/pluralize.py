from django import template

register = template.Library()

@register.filter
def rupluralize_2(value, arg="задача,задачи,задач"):
    args = arg.split(",")
    number = abs(int(value))
    a = number % 10
    b = number % 100

    if (a == 1) and (b != 11):
        return args[0]
    elif (a >= 2) and (a <= 4) and ((b < 10) or (b >= 20)):
        return args[1]
    else:
        return args[2]

@register.filter
def rupluralize_1(value, arg="осталась, остались, осталось"):
    args = arg.split(",")
    number = abs(int(value))

    if (number == 1):
        return args[0]
    elif (number >= 2):
        return args[1]
    elif (number == 0):
        return args[2]