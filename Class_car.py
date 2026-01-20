class Car:
    def __init__ (self,name):
        self.name=name
        
    def start (self):
        print("The",self.name ,"is being started....")
    def stop(self):
        print("The",self.name,"is being stopped....")
s=Car("Bentley")
s.stop()