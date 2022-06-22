def alarm_clock(day, vacation):
  if (day in (0, 6) and vacation):
    return 'off'
  elif (day in (0, 6) and not vacation) or (day in range(1, 6) and vacation) :
    return '10:00'
  else:
    return '7:00'
