from datetime import datetime as dtdt, timedelta as td, timezone as tz

tz1 = tz(td(hours=2), "UTC+2")

print("Time zone UA:", tz1)  # UTC+2
print("Type of time zone", type(tz1))  # datetime.timezone
dt1 = dtdt(1998, 2, 10, 9, 45, tzinfo=tz1)
print("Datetime with timezone:", dt1)
print("Type datetime with timezone:", type(dt1))  # datetime.timezone
print(dt1.isoformat())  # datetime.timezone in ISO 8601
print(dtdt.today())  # .todday can't work with timezone
print(dtdt.now(tz1))  # but .now can work with timezone
