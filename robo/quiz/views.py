from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from robo import db
from robo.models import Questions, QuestionsMarks, Results,RiskProfile, User, EducationTable, HouseDownPaymentTable, MarriageTable, WealthCreationTable,Results,VacationTable
from robo.quiz.forms import QuestionsForm
from robo.calculator.forms import EducationForm
from robo.maths.calculations import FinancialPlanner
import plotly
import plotly.express as px
import plotly.graph_objects as go
import json
from robo.maths.calculations import Calculation


quiz = Blueprint('quiz', __name__)
@quiz.route('/quiz_form', methods = ['GET', 'POST'])
def quiz_form():
    form = QuestionsForm()

    if form.validate_on_submit():
        print('hello, this is really great that you have printed first question')
        print(form.question1.data)
        print(form.question2.data)
        answers = Results(owner=current_user.get_id(), question1 = form.question1.data, question2 = form.question2.data, question3 = form.question3.data,
                         question4 = form.question4.data, question5 = form.question5.data, question6 = form.question6.data, question7 = form.question7.data,
                          question8 = form.question8.data, question9 = form.question9.data, question10 = form.question10.data, question11 = form.question11.data,
                           question12 = form.question12.data, question13 = form.question13.data, question14 = form.question14.data) 

        db.session.add(answers)
        db.session.commit()
        print('successfully commited')
        return redirect(url_for('quiz.quiz_analysis_page'))


    return render_template('quiz.html',form  =form)


# @quiz.route('/quiz_form/quiz_analysis')
# def quiz_analysis_page():
#     results = Results.query.filter_by(owner= current_user.get_id()).order_by(Results.id.desc()).first()
#     results_sum = (results.question1 + results.question2 + results.question3 +
#                     results.question4 + results.question5 + results.question6 +
#                     results.question7 + results.question8 + results.question9 +
#                     results.question10 + results.question11 + results.question12 +
#                     results.question13 + results.question14)

    
#     risk_analysis_results = FinancialPlanner(results_sum).asset_allocation()
    

#     user_riskprofile = RiskProfile(owner = current_user.get_id(),type_of_investor = risk_analysis_results['type_of_investor'], accumulation_return = round(risk_analysis_results['accumulation_return'],3), retirement_return = round(risk_analysis_results['retirement_return'],2))
#     db.session.add(user_riskprofile)
#     db.session.commit()

#     fig = go.Figure(go.Indicator(
#         domain = {'x': [0, 1], 'y': [0, 1]},
#         value = 70,
#         mode = "gauge+number",
#         title = {'text': "Riskness"},
#         gauge = {'axis': {'range': [None, 100]},}))

#     graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     risk_analysis_results =  RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()
#     education_table_info =  EducationTable.query.filter_by(owner= current_user.get_id()).order_by(EducationTable.id.desc()).first()
#     calculations = Calculation(
#                                 annual_rate = education_table_info.annual_rate, 
#                                 inflation = education_table_info.inflation
#                                 )
#     results = calculations.education(amount = education_table_info.amount,time = education_table_info.time,deposit_freq = education_table_info.deposit_freq, compound_freq =education_table_info.compound_freq)
#     print(results)
#     education_results = {'saving_amount':results, 'interval':education_table_info.deposit_freq}



    
#     return render_template('quizanalysis.html', results_sum = results_sum, risk_analysis_results = risk_analysis_results,graphJSON=graphJSON, education_results = education_results,education_table_info = education_table_info)

@quiz.route('/quiz_form/quiz_analysis')
def quiz_analysis_page():
    results = Results.query.filter_by(owner= current_user.get_id()).order_by(Results.id.desc()).first()
    results_sum = (results.question1 + results.question2 + results.question3 +
                    results.question4 + results.question5 + results.question6 +
                    results.question7 + results.question8 + results.question9 +
                    results.question10 + results.question11 + results.question12 +
                    results.question13 + results.question14)

    
    risk_analysis_results = FinancialPlanner(results_sum).asset_allocation()
    

    user_riskprofile = RiskProfile(owner = current_user.get_id(),type_of_investor = risk_analysis_results['type_of_investor'], accumulation_return = round(risk_analysis_results['accumulation_return'],3), retirement_return = round(risk_analysis_results['retirement_return'],2))
    db.session.add(user_riskprofile)
    db.session.commit()

    risk_analysis_results =  RiskProfile.query.filter_by(owner= current_user.get_id()).order_by(RiskProfile.id.desc()).first()

    return redirect(url_for('users.dashboard'))
















    


    

























@quiz.route('/create_quiz')
def create_quiz():
    question = 'Which of the following best describes your current stage of life?'
    a = 'Single with a few financial burdens. Ready to accumulate wealth for future short-term and long-term goals.'
    b = 'A couple without children. Preparing for the future by establishing a home. Expecting to have or already have a high purchase rate of household and consumer items.'
    c = 'Young family with a home. You have a mortgage and childcare costs and maintain only small cash balances.'
    d = "Mature family. You are in your peak earnings and your mortgage is under control. You both work and you may have or may not have children that are growing up or have left home. You're ready to start thinking about your retirement years."
    e = "Preparing for retirement. You own your home and have few financial burdens; you want to ensure you can afford a comfortable retirement."
    f = "Retired. You rely on existing funds and investments to maintain your lifestyle in retirement. You may already be receiving a government pension and/or superannuation pension.	"

    question1 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question1)
    db.session.commit()

    questionid = 1
    a = 5
    b = 3
    c = 1
    d = 5
    e = 3
    f = 2
    quesstionopt1 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt1)
    db.session.commit()

    question = 'How secure is your current and future income from sources such as salary, pensions or other investments?'
    a = 'Not secure'
    b = 'Somewhat secure'
    c = 'Fairly secure'
    d = 'Very secure'
    e = ''
    f = ''
    question2 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question2)
    db.session.commit()

    questionid = 2
    a = 1
    b = 3
    c = 5
    d = 7
    e = 0
    f = 0

    quesstionopt2 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt2)
    db.session.commit()


    #Question 3
    question = "What would you estimate your total annual income (before tax) to be from these sources?"
    a = "Less than Rs. 2,50,000"
    b = "Between Rs. 2,50,000 and Rs. 6,00,000"
    c = "Between Rs. 6,00,000 and Rs. 12,00,000"
    d = "Between Rs. 12,00,000 and Rs. 25,00,000"
    e = "Greater than Rs. 25,00,000"
    f = ""
    question3 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question3)
    db.session.commit()


    questionid = 3
    a = 1
    b = 3
    c = 5
    d = 7
    e = 9
    f = 0

    quesstionopt3 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt3)
    db.session.commit()


    #Question 4
    question = "What would you estimate your net worth to be, that is total assets (excluding the family home) less liabilities?"
    a = "Less than Rs. 5,00,000"
    b = "Between Rs. 5,00,000 and Rs. 10,00,000"
    c = "Between Rs. 10,00,000 and Rs. 50,00,000"
    d = "Between Rs. 50,00,000 and Rs. 2,00,00,000"
    e = "Greater than Rs. 2,00,00,000"
    f = ""
    question4 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question4)
    db.session.commit()


    questionid = 4
    a = 1
    b = 3
    c = 5
    d = 7
    e = 9
    f = 0

    quesstionopt4 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt4)
    db.session.commit()




    #Question 5
    question = "If you have borrowed before to invest, how would you rate your experience?"
    a = "It met my objectives for creating wealth"
    b = "I was generally comfortable with this strategy"
    c = "The potential for tax benefits was not worth the risk"
    d = "I experienced an investment loss due to borrowing"
    e = "N/A - I have never borrowed to invest before"
    f = ""

    question5 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question5)
    db.session.commit()

    questionid = 5
    a = 7
    b = 5
    c = 3
    d = 1
    e = 1
    f = 0

    quesstionopt5 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt5)
    db.session.commit()


    #Question 6
    question = "How familiar are you with investment matters?"
    a = "Not familiar at all with investment matters and feel uncomfortable with the complexity"
    b = "Not very familiar when it comes to investments"
    c = "Somewhat familiar. I don't fully understand investments, including the sharemarket"
    d = "Fairly familiar. I understand the various factors which influence investment performance"
    e = "Very familiar. I use research and other investment information to make decisions. I understand the various factors which influence investment performance"
    f = ""

    question6 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question6)
    db.session.commit()

    questionid = 6
    a = 1
    b = 2
    c = 3
    d = 5
    e = 7
    f = 0

    quesstionopt6 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt6)
    db.session.commit()


    #Question 7
    question = "What is the source of the funds you want to invest?"
    a = "Personal injury or compensation payment"
    b = "Change in family circumstances (divorce, widowed, etc)"
    c = "Inheritance or gift (including prize money)"
    d = "Superannuation and/or personal savings"
    e = ""
    f = ""

    question7 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question7)
    db.session.commit()


    questionid = 7
    a = 1
    b = 3
    c = 5
    d = 7
    e = 0
    f = 0

    quesstionopt7 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt7)
    db.session.commit()

    #Question 8
    question = "How long you would invest the majority of your money before you think you would need access to it? (Assuming you already have plans in place to meet short-term cashflow and/or emergencies)"
    a = "In 2 years or less"
    b = "Within 3 - 5 years"
    c = "Within 6 - 10 years"
    d = "Not for 10+ years"
    e = ""
    f = ""

    question8 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question8)
    db.session.commit()

    questionid = 8
    a = 1
    b = 3
    c = 5
    d = 7
    e = 0
    f = 0

    quesstionopt8 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt8)
    db.session.commit()

    #Question 9
    question = "In some instances, tax savings can be obtained from investments but this means taking on more risk. Which of the following statements best describes your goal for investing?"
    a = "Preferably guaranteed returns, before tax savings"
    b = "Stable, reliable returns, minimal tax savings"
    c = "Some variability in returns, some tax savings"
    d = "Moderate variability in returns, reasonable tax savings"
    e = "Unstable but potentially higher returns, maximize tax savings"
    f = ""

    question9 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question9)
    db.session.commit()

    questionid = 9
    a = 1
    b = 3
    c = 5
    d = 7
    e = 9
    f = 0

    quesstionopt9 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt9)
    db.session.commit()

    #Question 10

    question = "When considering your investments and making investment decisions, do you think about the impact of possible losses or possible gains?"
    a = "I am always concerned about possible losses"
    b = "I am somewhat concerned about possible losses"
    c = "I usually consider possible gains"
    d = "I always consider possible gains"
    e = ""
    f = ""

    question10 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question10)
    db.session.commit()

    questionid = 10
    a = 1
    b = 3
    c = 5
    d = 7
    e = 0
    f = 0

    quesstionopt10 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt10)
    db.session.commit()

    #Question 11
    question = "Assume you had an initial investment portfolio worth Rs. 10,00,000. If due to market conditions, your portfolio fell to Rs. 8,50,000 within a short period, say a month, would you:"
    a = "Sell all of the investments? You do not intend to take risks."
    b = "Sell a portion of your portfolio to cut your losses and reinvest into more secure investment assets?"
    c = "Hold the investment and sell nothing, expecting performance to improve?"
    d = "Invest more funds to lower your average investment price?"
    e = ""
    f = ""

    question11 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question11)
    db.session.commit()

    questionid = 11
    a = 1
    b = 3
    c = 5
    d = 7
    e = 0
    f = 0

    quesstionopt11 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt11)
    db.session.commit()


    #Question 12
    question = "If the value of your investments then fell to Rs. 6,00,000 over the next 12 months, would you:"
    a = "Sell all of the remaining investments?"
    b = "Sell a portion of the remaining investments?"
    c = "Hold your investments and sell nothing, expecting conditions to improve?"
    d = "Invest more funds. You can tolerate short-term losses in expectation of future growth?"
    e = ""
    f = ""

    question12 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question12)
    db.session.commit()

    questionid = 12
    a = 1
    b = 3
    c = 5
    d = 7
    e = 0
    f = 0

    quesstionopt12 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt12)
    db.session.commit()


    #Question 13
    question = "The table below shows the highest one year gain and the highest one year loss on five different hypothetical investments of Rs. 10,00,000. Given the potential gain or loss in any one year, where would you invest your money?"
    a = "Highest Gain: 1,16,000, Highest Loss: -21,000"
    b = "Highest Gain: 1,48,000, Highest Loss: -39,000"
    c = "Highest Gain: 2,05,000, Highest Loss: -77,000"
    d = "Highest Gain: 2,68,000, Highest Loss: -1,21,000"
    e = "Highest Gain: 3,15,000, Highest Loss: -1,54,000"
    f = ""

    question13 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question13)
    db.session.commit()

    questionid = 13
    a = 1
    b = 3
    c = 5
    d = 7
    e = 9
    f = 0

    quesstionopt13 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt13)
    db.session.commit()


    #Question 14
    question = "Which one of the following statements describes your feelings towards choosing an investment?"
    a = "I would prefer investments with little or no fluctuation in value and have a low degree of risk associated with them. I am willing to accept the lower return associated with these investments."
    b = "I prefer to diversify with a mix of investments that have an emphasis on low risk. I am happy to have a small proportion of the portfolio invested in assets that have a higher degree of risk in order to achieve a slightly higher return."
    c = "I prefer to have a spread of investments in a balanced portfolio."
    d = "I prefer to diversify my investments with an emphasis on more investments that have higher returns but still having a small amount of low risk investments."
    e = "I would select investments that have a higher degree of investment price fluctuation so that I can earn higher long-term returns."
    f = ""

    question14 = Questions(question = question, a = a,b = b, c = c, d = d, e = e, f = f)
    db.session.add(question14)
    db.session.commit()

    questionid = 14
    a = 1
    b = 3
    c = 5
    d = 7
    e = 9
    f = 0

    quesstionopt14 = QuestionsMarks(questionid = questionid, a = a, b=b, c=c, d=d, e=e, f=f)
    db.session.add(quesstionopt14)
    db.session.commit()





    print('hii')
    return render_template('index.html')







        


        