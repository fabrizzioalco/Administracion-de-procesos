from random import random
import SRTFClass as SRTF
import ganttChart as gantt
import matplotlib.pyplot as plt
from PIL import Image



# Declaring a figure "gnt"
fig, gnt = plt.subplots()

# size of the rectangles

# Setting Y-axis limits
gnt.set_ylim(0, 50)

# Setting X-axis limits
gnt.set_xlim(0, 160)

# Setting labels for x-axis and y-axis
gnt.set_xlabel('seconds since start')
gnt.set_ylabel('Processor')

# Setting ticks on y-axis
gnt.set_yticks([15, 25, 35])
# Labelling tickes of y-axis
gnt.set_yticklabels(['1', '2', '3'])

# Setting graph attribute
gnt.grid(False)

# Declaring multiple bars in at same level and same width

numberOfProcess = int(input('Ingrese el numero de procesos: '))
processesList = []

for i in range(numberOfProcess):
    arrival = int(input(f'Ingrese el tiempo de llegada de P{i + 1}:'))
    duration = int(input(f'Ingrese la duracion de P{i + 1}:'))
    process = SRTF.Process(arrival, duration)
    processesList.append(process)

sumDuration = 0
for processes in processesList:
    sumDuration += processes.duration
print(sumDuration)

# copiamos la lista en otra para mejor organizacion.
notArrivedProcesses = processesList.copy()

# lista para almacenar los procesos que ya han estado corriendo
arrrivedProcesses = []

# recorremos la lista de notArrivedProcesses.
for i in range(sumDuration):
    for processes in notArrivedProcesses:
        if processes.arrival == i:
            # processes.setColor(randomColor())
            arrrivedProcesses.append(processes)

            # When we insert in arrived processes, we need to remove it
            notArrivedProcesses.remove(processes)

    shorterTime = sumDuration
    shorterProcess = None
    for process in arrrivedProcesses:
        if process.duration < shorterTime:
            shorterTime = process.duration
            shorterProcess = process

    shorterProcess.reducedTime(1)

    if shorterTime == 0:
        arrrivedProcesses.remove(shorterProcess)

    for process in arrrivedProcesses:
        if process is shorterProcess:
            continue
        process.waitingTime(1)

def promWaitingTime():
    waitingTimeSum =  0
    for processes in processesList:
        waitingTimeSum += processes.getWaitingTime()
        print(processes.getWaitingTime())
    print('Waiting time' + str(waitingTimeSum))
    return waitingTimeSum/numberOfProcess
print(promWaitingTime())


gnt.broken_barh([(10,9), (43, 43)], (10, 9), facecolors='tab:blue')
plt.savefig("gantt1.png")

img = Image.open("gantt1.png")
img.show()