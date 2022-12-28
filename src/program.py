import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
  "A" : 2,
  "B" : 4,
  "C" : 6,
  "D" : 8
}

symbol_values = {
  "A" : 5,
  "B" : 4,
  "C" : 3,
  "D" : 2
}

def slot_machine_spin(rows, cols, symbols):
  all_symbols = []
  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  columns = []
  for _ in range(cols):
    column = []
    current_symbols = all_symbols[:]
    for _ in range(rows):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      column.append(value)
    
    columns.append(column)

  return columns

#This function rearrange the output of the slot machine
def print_slot_machine(columns):
  for row in range(len(columns[0])):
    for i,column in enumerate(columns):
      if i != len(columns) - 1:
        print(column[row], end=" | ")
      else:
        print(column[row], end="")
    print()

#This function cahek if the user win
def check_winnings(columns, lines, bet, values):
  winnings = 0
  winning_lines = []
  for line in range(lines):
    symbol = columns[0][line]
    for column in columns:
      symbol_to_check = column[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)

  return winnings, winning_lines

# This function allows to user to deposit some amount
def deposit():

  while True:
    amount = input("What amount whould you like to deposit? $")

    if amount.isdigit():
      amount = int(amount)

      if amount > 0:
        break
      else:
        print("Amount must be greater than zero.")
    else:
      print("Please enter a numerical value.")
  
  return amount

#This function gets the number of lines user want to bet
def get_number_of_lines():

  while True:
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")

    if lines.isdigit():
      lines = int(lines)

      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Please enter valid number of line(s)")
    else:
      print("Please enter valid number of line(s)")
  
  return lines

#This function will get amount to bet on each line from the user
def get_bet():

  while True:
    amount = input("Enter the amount to bet on each line: $")

    if amount.isdigit():
      amount = int(amount)

      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Enter amount beteween ${MIN_BET} - ${MAX_BET}")
    else:
      print("Please enter valid amount to bet")

  return amount


def main():
  balance = deposit()
  lines = get_number_of_lines()

  while True:
    bet = get_bet()
    total_bet = bet * lines

    if total_bet > balance:
      print(f"You balance is insufficient to bet on. Your current balance is ${balance}")
    else:
      break

  print(f"You are betting ${bet} on {lines} Lines. Your total bet is ${total_bet}")

  slots = slot_machine_spin(ROWS, COLS, symbol_count)
  print_slot_machine(slots)
  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
  print(f"You won ${winnings}")
  print(f"You won on Line(s): ", *winning_lines)

main()