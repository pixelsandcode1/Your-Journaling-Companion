#Time.py shares the time and date.
import time

class TimeManager:
    #timezone in EST is -4 whichis UTC-4 during daylight saving. 
    #This will manually change depending on time of year.
    timezone_offset_hours = -4 

    weekday = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    month = [
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    @staticmethod
    def _local_time():
        utc = time.time()
        local = utc + (TimeManager.timezone_offset_hours * 3600)

        return time.localtime(local)   

    @staticmethod
    def get_date():
        t = TimeManager._local_time()

        weekday_out = TimeManager.weekday[t[6]]
        month_out = TimeManager.month[t[1]]
        day = t[2]

        return f"{weekday_out}, {month_out} {day}"

    @staticmethod
    def get_time():
        t = TimeManager._local_time()

        hour = t[3]
        minute = t[4]

        time_period = "AM"

        if hour >= 12:
            time_period = "PM"

        hour = hour % 12

        if hour == 0:
            hour = 12

        return f"{hour}:{minute:02d} {time_period}"
    
    @staticmethod
    def journaling_window():
        hour = time.localtime()[3]

        if 7 <= hour < 10:
            return "AM"
        
        elif 19 <= hour < 22:
            return "PM"
        
        else:
            return None
