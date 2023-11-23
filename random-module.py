import random

# Display 10 ramdom numbers from the interval [0, 1)

for i in range(10):
    print(random.random())

# Generate 10 random numbers from the interval [3, 7)

def my_random():
    # Random, scale, shift, return
    return 4 * random.random() + 3

for i in range(10):
    # print(my_random())
    print(random.uniform(3,7))

# Normal distribution

def normal_ditribution(mean, standar_deviation):
    # Mean = mean
    # Standar deviation = standar_deviation
    print(random.normalvariate(mean, standar_deviation))
        
for i in range(20):
     normal_ditribution(1, 2)


# Discrete probability

for i in range(20):
    print(random.randint(1, 6))

# Random element from a list

outcomes = ["rock", "paper", "sissor"]

for i in range(20):
    print(random.choice(outcomes))