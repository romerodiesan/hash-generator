import click
from hashgen.algorithms import Algorithms


data = (
  'shake_128', 'sha3_224', 'sha3_384', 'shake_256', 'whirlpool', 'sha384', 'blake2b', 'sha512_256', 'blake2s', 'sha3_256', 'sha512_224', 'ripemd160', 'sha3_512', 'md5-sha1',
  'bcrypt', 'sha1', 'sha224', 'md4', 'md5', 'sm3', 'sha256', 'sha512'
)


@click.group()
def cli():
  pass


@cli.command()
@click.option('--algorithm', '-a', default='bcrypt', help='Algorithm to use')
@click.option('--difficulty', '-d', default=4, help='Difficulty of the hash')
def generate(algorithm, difficulty) -> str:
  alg = Algorithms(algorithm, difficulty)
  if not difficulty:
    difficulty = 4

  if algorithm == 'bcrypt':
    print(alg.bcrypt_gen(difficulty))
    return True
  if algorithm in data and algorithm != 'bcrypt':
    print(alg.gen(algorithm, difficulty))
    return True
  if algorithm not in data:
    print('Algorithm not found')
  else:
    password = alg.bcrypt_gen(10)
    print(password)
    return True


@cli.command()
def list():
  for i in data:
    print('* ', i)

if __name__ == '__main__':
  cli()