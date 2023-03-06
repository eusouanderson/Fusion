import psutil


# % = 1
# Cpu Freq = 2
# Cpu Count = 1
'''cpu = (psutil.cpu_percent(), psutil.cpu_freq(), psutil.cpu_count())
print(cpu[1])
print('~'* 30)
'''

#Memory Swap = 5
#Memory Virtual = 4

memory = (psutil.swap_memory(), psutil.virtual_memory())
'''print(memory)'''
print(memory[1])


