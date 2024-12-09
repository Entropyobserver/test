class Parasite:
    counter = 0

    @classmethod
    def increment_counter(cls):
        cls.counter += 1
        return cls.counter

# Create instances of Parasite
parasite1 = Parasite()
print(Parasite.increment_counter())  # Output: 1

parasite2 = Parasite()
print(Parasite.increment_counter())  # Output: 2

@classmethod 
def increment_counter(cls):
    cls.counter += 1
    return cls.counter

@classmethod
def increment_counter(cls):
    cls.counter += 1
    return cls.counter