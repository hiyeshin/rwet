import time
from time import clock
from datetime import datetime
from time import sleep
import random

log = open("log.txt", "w")

while i in range(5):
	now = str(datetime.now())
	data = random.randint(0,1024)
	log.write(now + " " + str(data) + "\n")
	print(".")
	sleep(.9)

log.flush()
log.close()


