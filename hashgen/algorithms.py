import bcrypt
import hashlib

from hashgen.utilities import string_generator_and_encoding

class Algorithms:
  def __init__(self, algorithm, difficulty) -> None:
    self.algorithm = algorithm
    self.difficulty = difficulty
  

  def bcrypt_gen(self, difficulty):
    string = string_generator_and_encoding(difficulty=difficulty)
    return bcrypt.hashpw(string, bcrypt.gensalt()).decode('utf-8')


  def gen(self, algorithm, difficulty):
    string = string_generator_and_encoding(difficulty=difficulty)
    return hashlib.new(name=algorithm, data=string).hexdigest()