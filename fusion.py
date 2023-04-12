import psutil
from time import sleep, strftime

timestart = strftime("%H:%M:%S")
class color:

    HEADER = f'\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    def txt(type, txt):
        print(f"{type}{txt} {color.ENDC}", end='')
        
    def box(type, txt):
        print("~" * len(txt))
        print(f"{type}{txt} " + color.ENDC)
        print(color.OKBLUE + "Developed by Anderson" + color.ENDC)
        print("~" * len(txt))



def cpu(value, para, p):
    cpulist = list()

    while len(cpulist) != 10:
        sleep(1)
        timeEnd = strftime("%H:%M:%S")
        cont = len(cpulist)
        cpu = (psutil.cpu_percent(), psutil.cpu_freq(), psutil.cpu_count())
        cpulist.append(cpu[value])
        if p:
            color.txt(color.OKGREEN, cpu[value]), print(f"Test nº {cont}")
        else:
            color.txt(color.OKGREEN, cpu[value][para]), print(f"Test nº {cont}")
    color.box(color.HEADER, f"Successful Cpu Test Start in {timestart} End in {timeEnd}")


def memory(value, para, p):
    memoryList = list()

    while len(memoryList) != 10:
        sleep(1)
        timeEnd = strftime("%H:%M:%S")
        cont = len(memoryList)
        memory = (psutil.swap_memory(), psutil.virtual_memory())
        memoryList.append(memory)
        if p:
            color.txt(color.OKGREEN, memory[value]), print(f"Test nº {cont}")
        else:
            color.txt(color.OKGREEN, memory[value][para]), print(f"Test nº {cont}")
    color.box(color.HEADER, f"Successful Memory Test {timestart} End in {timeEnd}")


def selecor():
    NumberSelector = ""
    
    while NumberSelector != 000:
        color.box(color.HEADER, "Welcome to Fusion program")
        
        try:
            NumberSelector = int(input("0 to Cpu List\n1 to Memory List: "))

            responseCpu = "0 to Cpu Stats %\n1 to Cpu Feq\n2 to Cpu Count:\n"
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
            MemoryTotal = "Your Selected Memory Total\n"
            MemoryAvaillable = "Your Select Memory Available\n"
            
            Memory = [MemoryTotal, MemoryAvaillable, MemoryPercent, MemoryUsed, MemoryFree, MemorySout, MemorySin,
                    MemorySwap]

            # Select CPU >>>>>>>>>>>>>>>>>>>>

            if NumberSelector == 0:
                print(responseCpu)
                stats = int(input("Input Stats: "))

                # CPU %
                if stats == 0:
                    print(CpuStats)
                    cpu(stats, 0, True)

                # CPU FREQ
                if stats == 1:
                    print(CpuFreq)
                    cpufreqoption = int(input("Select\n0 to CurrentCpuFreq\n1 to CpuMinFreq\n2 to CpuMaxFreq: "))
                    if cpufreqoption == 0 or cpufreqoption == 1 and cpufreqoption == 2:
                        cpu(stats, cpufreqoption, False)
                    else:
                        print(error)

                # CPU COUNT
                if stats == 2:
                    print(CpuCount)
                    cpu(stats, 0, True)

            # SELECET MEMORY >>>>>>>>>>>>>>>>>>>>>>>
            if NumberSelector == 1:
                print(responseMemory)
                stats = int(input("Input Stats: "))
                if stats == 0:
                    swapMemory = int(input(
                        "Select\n0 to MemoryTotal\n1 to MemoryUsed\n2 to MemoryFree\n3 to MemoryPercent\n4 to "
                        "MemorySin\n5 to MemorySout: "))
                    if swapMemory == 0 or swapMemory == 1 or swapMemory == 2 or swapMemory == 3 or swapMemory == 4 \
                            or swapMemory == 5:
                        memory(stats, swapMemory, False)

                if stats == 1:
                    virtualMemory = int(input(
                        "Select\n0 to MemoryTotal\n1 to MemoryAvailable\n2 to MemoryPercent\n3 to MemorUsed\n4 to "
                        "MemoryFree: "))

                    if virtualMemory == 0 or 1 or 2 or 3 or 4:
                        if virtualMemory == 0:
                            print(Memory[0])
                        if virtualMemory == 1:
                            print(Memory[1])
                        if virtualMemory == 2:
                            print(Memory[2])
                        if virtualMemory == 3:
                            print(Memory[3])
                        if virtualMemory == 4:
                            print(Memory[4])
                        memory(stats, virtualMemory, False)

                    if virtualMemory == 5:
                        memory(stats, virtualMemory, False)
          
        except Exception as error:
            if NumberSelector != 0 or 1 or 2:
                print(f"Erro {error.__class__} Input Number Int!")
                print(error)

if True:
    selecor()
