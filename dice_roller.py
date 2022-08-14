import random

dice_rolls = 2
def main():
  i = 0
  for i in range(0, dice_rolls):
    roll = random.randint(1, 6)
    print(f'You rolled a {roll}')
    i = i + roll
  #1
  print(f"You have rolled a total of {i}")
if __name__== "__main__":
  main()