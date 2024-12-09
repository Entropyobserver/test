class Robot:
    def __init__(self, name, mechanism, cost, year):
        self.name = name        # Define instance attributes
        self.mechanism = mechanism
        self.cost = cost
        self.year = year

# Create five robot instances
robot1 = Robot("Robot1", "Vacuum", 1000, 2020)
robot2 = Robot("Robot2", "Sweeper", 2000, 2021)
robot3 = Robot("Robot3", "Washer", 3000, 2022)
robot4 = Robot("Robot4", "Duster", 4000, 2023)
robot5 = Robot("Robot5", "Mopper", 5000, 2024)

# Method 1: Print attributes individually
print("Print individual attributes:")
print(f"Name of robot1: {robot1.name}")
print(f"Cost of robot2: {robot2.cost}")
print(f"Mechanism of robot3: {robot3.mechanism}")
print(f"Year of robot4: {robot4.year}")

# Method 2: Iterate and print all robot information
print("\nIterate and print all robot information:")
robots = [robot1, robot2, robot3, robot4, robot5]
for robot in robots:
    print(f"Name: {robot.name}, Mechanism: {robot.mechanism}, Cost: {robot.cost}, Year: {robot.year}")

# Method 3: Selectively print robots with specific conditions
print("\nPrint robots with cost greater than 3000:")
for robot in robots:
    if robot.cost > 3000:
        print(f"Name: {robot.name}, Cost: {robot.cost}")

# Method 4: Calculate average cost
total_cost = sum(robot.cost for robot in robots)
average_cost = total_cost / len(robots)
print(f"\nAverage cost of robots: {average_cost}")
