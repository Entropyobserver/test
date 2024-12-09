class Robot:
    power_increase = 1.1

    def __init__(self, name, mechanism, cost, power):
        self.name = name
        self.mechanism = mechanism
        self.cost = cost
        self.power = power

    def increase_power(self):
        self.power = float(self.power * self.power_increase)

    @classmethod
    def set_power_increase(cls, increase):
        cls.power_increase = increase

    @classmethod
    def from_string(cls, rob_str):
        name, mechanism, cost, power = rob_str.split("/")
        return cls(name, mechanism, int(cost), int(power))

# Creating instances of Robot
rob1 = Robot("Roborock", "Vacuum", 9000, 10)
rob2 = Robot("Terminator", "Kill", 1000000, 97)
rob3 = Robot.from_string("R2-D2/Repair/100000/60")
rob4 = Robot.from_string("TARS/Utility/5000000/80")

# Printing the name of rob4
print(rob4.name)  # Output: TARS
print(rob3)

#1

robot_data = [
    "R2-D2/Repair/100000/60",
    "TARS/Utility/5000000/80",
    "C-3PO/Translate/10/30"
]
robots = [Robot.from_string(data) for data in robot_data]
for robot in robots:
    print(robot.name, robot.mechanism, robot.cost, robot.power)
#2
with open('robots.txt', 'r') as file:
    robots = [Robot.from_string(line.strip()) for line in file]

for robot in robots:
    print(robot.name, robot.mechanism, robot.cost, robot.power)

#3
import requests 
response = requests.get('https://api.example.com/robots') 
robot_data = response.text.splitlines() 
robots = [Robot.from_string(data) for data in robot_data] 
for robot in robots: 
    print(robot.name, robot.mechanism, robot.cost, robot.power)