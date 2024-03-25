class Cars:
    def __init__(self):
        print("This is the car factory!")

    def car_speed(self, speed):
        self.speed=speed
        speed = speed * 120
        return speed

c1 = Cars()
print(c1.car_speed(60))

# This happens because Python automatically passes the instance as the first argument, but the method doesn't have a parameter to receive it.
