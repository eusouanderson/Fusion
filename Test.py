import psutil
from time import sleep
from main import cpu


cpu = (psutil.cpu_percent(), psutil.cpu_freq(), psutil.cpu_count())
print(cpu)

cpu()