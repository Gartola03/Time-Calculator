def add_time(start, duration, *args):
    sta = start.split(":")
    dur = duration.split(":")
    period = sta[1].split(" ")
    sta1 = int(sta[0])
    sta2 = int(period[0])
    dur1 = int(dur[0])
    dur2 = int(dur[1])
    pe = period[1]
    week = ["Monday", "tuesday", "Wednesday", "thursday", "Friday", "saturDay", "Sunday"]
    days = 0

    minutes = sta2 + dur2
    if minutes >= 60:
        minutes-=60
        sta1+=1
        
    if minutes <10:
        minutesStr = "0"+ str(minutes)
    else:
        minutesStr = str(minutes)

    hours = sta1 + dur1
    
    if hours == 12 and pe == "AM":
        pe = "PM"
    elif sta1 == 12 and pe == "PM":
        pe = "AM"
        days+=1 
    
    while (hours > 12):
        hours-=12
        if pe == "AM":
            pe = "PM"
        else:
            pe = "AM"
            days +=1
    

    result = str(hours) + ":" + minutesStr + " " + pe
    if args:
        day = str(args).replace("(","")
        day = day.replace(")", "")
        day = day.replace("'", "")
        day = day.replace(",", "")
        pos = week.index(day)
        dayP = days + pos
        pos = dayP % 7
        day = week[pos]
        result += ", "+ day

    if days == 1:
        result+= " (next day)"
    elif days > 1:
        result+=" ("+ str(days) + " days later)"; 
    
    return result



