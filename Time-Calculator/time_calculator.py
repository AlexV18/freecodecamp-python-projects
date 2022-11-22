def add_time(start, duration, day="0"):
    weekdays = [
        "Monday", "Tuesday", "Wednesday", "Thursday", 'Friday', "Saturday",
        "Sunday"
    ]
    weekdays_lowered = [
        "monday", "tuesday", "wednesday", "thursday", 'friday', "saturday",
        "sunday"
    ]
    # storage variables:
    final_hour = 0
    final_minute = 0
    days_ahead = 0
    extra_days = False

    # split the start to get the time and the am/pm designation
    hour_min = start.split()[0].split(":")
    am_pm = start.split()[1]
    #split the duration:
    hour_min_dur = duration.split()[0].split(":")

    if int(hour_min_dur[0]) == 24 and int(hour_min_dur[1]) == 0 and day == "0":
        return start + " (next day)"
    elif int(hour_min_dur[0]) == 24 and int(hour_min_dur[1]) == 0:
        return start + ", " + weekdays[weekdays_lowered.index(day.lower()) +
                                       1] + " (next day)"

    # add the times together
    #===========================================================================
    # checks if minutes pass 60:
    if int(hour_min[1]) + int(hour_min_dur[1]) > 60:
        final_hour += 1
        final_minute = (int(hour_min[1]) + int(hour_min_dur[1])) % 60
    else:
        final_minute = (int(hour_min[1]) + int(hour_min_dur[1]))

    # this checks if the hour passes 12:
    if int(hour_min[0]) + int(hour_min_dur[0]) > 12:
        final_hour += (int(hour_min[0]) + int(hour_min_dur[0])) % 12
        # switches the am/pm
        if am_pm == "PM":
            days_ahead += 1
            am_pm = "AM"
            extra_days = True
        else:
            am_pm = "PM"
    else:
        final_hour += (int(hour_min[0]) + int(hour_min_dur[0]))
        if final_hour == 12:
            if am_pm == "PM":
                days_ahead += 1
                am_pm = "AM"
                extra_days = True
            else:
                am_pm = "PM"

    #===========================================================================

    # formatting:
    if len(str(final_minute)) == 1:
        final_minute = "0" + str(final_minute)
    #===========================================================================
    # if there are extra days, do the following, depending on how many days there are and if you have an actual starting weekday
    if extra_days:
        days_ahead += (int(hour_min[0]) + int(hour_min_dur[0])) // 24
        if days_ahead == 1:
            if day == "0":
                return str(final_hour) + ":" + str(
                    final_minute) + " " + am_pm + " (next day)"
        elif day == "0":
            return str(final_hour) + ":" + str(
                final_minute) + " " + am_pm + " (" + str(
                    days_ahead) + " days later)"
        else:
            return str(final_hour) + ":" + str(
                final_minute) + " " + am_pm + ", " + weekdays[
                    (days_ahead + weekdays_lowered.index(day.lower())) %
                    7] + " (" + str(days_ahead) + " days later)"

    if day == "0":
        return str(final_hour) + ":" + str(final_minute) + " " + am_pm
    else:
        return str(final_hour) + ":" + str(
            final_minute) + " " + am_pm + ", " + day
