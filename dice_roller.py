import random

def main():
  dice_rolls = int(input('How many dice would you like to roll?\n'))
  dice_total = 0
  print(dice_rolls)
  for i in range(1,dice_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    dice_total += roll
  print(f'Total: {dice_total}')

if __name__== "__main__":
  main()