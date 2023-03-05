import psutil
from time import sleep


def cpu(value=0):
    cpulist = list()
    while len(cpulist) != 10:
        sleep(1)
        cpu = (psutil.cpu_percent(), psutil.cpu_freq(), psutil.cpu_count())
        cpulist.append(cpu[value])
        print(cpu[value][value], end=' ')
        print(len(cpulist))
    print(f" Média do {cpu[0]} é {cpulist.pop()}")

def memory(value=0):
    memoryList = list()
    while len(memoryList) != 10:
        sleep(1)
        memory = (psutil.swap_memory(), psutil.virtual_memory())
        memoryList.append(memory)
        print(memory[value][value], end=' ')
        print(len(memoryList))
    print(f" Média do {memory[0][0]} é {memoryList.pop()}")
def selecor():

    while True:
        NumberSelector = int(input("0 to Cpu List\n1 to Memory List: "))
        responseCpu = "0 to Cpu Stats %\n1 to Cpu Feq\n2 to Cpu Count:\n "
        responseMemory = "0 to Swap Memory\n1 to Virtual Memory: "
        if NumberSelector == 0:
            print(responseCpu)
        if NumberSelector == 1:
            print(responseMemory)
        stats = int(input("Input Stats: "))
        if NumberSelector == 0:
            cpu(stats)
        if NumberSelector == 1:
            memory(stats)

if True:
    selecor()