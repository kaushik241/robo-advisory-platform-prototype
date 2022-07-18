from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, RadioField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


class EducationForm(FlaskForm):
    amount = FloatField(label = 'Amount', validators=[DataRequired()])
    # annual_rate = FloatField(label = 'Rate of Return', validators=[DataRequired()])
    # inflation = FloatField(label = 'Inflation Rate', validators=[DataRequired()])
    time = FloatField(label = 'Time(Years)', validators=[DataRequired()])
    deposit_freq = RadioField('Deposit Frequency', choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    compound_freq = RadioField('Compound Frequency',choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    submit = SubmitField(label='Submit')


class EducationForm(FlaskForm):
    amount = FloatField(label = 'Amount', validators=[DataRequired()])
    # annual_rate = FloatField(label = 'Rate of Return', validators=[DataRequired()])
    # inflation = FloatField(label = 'Inflation Rate', validators=[DataRequired()])
    time = FloatField(label = 'Time(Years)', validators=[DataRequired()])
    deposit_freq = RadioField('Deposit Frequency', choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    compound_freq = RadioField('Compound Frequency',choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    submit = SubmitField(label='Submit')


class MarriageForm(FlaskForm):
    amount = FloatField(label = 'Amount', validators=[DataRequired()])
    # annual_rate = FloatField(label = 'Rate of Return', validators=[DataRequired()])
    # inflation = FloatField(label = 'Inflation Rate', validators=[DataRequired()])
    time = FloatField(label = 'Time(Years)', validators=[DataRequired()])
    deposit_freq = RadioField('Deposit Frequency', choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    compound_freq = RadioField('Compound Frequency',choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    submit = SubmitField(label='Submit')


class VacationForm(FlaskForm):
    amount = FloatField(label = 'Amount', validators=[DataRequired()])
    # annual_rate = FloatField(label = 'Rate of Return', validators=[DataRequired()])
    # inflation = FloatField(label = 'Inflation Rate', validators=[DataRequired()])
    time = FloatField(label = 'Time(Years)', validators=[DataRequired()])
    deposit_freq = RadioField('Deposit Frequency', choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    compound_freq = RadioField('Compound Frequency',choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    submit = SubmitField(label='Submit')



class HouseDownPaymentForm(FlaskForm):
    amount = FloatField(label = 'Amount', validators=[DataRequired()])
    # annual_rate = FloatField(label = 'Rate of Return', validators=[DataRequired()])
    # inflation = FloatField(label = 'Inflation Rate', validators=[DataRequired()])
    down_payment_pct = FloatField(label = 'Down Payment Percentage', validators=[DataRequired()])
    time = FloatField(label = 'Time(Years)', validators=[DataRequired()])
    deposit_freq = RadioField('Deposit Frequency', choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    compound_freq = RadioField('Compound Frequency',choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    submit = SubmitField(label='Submit')


class WealthCreationForm(FlaskForm):
    amount = FloatField(label = 'Amount', validators=[DataRequired()])
    # annual_rate = FloatField(label = 'Rate of Return', validators=[DataRequired()])
    # inflation = FloatField(label = 'Inflation Rate', validators=[DataRequired()])
    payment = FloatField(label = 'Payment', validators=[DataRequired()])
    time = FloatField(label = 'Time(Years)', validators=[DataRequired()])
    deposit_freq = RadioField('Deposit Frequency', choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    compound_freq = RadioField('Compound Frequency',choices=[('Annual','Annual'),('Semi-Annual','Semi-Annual'),('Quarterly','Quaterly'),('Bi-Monthly','Bi-Monthly'),('Monthly','Monthly'),('Semi-Monthly','Semi-Monthly'),('Bi-Weekly','Bi-Weekly'),('Weekly','Weekly'),('Daily','Daily'),], validators = [DataRequired()])
    submit = SubmitField(label='Submit')

class RetirementForm(FlaskForm):
    current_age = FloatField(label = 'Current Age', validators=[DataRequired()])
    age_at_retirement = FloatField(label = 'Age to Retirement', validators=[DataRequired()])
    years_to_payout = FloatField(label = 'Years to Payout', validators=[DataRequired()])
    # returns_during_accumulation = FloatField(label = 'Returns During Accumulation', validators=[DataRequired()])
    # returns_after_retirement = FloatField(label = 'Returns After Retirement', validators=[DataRequired()])
    # annual_inflation_rate = FloatField(label = 'Annual Inflation Rate', validators=[DataRequired()])
    current_annual_salary = FloatField(label = 'Current Annual Salary', validators=[DataRequired()])
    annual_increase_in_salary = FloatField(label = 'Annual Increase in Salary', validators=[DataRequired()])
    percentage_of_salary_contributed = FloatField(label = 'Percentage of Salary Contributed', validators=[DataRequired()])
    salary_during_retirement = FloatField(label = 'Salary During Retirement', validators=[DataRequired()])
    current_retirement_saving_balance = FloatField(label = 'Current Retirement Saving Balance', validators=[DataRequired()])
    submit = SubmitField(label='Submit')














