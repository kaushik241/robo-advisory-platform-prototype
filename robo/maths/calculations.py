import pandas as pd
import numpy as np
import numpy_financial as npf
import datetime 
from monthdelta import monthdelta


class Calculation:
    mapping_dict = {'Annual':1,
                        'Semi-Annual':2,
                        'Quarterly':4,
                        'Bi-Monthly':6,
                        'Monthly':12,
                        'Semi-Monthly':24,
                        'Bi-Weekly':26,
                        'Weekly':52,
                        'Daily':365}
    
    
    def __init__(self,annual_rate, inflation):
        self.annual_rate = annual_rate
        self.inflation = inflation
        
    def education(self, amount, time, deposit_freq = 'Annual', compound_freq ='Annual'):
        deposit_freq = Calculation.mapping_dict[deposit_freq]
        compound_freq = Calculation.mapping_dict[compound_freq]
        nper = time*deposit_freq
        rate = (1 + self.annual_rate/compound_freq)**(compound_freq/deposit_freq) - 1
        future_value = amount * (1 + self.inflation)**time
        payment_per_peiod = npf.pmt(rate, nper, 0, -future_value, 0)
        return payment_per_peiod
    
    def marriage(self, amount, time, deposit_freq = 'Annual', compound_freq ='Annual'):
        deposit_freq = Calculation.mapping_dict[deposit_freq]
        compound_freq = Calculation.mapping_dict[compound_freq]

        nper = time*deposit_freq
        rate = (1 + self.annual_rate/compound_freq)**(compound_freq/deposit_freq) - 1
        future_value = amount * (1 + self.inflation)**time
        payment_per_peiod = npf.pmt(rate, nper, 0, -future_value, 0)
        return payment_per_peiod    
    
    def vacation(self, amount, time, deposit_freq = 'Annual', compound_freq ='Annual'):
        deposit_freq = Calculation.mapping_dict[deposit_freq]
        compound_freq = Calculation.mapping_dict[compound_freq]

        nper = time*deposit_freq
        rate = (1 + self.annual_rate/compound_freq)**(compound_freq/deposit_freq) - 1
        future_value = amount * (1 + self.inflation)**time
        payment_per_peiod = npf.pmt(rate, nper, 0, -future_value, 0)
        return payment_per_peiod
    
    def house_down_payment(self, amount, down_payment_pct,time,deposit_freq = 'Annual', compound_freq ='Annual'):   
        deposit_freq = Calculation.mapping_dict[deposit_freq]
        compound_freq = Calculation.mapping_dict[compound_freq]

        down_payment_pv = amount * down_payment_pct
        down_payment_fv = down_payment_pv * (1 + self.inflation)**time
        payment_remaining_pv = amount - down_payment_pv
        loan_amount = amount - down_payment_pv
        nper = time*deposit_freq
        rate = (1 + self.annual_rate/compound_freq)**(compound_freq/deposit_freq) - 1
        payment_per_peiod = npf.pmt(rate, nper,-payment_remaining_pv,0, 0)
        return payment_per_peiod
    
    
    def wealth_creation(self, amount, payment, time, deposit_freq = 'Annual', compound_freq ='Annual'):
        deposit_freq = Calculation.mapping_dict[deposit_freq]
        compound_freq = Calculation.mapping_dict[compound_freq]

        rate = (1 + self.annual_rate/compound_freq)**(compound_freq/deposit_freq) - 1
        start_date = datetime.date.today()
        df_wealth = pd.DataFrame(columns = ['Date','Payment', 'Payment+Principle', 'Interest','Cummulative Interest', 'Balance'], index = (range(0,int(time*deposit_freq+1))))
        df_wealth['Date'].iloc[0] = datetime.date.today()
        df_wealth['Payment+Principle'].iloc[0] = amount
        df_wealth['Balance'].iloc[0] = amount
        df_wealth['Payment'][1:] = payment
        df_wealth['Payment'].iloc[0] = 0
        df_wealth['Interest'].iloc[0] = 0
        df_wealth['Cummulative Interest'].iloc[0] = 0
        for i in range(1,len(df_wealth)):
            df_wealth['Date'].iloc[i] = df_wealth['Date'].iloc[i-1] + monthdelta(months = 1)
            df_wealth['Payment+Principle'].iloc[i] = df_wealth['Payment+Principle'].iloc[i-1] + df_wealth['Payment'].iloc[i]
            df_wealth['Interest'].iloc[i] = df_wealth['Balance'].iloc[i-1]*rate*1
            df_wealth['Balance'].iloc[i] = df_wealth['Interest'].iloc[i] + df_wealth['Balance'].iloc[i-1] + df_wealth['Payment'].iloc[i]

        df_wealth['Cummulative Interest'] = df_wealth['Interest'].cumsum()
        total_payments = sum(df_wealth['Payment'])
        total_payments_plus_principle = total_payments + amount
        total_investment_gains = sum(df_wealth['Interest'])
        future_value = df_wealth['Balance'].iloc[-1]
        present_value = npf.pv(self.inflation,time,0,-future_value,0)
        df_wealth['Date'] = pd.to_datetime(df_wealth['Date'], format = '%Y-%m-%d')
                
        return {'df_wealth':df_wealth, 'total_investment_gains':total_investment_gains, 'future_value':future_value,'present_value':present_value}
    
    
    def retirement(self, current_age = 25, age_at_retirement = 65, years_to_payout = 25,
               returns_during_accumulation = 0.06,returns_after_retirement = 0.03,annual_inflation = 0.03,
               current_annual_salary = 50000, annual_increase_in_salary = 0.02,
               percent_of_salary_contributed = 0.1,salary_during_retirement = 50000,
               current_retirement_saving_balance = 20000):
    
        #personal information
        years_to_invest = age_at_retirement - current_age

        #Rates and Inflation
        #Salary

        #Current Saving Contribution
        total_annual_contribution = percent_of_salary_contributed * current_annual_salary



        inflation_adjusted_salary_at_retirement = npf.fv(rate = annual_inflation,nper = age_at_retirement-current_age,pmt =0,pv = -salary_during_retirement)

        #assumption that we are taking the return at the starting period
        #and we are taking income yearly after retirement
        rate = (1 + returns_after_retirement)/(1 + annual_inflation) - 1
        nper = years_to_payout * 1 
        pmt = inflation_adjusted_salary_at_retirement
        needed_to_save_100_perc_retirement = npf.pv(rate,nper,-pmt,0,1)

        #Current retirement savings
        value_of_current_saving_at_retirement = npf.fv(returns_during_accumulation, years_to_invest, 0, -current_retirement_saving_balance,0)



        #to calculate accumulated money
        if annual_increase_in_salary == returns_during_accumulation:
            value_of_current_contribution_at_retirement = total_annual_contribution*((years_to_invest)*(1 + returns_during_accumulation)**(years_to_invest))
        else:
            value_of_current_contribution_at_retirement = total_annual_contribution*((1 + annual_increase_in_salary)**(years_to_invest) - (1 + returns_during_accumulation)**(years_to_invest))/(annual_increase_in_salary- returns_during_accumulation)

        #to calculate short fall
        shortfall_at_retirement = needed_to_save_100_perc_retirement - value_of_current_saving_at_retirement - value_of_current_contribution_at_retirement 

        #to calculate how many year last
        rate = rate = (1 + returns_after_retirement)/(1 + annual_inflation) - 1
        years_pay_out_will_last = npf.nper(rate, -inflation_adjusted_salary_at_retirement, -(needed_to_save_100_perc_retirement - shortfall_at_retirement))

        #to calculate payment for a goal
        if annual_increase_in_salary == returns_during_accumulation:
            additional_annual_saving = (shortfall_at_retirement*(1 + returns_during_accumulation))/(years_to_invest*(1 + annual_increase_in_salary)**years_to_invest)
        else:
            numerator = shortfall_at_retirement*(annual_increase_in_salary - returns_during_accumulation)
            denominator = (1 + annual_increase_in_salary)**years_to_invest - ( 1 + returns_during_accumulation)**years_to_invest
            additional_annual_saving = numerator/denominator

        #needed percentage of salary to save for retirement
        percent_of_salary_contributed_balanced = (additional_annual_saving + total_annual_contribution)/current_annual_salary


        #defining dataframe for the current approch
        df_accumulation = pd.DataFrame(columns = ['Year','Age', 'Return', 'Salary Basis', 'Annual Contribution', 'Retirement Income', 'Payout', 'Interest Earned', 'Balance'],index = range(years_to_invest+1))
        df_retirement = pd.DataFrame(columns = ['Year','Age', 'Return', 'Salary Basis', 'Annual Contribution', 'Retirement Income', 'Payout', 'Interest Earned', 'Balance'],index = range(years_to_payout))

        #calculation for accumulation period for current approch
        df_accumulation['Year'] = np.array(range(0,years_to_invest+1))
        df_accumulation['Age'] = np.array(range(current_age-1,years_to_invest + current_age))
        df_accumulation['Return'] = returns_during_accumulation

        #Salary Basis
        x = np.full(age_at_retirement-current_age,1+annual_increase_in_salary)
        y = np.array(range(0,years_to_invest))
        salary_basis_array = current_annual_salary*(x**y)
        df_accumulation['Salary Basis'][1:years_to_invest+1] =  salary_basis_array

        df_accumulation['Annual Contribution'] = df_accumulation['Salary Basis'] * percent_of_salary_contributed
        df_accumulation['Retirement Income'] = 0
        df_accumulation['Payout'] = 0


        #calculation for the retirement period for the current approch
        df_retirement['Year'] = np.array(range(years_to_invest+1, years_to_payout+years_to_invest+1))
        df_retirement['Age'] = np.array(range(age_at_retirement, age_at_retirement+years_to_payout))
        df_retirement['Return'] = returns_after_retirement
        df_retirement['Salary Basis'] = 0
        df_retirement['Annual Contribution'] = 0
        df_retirement['Retirement Income'] = 0
        #function to calculate payout
        for i in range(len(df_retirement)):
            df_retirement['Payout'].iloc[i] = npf.fv(annual_inflation, df_retirement['Age'].iloc[i] - current_age, 0, -salary_during_retirement)

        #combining both period accumulation and retirement
        df_accumulation_and_df_retirement = pd.concat([df_accumulation,df_retirement],axis = 0)
        df_accumulation_and_df_retirement.reset_index(drop = True, inplace = True)

        #to calculate interest earned and balance
        df_accumulation_and_df_retirement['Balance'].iloc[0] = current_retirement_saving_balance
        for i in range(1,len(df_accumulation_and_df_retirement)):
            interest_earned = (df_accumulation_and_df_retirement['Balance'].iloc[i-1]- df_accumulation_and_df_retirement['Payout'].iloc[i])*df_accumulation_and_df_retirement['Return'].iloc[i]
            balance = interest_earned + df_accumulation_and_df_retirement['Balance'].iloc[i-1]+df_accumulation_and_df_retirement['Annual Contribution'].iloc[i] - df_accumulation_and_df_retirement['Payout'].iloc[i]
            df_accumulation_and_df_retirement['Interest Earned'].iloc[i] = interest_earned
            df_accumulation_and_df_retirement['Balance'].iloc[i] = balance
        df_accumulation_and_df_retirement.fillna(0,inplace = True)


        ## For Balanced Senario

        #defining dataframe for balanced senario
        df_accumulation_balanced = pd.DataFrame(columns = ['Year','Age', 'Return', 'Salary Basis', 'Annual Contribution', 'Retirement Income', 'Payout', 'Interest Earned', 'Balance'],index = range(years_to_invest+1))
        df_retirement_balanced = pd.DataFrame(columns = ['Year','Age', 'Return', 'Salary Basis', 'Annual Contribution', 'Retirement Income', 'Payout', 'Interest Earned', 'Balance'],index = range(years_to_payout))

        #calculation for the accumulation for balanced senario
        df_accumulation_balanced['Year'] = np.array(range(0,years_to_invest+1))
        df_accumulation_balanced['Age'] = np.array(range(current_age-1,years_to_invest + current_age))
        df_accumulation_balanced['Return'] = returns_during_accumulation

        #Salary Basis
        x = np.full(age_at_retirement-current_age,1+annual_increase_in_salary)
        y = np.array(range(0,years_to_invest))
        salary_basis_array = current_annual_salary*(x**y)
        df_accumulation_balanced['Salary Basis'][1:years_to_invest+1] =  salary_basis_array

        df_accumulation_balanced['Annual Contribution'] = df_accumulation_balanced['Salary Basis'] * percent_of_salary_contributed_balanced
        df_accumulation_balanced['Retirement Income'] = 0
        df_accumulation_balanced['Payout'] = 0

        #calculation for the retirement period for the balanced senario
        df_retirement_balanced['Year'] = np.array(range(years_to_invest+1, years_to_payout+years_to_invest+1))
        df_retirement_balanced['Age'] = np.array(range(age_at_retirement, age_at_retirement+years_to_payout))
        df_retirement_balanced['Return'] = returns_after_retirement
        df_retirement_balanced['Salary Basis'] = 0
        df_retirement_balanced['Annual Contribution'] = 0
        df_retirement_balanced['Retirement Income'] = 0
        #function to calculate payout
        for i in range(len(df_retirement_balanced)):
            df_retirement_balanced['Payout'].iloc[i] = npf.fv(annual_inflation, df_retirement_balanced['Age'].iloc[i] - current_age, 0, -salary_during_retirement)

        #combining accumulation and retirement period for balanced senario
        df_accumulation_and_df_retirement_balanced = pd.concat([df_accumulation_balanced,df_retirement_balanced],axis = 0)
        df_accumulation_and_df_retirement_balanced.reset_index(drop = True, inplace = True)

        #to calculate interest earned and balance for balanced senario
        df_accumulation_and_df_retirement_balanced['Balance'].iloc[0] = current_retirement_saving_balance
        for i in range(1,len(df_accumulation_and_df_retirement_balanced)):
            interest_earned = (df_accumulation_and_df_retirement_balanced['Balance'].iloc[i-1]- df_accumulation_and_df_retirement_balanced['Payout'].iloc[i])*df_accumulation_and_df_retirement_balanced['Return'].iloc[i]
            balance = interest_earned + df_accumulation_and_df_retirement_balanced['Balance'].iloc[i-1]+df_accumulation_and_df_retirement_balanced['Annual Contribution'].iloc[i] - df_accumulation_and_df_retirement_balanced['Payout'].iloc[i]
            df_accumulation_and_df_retirement_balanced['Interest Earned'].iloc[i] = interest_earned
            df_accumulation_and_df_retirement_balanced['Balance'].iloc[i] = balance

        df_accumulation_and_df_retirement_balanced.fillna(0,inplace = True)

        #for calcuating comparision dataframe
        df_comparision = pd.DataFrame(columns = ['Year','Current Approch', 'Modified(Balanced) Approch'])
        df_comparision['Year'] = df_accumulation_and_df_retirement['Year']
        df_comparision['Current Approch'] = df_accumulation_and_df_retirement['Balance']

        df_comparision['Modified(Balanced) Approch'] = df_accumulation_and_df_retirement_balanced['Balance']
        df_comparision.set_index('Year',inplace = True)
        
        return df_comparision


#######################################################################################################################################################################
class FinancialPlanner:
    #we will ask for name, age and having rating of your self form 0 to 10 with finance
    df_asset_allocation_before_retirement = pd.DataFrame({'Types':['Conservative','Moderate','Balanced','Assertive','Aggressive'],
                              'Equity':[0.15,0.35,0.5,0.7,0.7],
                              'Debt':[0.75,0.55,0.35,0.20,0.15],
                              'Commodities':[0.10,0.10,0.10,0.05,0.05],
                              'Real Estate':[0,0,0.05,0.05,0.10]})
    df_class_returns = pd.DataFrame({'Asset Class':['Equity', 'Debt', 'Commodities', 'Real Estate'],'Returns':[0.12,0.065,0.075,0.09]})
    
    df_asset_allocation_after_retirement = pd.DataFrame({'Types':['After Retirement'],'Equity':[0.15],'Debt':[0.75],'Commodities':[0.10],'Real Estate':[0]})
    
    
    def __init__(self,score):
        self.score = score
        
    def type_after_assessing_risk(self):
        if self.score <= 21:
            self.type_of_investor = 'Conservative'

        elif self.score <= 44:
            self.type_of_investor = 'Moderate'

        elif self.score <= 68:
            self.type_of_investor = 'Balanced'

        elif self.score <= 90:
            self.type_of_investor = 'Assertive'

        else:
            self.type_of_investor = 'Aggressive'
            
        
       
    def asset_allocation(self):
        self.type_after_assessing_risk()
        df_asset_allocation_before_retirement_local = self.df_asset_allocation_before_retirement.set_index('Types')
        df_class_returns_local = self.df_class_returns.set_index('Asset Class')
        df_asset_allocation_after_retirement_local = self.df_asset_allocation_after_retirement.set_index('Types')
        df_asset_allocation_before_retirement_local['Portfolio Return Before Retirement'] = np.dot(df_asset_allocation_before_retirement_local,df_class_returns_local)
        
        self.retirement_return = np.dot(df_asset_allocation_after_retirement_local,df_class_returns_local)[0][0]
        df_asset_allocation_before_retirement_local =  pd.DataFrame(df_asset_allocation_before_retirement_local['Portfolio Return Before Retirement'])
        self.accumulation_return = df_asset_allocation_before_retirement_local.loc[self.type_of_investor][0]
        
        
        
        return {'accumulation_return':self.accumulation_return, 'retirement_return':self.retirement_return,'type_of_investor':self.type_of_investor}
    
        
    
    
        
        
        
    
    