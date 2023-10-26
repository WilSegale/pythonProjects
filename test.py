from datetime import datetime, timedelta

def get_current_time():
    return datetime.now().time()

def add_time(clock_time, hours, minutes):
    time_obj = datetime.strptime(clock_time, "%H:%M")
    
    time_delta = timedelta(hours=hours, minutes=minutes)
    
    new_time = (time_obj + time_delta).time()
    
    return new_time

def subtract_time(clock_time, hours, minutes):
    time_obj = datetime.strptime(clock_time, "%H:%M")
    
    time_delta = timedelta(hours=hours, minutes=minutes)

    new_time = (time_obj - time_delta).time()
    
    return new_time