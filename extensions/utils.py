from . import jalaly
from django.utils import timezone


def jalali_convertor(time):
    
    time = timezone.localtime(time)
    
    time_to_string = "{},{},{}".format(time.year, time.month, time.day)
    time_to_tuple = jalaly.Gregorian(time_to_string).persian_tuple()
    output = "{} {} {}, ساعت {}:{}".format(
        time_to_tuple[2],
        time_to_tuple[1],
        time_to_tuple[0],
        time.hour,
        time.minute,
    )
    
    return output