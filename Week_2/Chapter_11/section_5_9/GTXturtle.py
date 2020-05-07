import random
from turtle import Turtle, Screen


def get_flat_tyre_distance():
    return random.uniform(50, 150)


class TurtleGTX(Turtle):

    def __init__(self):
        super().__init__()
        self.odometer = 0
        self.flat_tyre = get_flat_tyre_distance()

    def forward(self, distance):
        if self.odometer >= self.flat_tyre:
            self.change_tyre()
        super().forward(distance)
        self.odometer += abs(distance)

    def get_odo(self):
        return self.odometer

    def change_tyre(self):
        self.flat_tyre += get_flat_tyre_distance()


if __name__ == "__main__":
    screen = Screen()
    gtx = TurtleGTX()

    gtx.forward(50)
    gtx.forward(100)
    gtx.forward(-30)
    gtx.forward(40)

    print(gtx.get_odo())

    screen.exitonclick()