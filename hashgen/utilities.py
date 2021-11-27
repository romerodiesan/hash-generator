import random

def random_length(length) -> int:
  if length in range(1, 11):
    number = int(length * '9')
  
  else:
    number = int(4 * '9')
  
  return random.randint(1, number)


def random_string(lenght: int) -> str:
  return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()') for i in range(lenght))


def string_generator_and_encoding(difficulty) -> str:
  size = random_length(difficulty)
  string = random_string(lenght=size)
  string = bytes(string, encoding='utf-8')
  
  return string
