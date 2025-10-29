# import datetime as dt  # import library/all module short word (Alias) # rarely used

# [directory] [.] is [/] [name_module] == datetime.something
# import libraries, but not all, only part of them
# Example: import numpy as np
# print(dir(dt))
# print(dt.MINYEAR, dt.MAXYEAR, dt.UTC)  # MINYEAR = 1, MAXYEAR = 1999, UTC = UTC (costants or literals)

from datetime import datetime as dtdt, timedelta as td

print("Date and time now:", dtdt.now())  # Date and time now: 2025-10-29 12:41:29.681459
print("Year now:", dtdt.now().year)  # Year now: 2025 (ISO8601)
print("Month now:", dtdt.now().month)  # Month now: 10 (ISO8601)
print("Day now:", dtdt.now().day)  # Day now: 29 (ISO8601)
print("Hour now:", dtdt.now().hour)  # Hour now: 12 (ISO8601)
print("Minute now:", dtdt.now().minute)  # Minute now: 41 (ISO8601)
print("Second now:", dtdt.now().second)  # Second now: 29 (ISO8601)
print("Microsecond now:", dtdt.now().microsecond)  # Microsecond now: 681459 (ISO8601)


# year=[1-9999], month=[1-12], day=[1-31], hour = [0-23], minute=[0-59], second=[0-59], microsecond=[0-999999]
print(dtdt(year=1998, month=2, day=28, hour=9, minute=45, second=30, microsecond=2433))
print(dtdt(1998, 2, 10, 9, 45, 30, 2433))  # 1998-02-10 09:45:30.002433

dt1 = dtdt(1998, 2, 10, 9, 45, 13)
dt2 = dtdt(2025, 10, 29, 13, 15, 13)
print("Difference dt2 - dt1: ", dt2 - dt1)
print("Type dt1:", type(dt1))  # type datetime.datetime -> date and time
print(
    "Type difference dt2 - dt1: ", type(dt2 - dt1)
)  # type datetime.timedelta -> date and time difference default in day
td1 = td(days=3650)
print("td:", td1)  # date and time difference
print("Type td:", type(td))  # type
print("dt2 + td1:", dt2 + td1)  # dt2 + td1

now = dtdt.now()
print("Date and time now:", dtdt.now())  # Date and time now: 2025-10-29 12:41:29.681459
ts1 = dtdt.timestamp(now)  # method(class) seconds to now from 01.01.01
print("timestamp:", ts1)  # print timestamp
print(dtdt.fromtimestamp(ts1))  # 2025-10-29 13:47:54.021636

print(
    dtdt.strftime(now, "%d/%m/%Y, /yes, _%m %H:%M:%S")
)  # change ISO to other format(string format time) 29/10/2025, /yes, _10 13:58:47
print(
    dtdt.strftime(now, "%d/%b/%y, %a, _%m %I:%M:%S %p")
)  # change ISO to other format(string format time) 29/Oct/25, Wed, _10 02:01:55 PM
udow = {
    0: "Понеділок",
    1: "Вівторок",
    2: "Середа",
    3: "Четвер",
    4: "П'ятниця",
    5: "Субота",
    6: "Неділя",
}
print(dtdt.strftime(now, f"%d/%m/%Y, {udow[now.weekday()]}, %H:%M:%S"))
# Ukrainian weekday from dictionary udow (ukr day of week)
print(
    dtdt.strptime(
        "29/10/2025, Середа, 14:21:59", f"%d/%m/%Y, {udow[now.weekday()]}, %H:%M:%S"
    )
)  # string format to ISO(object type datetime.datetime), need all correct symbols(will be Error if not correct) -> 2025-10-29 14:21:59
print(now.isoformat())  # 2025-10-29T14:36:34.006954 ISO 8601
print(type(now.isoformat()))  # format string
print(dtdt.fromisoformat("2025-10-29T14:36:34.006954"))  # 2025-10-29 14:36:34.006954
print(
    type(dtdt.fromisoformat("2025-10-29T14:36:34.006954"))
)  # format datetime.datetime
