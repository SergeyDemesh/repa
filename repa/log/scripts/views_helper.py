import datetime


def get_current_weak(day_offset):
    weak = []
    day = datetime.date.today() + datetime.timedelta(days=day_offset)
    start_weak_day = day - datetime.timedelta(days=day.weekday())
    for i in range(7):
        weak.append(start_weak_day + datetime.timedelta(days=i))
    return weak

