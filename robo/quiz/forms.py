from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, FloatField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError
from robo.models import Questions, QuestionsMarks


class QuestionsForm(FlaskForm):
    
    questions = Questions.query.all()
    questionmarks = QuestionsMarks.query.all()
    question1 = RadioField(label = questions[0].question,
                                choices = [(questionmarks[0].a, questions[0].a),
                                (questionmarks[0].b, questions[0].b),
                                (questionmarks[0].c, questions[0].c),
                                (questionmarks[0].d, questions[0].d),
                                (questionmarks[0].e, questions[0].e),
                                (questionmarks[0].f, questions[0].f)], validators = [DataRequired()])


    question2 = RadioField(label = questions[1].question,
                                choices = [(questionmarks[1].a, questions[1].a),
                                (questionmarks[1].b, questions[1].b),
                                (questionmarks[1].c, questions[1].c),
                                (questionmarks[1].d, questions[1].d)], validators = [DataRequired()])





    question3 = RadioField(label = questions[2].question,
                                choices = [(questionmarks[2].a, questions[2].a),
                                (questionmarks[2].b, questions[2].b),
                                (questionmarks[2].c, questions[2].c),
                                (questionmarks[2].d, questions[2].d),
                                (questionmarks[2].e, questions[2].e)], validators = [DataRequired()])



    
    question4 = RadioField(label = questions[3].question,
                                choices = [(questionmarks[3].a, questions[3].a),
                                (questionmarks[3].b, questions[3].b),
                                (questionmarks[3].c, questions[3].c),
                                (questionmarks[3].d, questions[3].d),
                                (questionmarks[3].e, questions[3].e)], validators = [DataRequired()])





    question5 = RadioField(label = questions[4].question,
                                choices = [(questionmarks[4].a, questions[4].a),
                                (questionmarks[4].b, questions[4].b),
                                (questionmarks[4].c, questions[4].c),
                                (questionmarks[4].d, questions[4].d),
                                (questionmarks[4].e, questions[4].e)], validators = [DataRequired()])





    question6 = RadioField(label = questions[5].question,
                                choices = [(questionmarks[5].a, questions[5].a),
                                (questionmarks[5].b, questions[5].b),
                                (questionmarks[5].c, questions[5].c),
                                (questionmarks[5].d, questions[5].d),
                                (questionmarks[5].e, questions[5].e)], validators = [DataRequired()])





    
    question7 = RadioField(label = questions[6].question,
                                choices = [(questionmarks[6].a, questions[6].a),
                                (questionmarks[6].b, questions[6].b),
                                (questionmarks[6].c, questions[6].c),
                                (questionmarks[6].d, questions[6].d)], validators = [DataRequired()])






    question8 = RadioField(label = questions[7].question,
                                choices = [(questionmarks[7].a, questions[7].a),
                                (questionmarks[7].b, questions[7].b),
                                (questionmarks[7].c, questions[7].c),
                                (questionmarks[7].d, questions[7].d)], validators = [DataRequired()])





    question9 = RadioField(label = questions[8].question,
                                choices = [(questionmarks[8].a, questions[8].a),
                                (questionmarks[8].b, questions[8].b),
                                (questionmarks[8].c, questions[8].c),
                                (questionmarks[8].d, questions[8].d),
                                (questionmarks[8].e, questions[8].e)], validators = [DataRequired()])



    question10 = RadioField(label = questions[9].question,
                                choices = [(questionmarks[9].a, questions[9].a),
                                (questionmarks[9].b, questions[9].b),
                                (questionmarks[9].c, questions[9].c),
                                (questionmarks[9].d, questions[9].d)], validators = [DataRequired()])



    question11 = RadioField(label = questions[10].question,
                                choices = [(questionmarks[10].a, questions[10].a),
                                (questionmarks[10].b, questions[10].b),
                                (questionmarks[10].c, questions[10].c),
                                (questionmarks[10].d, questions[10].d)], validators = [DataRequired()])




    question12 = RadioField(label = questions[11].question,
                                choices = [(questionmarks[11].a, questions[11].a),
                                (questionmarks[11].b, questions[11].b),
                                (questionmarks[11].c, questions[11].c),
                                (questionmarks[11].d, questions[11].d)], validators = [DataRequired()])





    question13 = RadioField(label = questions[12].question,
                                choices = [(questionmarks[12].a, questions[12].a),
                                (questionmarks[12].b, questions[12].b),
                                (questionmarks[12].c, questions[12].c),
                                (questionmarks[12].d, questions[12].d),
                                (questionmarks[12].e, questions[12].e)], validators = [DataRequired()])





    question14 = RadioField(label = questions[13].question,
                                choices = [(questionmarks[13].a, questions[13].a),
                                (questionmarks[13].b, questions[13].b),
                                (questionmarks[13].c, questions[13].c),
                                (questionmarks[13].d, questions[13].d),
                                (questionmarks[13].e, questions[13].e)], validators = [DataRequired()])






    submit = SubmitField('Submit')