#models.py 
from robo import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    #profile_image = db.Column(db.String(64), nullable = False, default = 'default_profile.png')
    email = db.Column(db.String(64), unique = True, index = True)
    username = db.Column(db.String(64), unique = True, index = True)
    password_hash = db.Column(db.String(128))

    #posts = db.relationship('BlogPost', backref = 'author', lazy = True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'Usernaem {self.username}'



class EducationTable(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float())
    annual_rate = db.Column(db.Float())
    inflation = db.Column(db.Float())
    time = db.Column(db.Float())
    deposit_freq = db.Column(db.String()) 
    compound_freq = db.Column(db.String())
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __init__(self,amount, annual_rate, inflation, time, deposit_freq, compound_freq, owner):
        self.amount = amount
        self.annual_rate = annual_rate
        self.inflation = inflation
        self.time = time
        self.deposit_freq = deposit_freq
        self.compound_freq = compound_freq
        self.owner = owner 


    def __repr__(self):
        return f'Owner {self.owner}'  




class MarriageTable(db.Model):
    __tablename__ = 'marriage'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float())
    annual_rate = db.Column(db.Float())
    inflation = db.Column(db.Float())
    time = db.Column(db.Float())
    deposit_freq = db.Column(db.String()) 
    compound_freq = db.Column(db.String())
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __init__(self,amount, annual_rate, inflation, time, deposit_freq, compound_freq, owner):
        self.amount = amount
        self.annual_rate = annual_rate
        self.inflation = inflation
        self.time = time
        self.deposit_freq = deposit_freq
        self.compound_freq = compound_freq
        self.owner = owner 


    def __repr__(self):
        return f'Owner {self.owner}' 



class VacationTable(db.Model):
    __tablename__ = 'vacation'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float())
    annual_rate = db.Column(db.Float())
    inflation = db.Column(db.Float())
    time = db.Column(db.Float())
    deposit_freq = db.Column(db.String()) 
    compound_freq = db.Column(db.String())
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __init__(self,amount, annual_rate, inflation, time, deposit_freq, compound_freq, owner):
        self.amount = amount
        self.annual_rate = annual_rate
        self.inflation = inflation
        self.time = time
        self.deposit_freq = deposit_freq
        self.compound_freq = compound_freq
        self.owner = owner 


    def __repr__(self):
        return f'Owner {self.owner}' 



class HouseDownPaymentTable(db.Model):
    __tablename__ = 'housedownpayment'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float())
    down_payment_pct = db.Column(db.Float())
    annual_rate = db.Column(db.Float())
    inflation = db.Column(db.Float())
    time = db.Column(db.Float())
    deposit_freq = db.Column(db.String()) 
    compound_freq = db.Column(db.String())
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __init__(self,amount, down_payment_pct, annual_rate, inflation, time, deposit_freq, compound_freq, owner):
        self.amount = amount
        self.down_payment_pct = down_payment_pct
        self.annual_rate = annual_rate
        self.inflation = inflation
        self.time = time
        self.deposit_freq = deposit_freq
        self.compound_freq = compound_freq
        self.owner = owner 


    def __repr__(self):
        return f'Owner {self.owner}' 


class WealthCreationTable(db.Model):
    __tablename__ = 'wealthcreation'
    id = db.Column(db.Integer(), primary_key=True)
    amount = db.Column(db.Float())
    payment = db.Column(db.Float())
    annual_rate = db.Column(db.Float())
    inflation = db.Column(db.Float())
    time = db.Column(db.Float())
    deposit_freq = db.Column(db.String()) 
    compound_freq = db.Column(db.String())
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))


    def __init__(self,amount, payment, annual_rate, inflation, time, deposit_freq, compound_freq, owner):
        self.amount = amount
        self.payment = payment
        self.annual_rate = annual_rate
        self.inflation = inflation
        self.time = time
        self.deposit_freq = deposit_freq
        self.compound_freq = compound_freq
        self.owner = owner 


    def __repr__(self):
        return f'Owner {self.owner}'


class RetirementTable(db.Model):
    __tablename__ = 'retirement'
    id = db.Column(db.Integer(), primary_key=True)
    current_age = db.Column(db.Integer())
    age_at_retirement = db.Column(db.Integer())
    years_to_payout = db.Column(db.Integer())
    returns_during_accumulation = db.Column(db.Float())
    returns_after_retirement = db.Column(db.Float())
    annual_inflation_rate = db.Column(db.Float())
    current_annual_salary = db.Column(db.Float())
    annual_increase_in_salary = db.Column(db.Float())
    percentage_of_salary_contributed = db.Column(db.Float())
    salary_during_retirement = db.Column(db.Float())
    current_retirement_saving_balance = db.Column(db.Float())
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __init__(self,current_age, age_at_retirement, years_to_payout, returns_during_accumulation, returns_after_retirement, annual_inflation_rate, current_annual_salary, annual_increase_in_salary, percentage_of_salary_contributed, salary_during_retirement, current_retirement_saving_balance, owner):
        self.current_age = current_age
        self.age_at_retirement = age_at_retirement
        self.years_to_payout = years_to_payout
        self.returns_during_accumulation = returns_during_accumulation
        self.returns_after_retirement = returns_after_retirement
        self.annual_inflation_rate = annual_inflation_rate
        self.current_annual_salary = current_annual_salary
        self.annual_increase_in_salary = annual_increase_in_salary
        self.percentage_of_salary_contributed = percentage_of_salary_contributed
        self.salary_during_retirement = salary_during_retirement
        self.current_retirement_saving_balance = current_retirement_saving_balance
        self.owner = owner
    

    def __repr__(self):
        return f'Owner {self.owner}'



class Questions(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.Text)
    a = db.Column(db.Text)
    b = db.Column(db.Text)
    c = db.Column(db.Text)
    d = db.Column(db.Text)
    e = db.Column(db.Text)
    f = db.Column(db.Text)
    marks = db.relationship('QuestionsMarks', backref = 'que', lazy = True)

    def __init__(self,question,a,b,c,d,e,f):
        self.question = question
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f




class  QuestionsMarks(db.Model):
    __tablename__ = 'questionsmarks'

    id = db.Column(db.Integer, primary_key = True)
    questionid = db.Column(db.Integer, db.ForeignKey('questions.id'))
    a = db.Column(db.Integer)
    b = db.Column(db.Integer)
    c = db.Column(db.Integer)
    d = db.Column(db.Integer)
    e = db.Column(db.Integer)
    f = db.Column(db.Integer)

    def __init__(self,questionid,a,b,c,d,e,f):
        self.questionid = questionid
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f


# class Results(db.Model):
#     __tablename__ = 'results'

#     id = db.Column(db.Integer, primary_key = True)
#     owner = db.Column(db.Integer(), db.ForeignKey('users.id'))
#     questionid = db.Column(db.Integer(), db.ForeignKey('questions.id'))

class Results(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))
    question1 = db.Column(db.Integer())
    question2 = db.Column(db.Integer())
    question3 = db.Column(db.Integer())
    question4 = db.Column(db.Integer())
    question5 = db.Column(db.Integer())
    question6 = db.Column(db.Integer())
    question7 = db.Column(db.Integer())
    question8 = db.Column(db.Integer())
    question9 = db.Column(db.Integer())
    question10 = db.Column(db.Integer())
    question11 = db.Column(db.Integer())
    question12 = db.Column(db.Integer())
    question13 = db.Column(db.Integer())
    question14 = db.Column(db.Integer())


    def __init__(self,owner,question1,question2,question3,question4,question5,question6,question7,question8,question9,question10,question11,question12,question13,question14):
        self.owner = owner
        self.question1 = question1
        self.question2 = question2
        self.question3 = question3
        self.question4 = question4
        self.question5 = question5
        self.question6 = question6
        self.question7 = question7
        self.question8 = question8
        self.question9 = question9
        self.question10 = question10
        self.question11 = question11
        self.question12 = question12
        self.question13 = question13
        self.question14 = question14


class RiskProfile(db.Model):
    __tablename__ = 'riskprofile'

    id = db.Column(db.Integer, primary_key = True)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))
    type_of_investor = db.Column(db.String(20))
    accumulation_return = db.Column(db.Float())
    retirement_return = db.Column(db.Float())

    def __init__(self, owner, type_of_investor, accumulation_return, retirement_return):
        self.owner = owner
        self.type_of_investor = type_of_investor
        self.accumulation_return = accumulation_return
        self.retirement_return = retirement_return
        






        
    
    
    
    
    
    
    
    
    
    
    
    
    
    










