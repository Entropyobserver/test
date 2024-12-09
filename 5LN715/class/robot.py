

class Robot:
    pass
rob1 = Robot()
rob2 = Robot()

print(rob1)
print(rob2)
#<__main__.Robot object aD5D5DDD539E0>
#<__main__.Robot object at 0x000001DDABD53950>

class Robot:
    def __init__(self,name,mechanism,cost,year):
        self.name = name
        self.mechanism = mechanism
        self.cost = cost
        self.year = year

    def describe(self):
        return f"{self.name} is a {self.mechanism} robot that costs {self.cost} in {self.year}"

    def work(self):
        return f"{self.name} is working"
    
    def stop(self):
        return f"{self.name} has stopped working"
    
    def battery(self,power):
        self.power = power
        return power
    
    def information(self):
        print(f"Your robot is {self.name} and it is a {self.mechanism} and has a battery level of {self.power}%")

    

robot1 = Robot("Robot1","Vacume",1000,2020)
robot2 = Robot("Robot2","Sweeper",2000,2021)
robot3 = Robot("Robot3","Washer",3000,2022)
robot4 = Robot("Robot4","Duster",4000,2023)
robot5 = Robot("Robot5","Mopper",5000,2024)

print(robot1.name)
print(robot2.cost)
print(robot3.mechanism)
print(robot4.year)
print(robot5.describe())
print(robot1.work())
print(robot2.battery(100))
print(robot2.information())
"""

class Robot:
    def __init__(self, name, mechanism, cost):
        self.name = name
        self.mechanism = mechanism
        self.cost = cost

    def battery(self, power):
        self.power = power
        return power

    def information(self):
        print("Your robot is", self.name,
              "and it can", self.mechanism,
              "and has a battery level of",
              self.power, "%")

# Create an instance of the Robot class
rob1 = Robot("Roborock", "Vacuum", 9000)
rob1.battery(100)
rob1.information()
"""