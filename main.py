
import psutil
from time import sleep, strftime

time = strftime("%H:%M:%S")

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
    print(f"Successful Cpu Test {time}")

def memory(value, para, p):
    memoryList = list()

    while len(memoryList) != 10:
        sleep(1)
        memory = (psutil.swap_memory(), psutil.virtual_memory())
        memoryList.append(memory)
        if p:
            print(memory[value], end=' ')
        else:
            print(memory[value][para], end=' ')
        print(len(memoryList))
    print(f" Successful Memory Test {time}")

def selecor():
    NumberSelector = ""

    while NumberSelector != 000:
        NumberSelector = int(input("0 to Cpu List\n1 to Memory List: "))
        responseCpu = "0 to Cpu Stats %\n1 to Cpu Feq\n2 to Cpu Count:\n "
        responseMemory = "0 to Swap Memory\n1 to Virtual Memory: "
        CpuStats = "Your Selected Cpu %\n"
        CpuFreq = "Your Selected Cpu Freq\n"
        CpuCount = "Your Selected Cpu Count\n"

        MemorySwap = "Your Selected Memory Swap\n"
        MemoryUsed = "Your Selected Memory Used\n"
        MemoryFree = "Your Selected Memory Free\n"
        MemoryPercent = "Your Selected Memory Percent\n"
        MemorySin = "Your Selected Memory Sin\n"
        MemorySout = "Your Selected Memory Sout\n"
        MemoryTotal = "Yout Selected Memory Total\n"
        Memory = [MemorySout, MemorySin, MemoryPercent, MemoryFree, MemoryUsed, MemorySwap]

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
            stats = int(input("Input Stats: "))
            if stats == 0:
                swapMemory = int(input("Select\n0 to MemoryTotal\n1 to MemoryUsed\n2 to MemoryFree\n3 to MemoryPercent\n4 to MemorySin\n5 to MemorySout: "))
                if swapMemory == 0 or swapMemory == 1 or swapMemory == 2 or swapMemory == 3 or swapMemory == 4 or swapMemory == 5:
                    memory(stats, swapMemory, False)
            if stats == 1:
                virtualMemory = int(input("Select\n0 to MemoryTotal\n1 to MemoryAvailable\n2 to MemoryPercent\n3 to MemorUsed\n4 to MemoryFree: "))
                if virtualMemory == 0 or virtualMemory == 1 or virtualMemory == 2 or virtualMemory == 3 or virtualMemory == 4:
                    memory(stats, virtualMemory, False)
                if virtualMemory == 5:
                    memory(stats, virtualMemory, False)
                else:
                    print(error)

        else:
            print(error)

if True:
    selecor()