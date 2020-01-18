import time
"""
    Write a Stopwatch Program for measuring the time that elapses between the start and end clicks
"""


def time_convert(sec):
  
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),round(sec,2)))

try:

  input("Press Enter to start")
  start_time = time.time()
  
  input("Press Enter to stop")
  end_time = time.time()
  
  time_lapsed = end_time - start_time
  
  print(time_lapsed)
  time_convert(time_lapsed)

except ValueError:
  
  print("Error")