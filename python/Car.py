class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.is_engine_started=False
        self.current_speed=0
        
    def start_engine(self):
        self.is_engine_started=True
        
    def stop_engine(self):
        self.is_engine_started=False
    
    def accelerate(self):
        if self.is_engine_started==False:
            print("Car has not started yet")
        else:
            self.current_speed += self.acceleration
            if (self.current_speed>self.max_speed):
                self.current_speed=self.max_speed
                
    def apply_brakes(self):
        self.current_speed-=self.tyre_friction
        if self.current_speed<0:
            self.current_speed=0
        
    def sound_horn(self):
        if self.is_engine_started==True:
            print("Beep Beep")
        else:
            print("Car has not started yet")
            
            
    
def default_test():
    car = Car("red",50,10,10)
    car.accelerate()
    print(car.current_speed)
    car.start_engine()
    car.accelerate()
    print(car.current_speed)
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    print(car.current_speed)
    car.accelerate()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    car.apply_brakes()
    car.apply_brakes()
    print(car.current_speed)
    car.apply_brakes()
    print(car.current_speed)
    car.sound_horn()
    car.stop_engine()
    car.sound_horn()
    

default_test()