class ClockAngle:
    def __init__(self):
        self.hour = int(input("Enter hour (1-12): "))
        self.minute = int(input("Enter minutes (0-59): "))

    def find_angle(self):
        if self.hour == 12:
            self.hour = 0

        hour_angle = (30 * self.hour) + (0.5 * self.minute)
        minute_angle = 6 * self.minute

        angle = abs(hour_angle - minute_angle)

        if angle > 180:
            angle = 360 - angle

        print("Angle between clock hands =", angle, "degrees")


obj = ClockAngle()
obj.find_angle()