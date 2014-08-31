import time

while True:
  try:
    time.sleep(1)
    print "a"
  except KeyboardInterrupt:
    print "ctrl+c"
