from savings import Savings
from time import sleep


def exit(): 
    print('Okay, exit...')
    sleep(2)
    print('Program finished!')

def savingsUX(): 
    while True: 
        var_choice = str(input('Do you want to use Python Savings? [Y/N]: '))

        if var_choice.upper() == 'Y': 
            var_invested_capital = float(input('Enter the invested capital: '))
            var_time_months = int(input('Enter the time invested (in months): '))

            savings_inst = Savings(var_invested_capital, var_time_months)

            savings_inst.showSavings()
        elif var_choice.upper() == 'N': 
            exit()
            break
        else: 
            print(f'Wrong choice: You can only use [Y] for yes and [N] for no!')

if __name__ == '__main__': 
    savingsUX()
