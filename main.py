import math


class MathsAppObject:

    def __init__(self, x, y, point_name):
        self.x = x
        self.y = y
        self.point_name = point_name

    def input_attributes(self):
        self.x = float(input("Nceda ufake uququzelelo x:"))
        self.y = float(input("Nceda ufake uququzelelo y:"))
        self.point_name = (input("Nceda ufake igama lendawo :"))

    def output(self):
        print("==========================================================================================")
        print("                            Wamkelekile kwi MATHS APP                                     ")
        print("===========================================================================================")
        print("===========================================================================================")
        print("*********************************************************************************************")
        print("Imbonakalo X-Axis ngu : (", self.x, ",  ", reflection_x(self), ") Kwinqaku :  ", self.point_name)
        print("Imbonakalo Y-Axis ngu : (", reflection_y(self), " , ", self.y, ") Kwinqaku :  ", self.point_name)
        print("Ifomula yomgca ochanekileyo yile ", "", "y = ", (self.y - 0) / (self.x - 0), "x  + ", self.y)
        print("Ulungelelwaniso lwenqaku: " + "'", self.point_name, "'" + "", quadrant(self))
        print("Umgama phakathi konxibelelaniso kwa (", self.x, ",", self.y, ") kunye ( 0,0) :", calculate_distance(self))
        print("***********************************************************************************************")

def calculate_distance(self):
    return math.sqrt(pow((self.x - self.y), 2) + pow(0, 2))


def reflection_x(self):
    return (-1) * self.y


def reflection_y(self):
    return (-1) * self.x


def quadrant(self):
    if self.x <= 0 or self.y <= 0:
        return
    quad = " ilele kwikota yokuqala yokuqala, EMTLA MPUMA."
    if self.x < 0:
        quad = " ilele kwikota yesibini yesibini, EMTLA MPUMA."
        if self.y < 0:
            quad = " ilele kwikota yesithathu, EMZANTSI NTSHONA."
            quad = " ilele kwikota yesine, EMZANTSI MPUMA."
            if self.x == 0 and self.y == 0:
                quad = "ISIPHAMBUKA."

    return quad


if __name__ == '__main__':
    obj = MathsAppObject(0, 0, "")
    obj.input_attributes()
    obj.output()