class Process:
    number = 1

    # constructor sirve para definir las partes que tu cosa tendra (caracteristicas)
    def __init__(self, arrival, duration):
        self.arrival = arrival
        self.duration = duration
        self.waiting = 0
        self.numeroProceso = Process.number
        self.color = None
        Process.number += 1

    def getArrival(self):
        return self.arrival

    def getDuration(self):
        return self.duration

    # cuando usamos setter no retornamos nada , ya que lo que cambiamos es la estructura que esta en memoria.
    def reducedTime(self, time):
        self.duration -= time

    def waitingTime(self, time):
        self.waiting += time

    def getWaitingTime(self):
        return self.waiting


    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color