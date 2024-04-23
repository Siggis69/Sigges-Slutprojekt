import random

def generate_random_list(length, min_value, max_value):

    random_list = [random.randint(min_value, max_value) for _ in range(length)]
    return random_list


random_list = generate_random_list(50, 1, 100)
print(random_list)
