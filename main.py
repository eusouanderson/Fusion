import psutil
from time import sleep


def cpu(value=0):

    ''' Função retorna porcentagem cpu , frequencia e count '''
    cpulist = list()
    while len(cpulist) != 10:
        sleep(1)
        cpu = (psutil.cpu_percent(), psutil.cpu_freq(), psutil.cpu_count())
        cpulist.append(cpu[value])
        print(cpu[value], end=' ')
        print(len(cpulist))

def memory(value=0):
    memoryList = list()
    while len(memoryList) != 10:
        sleep(1)
        memory = (psutil.swap_memory(), psutil.virtual_memory())
        memoryList.append(memory)
        print(memory[value], end=' ')
        print(len(memoryList))
def selecor():
    while True:
        NumberSelector = int(input("Input Number: "))
        stats = int(input("Input Stats: "))
        if NumberSelector == 1:
            cpu(stats)
            if stats == 1:
                ...
        if NumberSelector == 2:
            memory(stats)
        else:
            print("Number Select Error")
if True:
    selecor()