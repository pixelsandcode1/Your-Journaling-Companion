import time

class TimeManager:

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
    
""" @staticmethod
    def journaling_window():
        True if the current time is between 7 - 10AM or 7 - 10PM"""