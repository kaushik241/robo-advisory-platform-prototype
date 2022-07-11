from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from robo import db
from werkzeug.security import generate_password_hash,check_password_hash
from robo.models import User,RiskProfile,Results,EducationTable, MarriageTable, HouseDownPaymentTable, VacationTable, WealthCreationTable
from robo.users.forms import RegistrationForm, LoginForm, UpdateUserForm
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
from robo.maths.calculations import Calculation

#from robo.users.picture_handler import add_profile_pic


users = Blueprint('users', __name__)

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login!')
        return redirect(url_for('users.login'))
    return render_template('register.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        # Grab the user from our User Models table
        user = User.query.filter_by(email=form.email.data).first()

        # Check that the user was supplied and the password is right
        # The verify_password method comes from the User object
        # https://stackoverflow.com/questions/2209755/python-operation-vs-is-not

        if user.check_password(form.password.data) and user is not None:
            #Log in the user

            login_user(user)
            flash('Logged in successfully.')

            # If a user was trying to visit a page that requires a login
            # flask saves that URL as 'next'.
            next = request.args.get('next')

            # So let's now check if that next exists, otherwise we'll go to
            # the welcome page.
            if next == None or not next[0]=='/':
                next = url_for('users.dashboard')

            return redirect(next)
    return render_template('login.html', form=form)




@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('core.index'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    user_risk_profile = RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()
    form = UpdateUserForm()

    if form.validate_on_submit():
        print(form)
        # if form.picture.data:
            # username = current_user.username
            # pic = add_profile_pic(form.picture.data,username)
            # current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    #profile_image = url_for('static', filename='profile_pics/' + current_user.profile_image)
    return render_template('account.html',form=form, user_risk_profile = user_risk_profile)

# @users.route("/<username>")
# def user_posts(username):
#     page = request.args.get('page', 1, type=int)
#     user = User.query.filter_by(username=username).first_or_404()
#     blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
#     return render_template('user_blog_posts.html', blog_posts=blog_posts, user=user)


@users.route('/dashboard')
def dashboard():
    education_results_content = {}
    
    user = User.query.filter_by(id= current_user.get_id()).order_by(User.id.desc()).first()
    risk_analysis_results =  RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()
    if risk_analysis_results:
        results = Results.query.filter_by(owner= current_user.get_id()).order_by(Results.id.desc()).first()
        results_sum = (results.question1 + results.question2 + results.question3 +
                        results.question4 + results.question5 + results.question6 +
                        results.question7 + results.question8 + results.question9 +
                        results.question10 + results.question11 + results.question12 +
                        results.question13 + results.question14)

        print(user.username)
        fig = go.Figure(go.Indicator(
            domain = {'x': [0, 1], 'y': [0, 1]},
            value = results_sum,
            mode = "gauge+number",
            title = {'text': "Riskness"},
            gauge = {'axis': {'range': [None, 100]},}))
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)


        education_table_info = EducationTable.query.filter_by(owner= current_user.get_id()).order_by(EducationTable.id.desc()).first()
        marriage_table_info =  MarriageTable.query.filter_by(owner= current_user.get_id()).order_by(MarriageTable.id.desc()).first()
        wealthcreation_table_info =  WealthCreationTable.query.filter_by(owner= current_user.get_id()).order_by(WealthCreationTable.id.desc()).first()
        vacation_table_info =  VacationTable.query.filter_by(owner= current_user.get_id()).order_by(VacationTable.id.desc()).first()
        housedownpayment_table_info =  HouseDownPaymentTable.query.filter_by(owner= current_user.get_id()).order_by(HouseDownPaymentTable.id.desc()).first()


        if education_table_info or marriage_table_info or wealthcreation_table_info or vacation_table_info or housedownpayment_table_info:
            education_results_content = None
            marriage_results_content = None
            wealthcreation_results_content = None
            vacation_results_content = None 
            housedownpayment_results_content = None

            if education_table_info:
                calculations = Calculation(annual_rate = education_table_info.annual_rate, 
                                        inflation = education_table_info.inflation)

                education_results = calculations.education(amount = education_table_info.amount,time = education_table_info.time,deposit_freq = education_table_info.deposit_freq, compound_freq =education_table_info.compound_freq)
                education_results_content = {'saving_amount':round(education_results,2), 'interval':education_table_info.deposit_freq}
                print(education_results_content)
                print('in education')

            if marriage_table_info:
                calculations = Calculation(annual_rate = marriage_table_info.annual_rate, 
                                inflation = marriage_table_info.inflation)
                marriage_results = calculations.marriage(amount = marriage_table_info.amount,time = marriage_table_info.time,deposit_freq = marriage_table_info.deposit_freq, compound_freq =marriage_table_info.compound_freq)
                marriage_results_content = {'saving_amount':round(marriage_results,2), 'interval':marriage_table_info.deposit_freq}
                print(marriage_results_content)
                print('in marriage')




            if wealthcreation_table_info:
                calculations = Calculation(annual_rate = wealthcreation_table_info.annual_rate, 
                            inflation = wealthcreation_table_info.inflation)
                wealthcreation_results = calculations.wealth_creation(amount = wealthcreation_table_info.amount,payment = wealthcreation_table_info.payment,time = wealthcreation_table_info.time,deposit_freq = wealthcreation_table_info.deposit_freq, compound_freq =wealthcreation_table_info.compound_freq)
                df_wealth = wealthcreation_results['df_wealth']
                current_sip = wealthcreation_table_info.amount
                total_investment_gains = wealthcreation_results['total_investment_gains']
                future_value = wealthcreation_results['future_value']
                present_value = wealthcreation_results['present_value']
                wealthcreation_results_content = {'interval':wealthcreation_table_info.deposit_freq,'df_wealth':round(df_wealth,2), 'total_investment_gains':round(total_investment_gains,2), 'future_value':round(future_value,2),'present_value':round(present_value,2),'current_sip':current_sip}
                print(wealthcreation_results_content)
                print('in wealthcreation')

            if vacation_table_info:
                calculations = Calculation(annual_rate = vacation_table_info.annual_rate, 
                                            inflation = vacation_table_info.inflation)
                vacation_results = calculations.vacation(amount = vacation_table_info.amount,time = vacation_table_info.time,deposit_freq = vacation_table_info.deposit_freq, compound_freq =vacation_table_info.compound_freq)
                vacation_results_content = {'saving_amount':round(vacation_results,2), 'interval':vacation_table_info.deposit_freq}
                print(vacation_results_content)

            if housedownpayment_table_info:
                calculations = Calculation(annual_rate = housedownpayment_table_info.annual_rate, 
                                            inflation = housedownpayment_table_info.inflation)
                housedownpayment_results = calculations.house_down_payment(amount = housedownpayment_table_info.amount,down_payment_pct = housedownpayment_table_info.down_payment_pct,time = housedownpayment_table_info.time,deposit_freq = housedownpayment_table_info.deposit_freq, compound_freq =housedownpayment_table_info.compound_freq)            
                housedownpayment_results_content = {'saving_amount':round(housedownpayment_results,2), 'interval':housedownpayment_table_info.deposit_freq}
                print(housedownpayment_results_content)

            return render_template('dashboard.html',user = user,risk_analysis_results = risk_analysis_results,graphJSON = graphJSON,
                            education_results_content = education_results_content,education_table_info = education_table_info,
                            vacation_results_content = vacation_results_content, vacation_table_info = vacation_table_info,
                            housedownpayment_results_content = housedownpayment_results_content, housedownpayment_table_info = housedownpayment_table_info,
                            marriage_results_content = marriage_results_content, marriage_table_info = marriage_table_info,
                            wealthcreation_results_content = wealthcreation_results_content, wealthcreation_table_info = wealthcreation_table_info)



        else:
            return render_template('dashboard.html',user = user,risk_analysis_results = risk_analysis_results,graphJSON = graphJSON)

    return render_template('dashboard.html',user = user)


















    


