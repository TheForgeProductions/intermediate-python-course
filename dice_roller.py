import random

def main():
  dice_rolls = int(input('How many dice would you like to roll?\n'))
  dice_total = 0
  dice_size = int(input('How many sides per die?\n'))
  for i in range(1,dice_rolls):
    roll = random.randint(1,dice_size)
    if roll == 2:
      print('Snake eyes mothafuckah!')
    elif roll == 6:
      print('Its a six')      
    else:
       print(f'You rolled a {roll}')
    dice_total += roll
  print(f'Total of all rolls: {dice_total}')

if __name__== "__main__":
  main()