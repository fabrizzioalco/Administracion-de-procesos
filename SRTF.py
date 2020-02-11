import random
import SRTFClass as SRTF
import ganttChart as gantt
import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk, Image
matplotlib.use("TkAgg")


def generateRandomColor():
    r = random.random()
    g = random.random()
    b = random.random()
    alpha = 1.0
    rgb = (r, g, b, alpha)

    return rgb

# Declaring a figure "gnt"
fig, gnt = plt.subplots()

# size of the rectangles

# Setting Y-axis limits
gnt.set_ylim(0, 10)

# Setting X-axis limits


# Setting labels for x-axis and y-axis


gnt.set_ylabel('Processor')

# Setting ticks on y-axis
gnt.set_yticks([15])
# Labelling tickes of y-axis
gnt.set_yticklabels(['1'])

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
listaTuplas =[]

# recorremos la lista de notArrivedProcesses.
counter = 0
for i in range(sumDuration):
    for processes in notArrivedProcesses:
        if processes.arrival == i:
            processes.setColor(generateRandomColor())
            arrrivedProcesses.append(processes)
            # When we insert in arrived processes, we need to remove it
            notArrivedProcesses.remove(processes)
    counter += 1



    shorterTime = sumDuration
    shorterProcess = None
    for process in arrrivedProcesses:
        if process.duration < shorterTime:
            process.setLapsedTime(process.arrival, counter)
            print(process.getLapsedTime())
            shorterTime = process.duration
            shorterProcess = process

    shorterProcess.reducedTime(1)

    if shorterProcess.duration == 0:
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



gnt.set_xlim(0, sumDuration)
for process in processesList:
    print(process.getLapsedTime())
    gnt.broken_barh(process.getLapsedTime(), (10, 9), color=process.getColor())

def crateGUI(image):
    root = tk.Tk()
    img = ImageTk.PhotoImage(Image.open('gantt1.png'))
    img_panel = tk.Label(root, image=img)
    img_panel.grid(column=1, row=0)
    root.mainloop()




plotImage='gantt_SRTF.png'
plt.savefig("gantt_SRTF.png")
crateGUI(plotImage)

# img = Image.open("gantt1.png")
# img.show()