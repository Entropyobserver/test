class Robot:
    power_increase = 1.1  # Class attribute for power increase factor,visit by class name and instance name,if changed,will change for all instances
    power_decrease = 0.9  # Class attribute for power decrease factor,visit by class name and instance name

    def __init__(self, name, mechanism, cost, power):#self is changeable according to the instance name
        self.name = name  # Instance attribute for the robot's name
        self.mechanism = mechanism  # Instance attribute for the robot's mechanism
        self.cost = cost  # Instance attribute for the robot's cost
        self.power = power  # Instance attribute for the robot's power level

    def battery(self, power):
        self.power = power  # Method to set the robot's power level
        return power  # Return the new power level

    def information(self):
        # Method to print the robot's information
        print(f"Your robot is {self.name} and it is a {self.mechanism} and has a battery level of {self.power}%")

    def increase_power(self):
        # Method to increase the robot's power level by the power_increase factor
        self.power = float(self.power * self.power_increase)

    def decrease_power(self):
        # Method to decrease the robot's power level by the power_decrease factor
        self.power = float(self.power * self.power_decrease)

# Create an instance of the Robot class with initial attributes
rob1 = Robot("Robot1", "Vacuum", 1000, 100)
# Create another instance of the Robot class with initial attributes
rob2 = Robot("Robot2", "Sweeper", 2000, 100)

# Print the initial power level of rob1
print(rob1.power)
# Increase the power level of rob1
rob1.increase_power()
# Print the updated power level of rob1
print(rob1.power)
print("-" * 20)  # Print a separator line

# Print the initial power level of rob2
print(rob2.power)
# Decrease the power level of rob2
rob2.decrease_power()
print("-" * 20)  # Print a separator line

# Access and print the class attribute power_increase through the class itself
print(Robot.power_increase)
# Access and print the class attribute power_decrease through the class itself
print(Robot.power_decrease)
print("-" * 20)  # Print a separator line

# Access and print the class attribute power_increase through the first class instance
print(rob1.power_increase)
# Access and print the class attribute power_decrease through the first class instance
print(rob1.power_decrease)
print("-" * 20)  # Print a separator line

# Access and print the class attribute power_increase through the second class instance
print(rob2.power_increase)
# Access and print the class attribute power_decrease through the second class instance
print(rob2.power_decrease)
