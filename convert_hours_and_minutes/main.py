def hoursMinutes(minutes):
    hours = int(minutes/60)
    mins = minutes % 60
    return f"{hours} hours and {mins} minutes"

print(hoursMinutes(125)) # => '2 hours and 5 minutes'
print(hoursMinutes(75)) # => '1 hours and 15 minutes'
print(hoursMinutes(55)) # => '0 hours and 1 minutes'
print(hoursMinutes(121)) # => '2 hours and 1 minutes'