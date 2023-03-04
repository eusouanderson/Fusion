import psutil
from time import sleep


cpu = (psutil.cpu_percent(), psutil.cpu_freq(), psutil.cpu_count())
print(len(cpu))