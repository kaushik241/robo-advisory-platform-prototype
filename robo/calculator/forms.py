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










