#DiceRoll.py
#Name: Liam Gillispie
#Date: 3/1/2026
#Assignment: Lab 6
#Purpose: Simulate two rolling dice, show counts and percentages
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  total_rolls=int(input("How many rolls would you like to run for these dice? (Must be 10000 or more)"))
  for r in range(total_rolls):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
  #find the sum total of the two dice
    current_sum=dice1+dice2
    rolls[current_sum-2]=rolls[current_sum-2]+1
  #print statictics for dice rolls
  current_sum_value=2
  for count in rolls:
    percent=(count/total_rolls)*100
    print(f"{current_sum_value}:{count}:{percent:.2f}%")
    current_sum_value=current_sum_value+1
  

if __name__ == '__main__':
  main()
