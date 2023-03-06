from os import stat

import psutil
from time import sleep


def cpu(value, para, p):
    cpulist = list()
    while len(cpulist) != 10:
        sleep(1)
        cpu = (psutil.cpu_percent(), psutil.cpu_freq(), psutil.cpu_count())
        cpulist.append(cpu[value])
        if p:
            print(cpu[value], end=' ')
        else:
            print(cpu[value][para], end=' ')
        print(len(cpulist))
    print(f" Média do {cpu[0]} é {cpulist.pop()}")

def memory(value, para, p):
    memoryList = list()
    for c in range(0, len(memoryList)) != 10:
        sleep(1)
        memory = (psutil.swap_memory(), psutil.virtual_memory())
        memoryList.append(memory)
        if p:
            print(memory[value], end=' ')
        else:
            print(memory[value][para], end=' ')
        print(len(memoryList))
    print(f" Média do {memoryList[f'{stat}']} é {memoryList.pop()}")

def selecor():
    NumberSelector = ""
    while NumberSelector != 000:
        NumberSelector = int(input("0 to Cpu List\n1 to Memory List: "))
        responseCpu = "0 to Cpu Stats %\n1 to Cpu Feq\n2 to Cpu Count:\n "
        responseMemory = "0 to Swap Memory\n1 to Virtual Memory: "
        CpuStats = "Your Selected Cpu %\n"
        CpuFreq = "Your Selected Cpu Freq\n"
        CpuCount = "Your Selected Cpu Count\n"
        error = 'Error Select Number Ivalid'
        #Select CPU >>>>>>>>>>>>>>>>>>>>

        if NumberSelector == 0:
            print(responseCpu)
            stats = int(input("Input Stats: "))
            #CPU %
            if stats == 0:
                print(CpuStats)
                cpu(stats, 0, True)

            #CPU FREQ
            if stats == 1:
                print(CpuFreq)

                cpufreqoption = int(input("Select\n0 to CurrentCpuFreq\n1 to CpuMinFreq\n2 to CpuMaxFreq: "))
                if cpufreqoption == 0 or cpufreqoption == 1 or cpufreqoption == 2:
                    cpu(stats, cpufreqoption, False)
                else:
                    print(error)

            #CPU COUNT
            if stats == 2:
                print(CpuCount)
                cpu(stats, 0, True)
            else:
                print(error)

        #SELECET MEMORY >>>>>>>>>>>>>>>>>>>>>>>
        if NumberSelector == 1:
            print(responseMemory)
        else:
            print(error)

if True:
    selecor()