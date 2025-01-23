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
            self.current_speed+=self.acceleration
            if self.current_speed>self.max_speed:
                self.current_speed=self.max_speed   
        
    def apply_brakes(self):
        self.currrent_speed-=self.tyre_friction
        if self.current_speed<0:
            self.current_speed=0
            
    
    def sound_horn(self):
        if self.is_engine_started:
            print("Beep Beep")
        else:
            print("Car has not started yet")

class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight, load):
        super().__init__(self, color, max_speed, acceleration, tyre_friction)
        self.max_cargo_weight=max_cargo_weight
        self.load=0
        
    def load_cargo(self, cargo_weight):
        self.cargo_weight=cargo_weight
        if self.is_engine_started==False:
            self.load+=self.cargo_weight
        elif self.cargo_weight>=self.max_cargo_weight:
            print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
        else:
            print("Cannot load cargo during motion")
            
    def unload_cargo(self, cargo_weight):
        self.cargo_weight=cargo_weight
        if self.is_engine_started==False:
            self.load-=self.cargo_weight
        elif self.cargo_weight<0:
            self.cargo_weight=0
        else:
            print("Cannot unload cargo during motion")
    
    def sound_horn(self):
        if self.is_engine_started==True:
            print("Honk Honk")
        else:
            print("Car has not started yet")