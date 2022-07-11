from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from robo import db
from robo.models import EducationTable, MarriageTable, HouseDownPaymentTable, WealthCreationTable, VacationTable,RiskProfile
from robo.calculator.forms import EducationForm, MarriageForm, HouseDownPaymentForm, WealthCreationForm, VacationForm
from robo.maths.calculations import Calculation
import pandas as pd 
import plotly
import plotly.express as px
import json


calculator = Blueprint('calculator', __name__)

@calculator.route('/calculator_list')
def calculator_list():
    return render_template('calculator_list.html')



@calculator.route('/calculator_list/education',methods=['GET', 'POST'])
def education_page():
    user_risk_profile = RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()
    form = EducationForm()

    if form.validate_on_submit():
        details = EducationTable(amount = form.amount.data,
                                    annual_rate = user_risk_profile.accumulation_return,
                                    inflation = 0.06,
                                    time = form.time.data,
                                    deposit_freq = form.deposit_freq.data,
                                    compound_freq = form.compound_freq.data,
                                    owner = current_user.get_id())
        db.session.add(details)
        db.session.commit()
        flash('Thanks for filling out this details')
        return redirect(url_for('calculator.education_analysis_page'))
    return render_template('education.html', form=form,accumulation_return = user_risk_profile.accumulation_return)


@calculator.route('/calculator_list/education/anaysis',methods=['GET', 'POST'])
def education_analysis_page():
    education_table_info = EducationTable.query.filter_by(owner= current_user.get_id()).order_by(EducationTable.id.desc()).first()


    calculations = Calculation(
                                annual_rate = education_table_info.annual_rate, 
                                inflation = education_table_info.inflation
                                )
    results = calculations.education(amount = education_table_info.amount,time = education_table_info.time,deposit_freq = education_table_info.deposit_freq, compound_freq =education_table_info.compound_freq)
    print(results)
    content = {'saving_amount':results, 'interval':education_table_info.deposit_freq}
    return render_template('educationresults.html',content = content)





#Marriage
@calculator.route('/calculator_list/marriage',methods=['GET', 'POST'])
def marriage_page():
    user_risk_profile = RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()
    form = MarriageForm()
    if form.validate_on_submit():
        details = MarriageTable(amount = form.amount.data,
                                    annual_rate = user_risk_profile.accumulation_return,
                                    inflation = 0.06,
                                    time = form.time.data,
                                    deposit_freq = form.deposit_freq.data,
                                    compound_freq = form.compound_freq.data,
                                    owner = current_user.get_id())
        db.session.add(details)
        db.session.commit()
        flash('Thanks for filling out this details')
        return redirect(url_for('calculator.marriage_analysis_page'))
    return render_template('marriage.html', form=form,accumulation_return = user_risk_profile.accumulation_return)


@calculator.route('/calculator_list/marriage/anaysis',methods=['GET', 'POST'])
def marriage_analysis_page():
    marriage_table_info = MarriageTable.query.filter_by(owner= current_user.get_id()).order_by(MarriageTable.id.desc()).first()
    #EducationTable.query.filter_by(owner= current_user.get_id()).order_by(EducationTable.id.desc()).first()
    calculations = Calculation(
                                annual_rate = marriage_table_info.annual_rate, 
                                inflation = marriage_table_info.inflation
                                )
    results = calculations.marriage(amount = marriage_table_info.amount,time = marriage_table_info.time,deposit_freq = marriage_table_info.deposit_freq, compound_freq =marriage_table_info.compound_freq)
    print(results)
    content = {'saving_amount':results, 'interval':marriage_table_info.deposit_freq}
    return render_template('marriageresults.html',content = content)



#House down payment
@calculator.route('/calculator_list/housedownpayment',methods=['GET', 'POST'])
def housedownpayment_page():
    user_risk_profile = RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()

    form = HouseDownPaymentForm()
    if form.validate_on_submit():
        details = HouseDownPaymentTable(amount = form.amount.data,
                                    annual_rate = user_risk_profile.accumulation_return,
                                    inflation = 0.06,
                                    down_payment_pct = form.down_payment_pct.data,
                                    time = form.time.data,
                                    deposit_freq = form.deposit_freq.data,
                                    compound_freq = form.compound_freq.data,
                                    owner = current_user.get_id())
        db.session.add(details)
        db.session.commit()
        flash('Thanks for filling out this details')
        return redirect(url_for('calculator.housedownpayment_analysis_page'))
    return render_template('housedownpayment.html', form=form,accumulation_return = user_risk_profile.accumulation_return)


@calculator.route('/calculator_list/housedownpayment/anaysis',methods=['GET', 'POST'])
def housedownpayment_analysis_page():
    housedownpayment_table_info = HouseDownPaymentTable.query.filter_by(owner= current_user.get_id()).order_by(HouseDownPaymentTable.id.desc()).first()
    calculations = Calculation(
                                annual_rate = housedownpayment_table_info.annual_rate, 
                                inflation = housedownpayment_table_info.inflation
                                )
    results = calculations.house_down_payment(amount = housedownpayment_table_info.amount,down_payment_pct = housedownpayment_table_info.down_payment_pct,time = housedownpayment_table_info.time,deposit_freq = housedownpayment_table_info.deposit_freq, compound_freq =housedownpayment_table_info.compound_freq)
    print(results)
    content = {'saving_amount':results, 'interval':housedownpayment_table_info.deposit_freq}
    return render_template('housedownpaymentresults.html',content = content)



#Vacation
@calculator.route('/calculator_list/vacation',methods=['GET', 'POST'])
def vacation_page():
    user_risk_profile = RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()
    form = VacationForm()
    if form.validate_on_submit():
        details = VacationTable(amount = form.amount.data,
                                    annual_rate = user_risk_profile.accumulation_return,
                                    inflation = 0.06,
                                    time = form.time.data,
                                    deposit_freq = form.deposit_freq.data,
                                    compound_freq = form.compound_freq.data,
                                    owner = current_user.get_id())
        db.session.add(details)
        db.session.commit()
        flash('Thanks for filling out this details')
        return redirect(url_for('calculator.vacation_analysis_page'))
    return render_template('vacation.html', form=form,accumulation_return = user_risk_profile.accumulation_return)


@calculator.route('/calculator_list/vacation/anaysis',methods=['GET', 'POST'])
def vacation_analysis_page():
    vacation_table_info = VacationTable.query.filter_by(owner= current_user.get_id()).order_by(VacationTable.id.desc()).first()
    calculations = Calculation(
                                annual_rate = vacation_table_info.annual_rate, 
                                inflation = vacation_table_info.inflation
                                )
    results = calculations.vacation(amount = vacation_table_info.amount,time = vacation_table_info.time,deposit_freq = vacation_table_info.deposit_freq, compound_freq =vacation_table_info.compound_freq)
    print(results)
    content = {'saving_amount':results, 'interval':vacation_table_info.deposit_freq}
    return render_template('vacationresults.html',content = content)


#Wealth Creation
@calculator.route('/calculator_list/wealthcreation',methods=['GET', 'POST'])
def wealthcreation_page():
    user_risk_profile = RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()
    form = WealthCreationForm()
    if form.validate_on_submit():
        details = WealthCreationTable(amount = form.amount.data,
                                    annual_rate = user_risk_profile.accumulation_return,
                                    inflation = 0.06,
                                    payment = form.payment.data,
                                    time = form.time.data,
                                    deposit_freq = form.deposit_freq.data,
                                    compound_freq = form.compound_freq.data,
                                    owner = current_user.get_id())
        db.session.add(details)
        db.session.commit()
        flash('Thanks for filling out this details')
        return redirect(url_for('calculator.wealthcreation_analysis_page'))
    return render_template('wealthcreation.html', form=form,accumulation_return = user_risk_profile.accumulation_return)


@calculator.route('/calculator_list/wealthcreation/anaysis',methods=['GET', 'POST'])
def wealthcreation_analysis_page():
    wealthcreation_table_info = WealthCreationTable.query.filter_by(owner= current_user.get_id()).order_by(WealthCreationTable.id.desc()).first()
    calculations = Calculation(
                                annual_rate = wealthcreation_table_info.annual_rate, 
                                inflation = wealthcreation_table_info.inflation
                                )
    results = calculations.wealth_creation(amount = wealthcreation_table_info.amount,payment = wealthcreation_table_info.payment,time = wealthcreation_table_info.time,deposit_freq = wealthcreation_table_info.deposit_freq, compound_freq =wealthcreation_table_info.compound_freq)
    df_wealth = results['df_wealth']
    total_investment_gains = results['total_investment_gains']
    future_value = results['future_value']
    present_value = results['present_value']

    fig = px.line(df_wealth, x="Date", y="Balance", title='See your Compounded wealth')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


    print(results)
    content = {'interval':wealthcreation_table_info.deposit_freq,'df_wealth':df_wealth, 'total_investment_gains':total_investment_gains, 'future_value':future_value,'present_value':present_value}
    return render_template('wealthcreationresults.html',content = content,graphJSON=graphJSON)








        