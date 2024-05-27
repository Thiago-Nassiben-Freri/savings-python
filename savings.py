
class Savings: 
    def __init__(self, invested_capital, time_months, interest_rate=0.5, amount = 0):
        self.invested_capital = invested_capital
        self.time_months = time_months
        self.interest_rate = interest_rate
        self.amount = amount
    
    def savingsCalc(self): 
        '''Amount calculation: Basically we use interest compound to calculate the final amount of the investment.'''
        self.amount = self.invested_capital * (1 + (self.interest_rate / 100))**self.time_months
        return self.amount
    
    def showSavings(self): 
        '''Show Savings: Here we show the initial invested value and the final amount.'''
        self.savingsCalc()
        print(f"{'Invested Capital':<25} {'Amount':<25}")
        print(f"${self.invested_capital:<23} ${self.amount:<25.2f}")

