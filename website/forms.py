from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from website.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken. Please choose another one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is taken. Please choose another one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class BookingForm(FlaskForm):
    date = DateField('Select show date:', format='%Y-%m-%d')
    time = RadioField('Select show time:',
                      choices=[('09:00 AM', '09:00 AM'),
                               ('12:00 PM', '12:00 PM'),
                               ('03:00 PM', '03:00 PM'),
                               ('06:00 PM', '06:00 PM')])
    hall_name = SelectField('Select your hall:',
                       choices=[('Cinepolis: Forum Shantiniketan, Bengaluru', 'Cinepolis: Forum Shantiniketan, Bengaluru'),
                                ('INOX: Galleria Mall, Yelahanka', 'INOX: Galleria Mall, Yelahanka'),
                                ('INOX: Mantri Square, Malleshwaram', 'INOX: Mantri Square, Malleshwaram')])
    seat_type = SelectField('Choose seat type:',
                            choices=[('Normal', 'Normal: Rs.150'),
                                     ('Executive', 'Executive: Rs.200'),
                                     ('Premium', 'Premium: Rs.250')])
    no_of_seats = SelectField('Select number of seats:',
                              choices=[('1', '1'),
                                       ('2', '2'),
                                       ('3', '3'),
                                       ('4', '4'),
                                       ('5', '5'),
                                       ('6', '6'),
                                       ('7', '7'),
                                       ('8', '8'),
                                       ('9', '9'),
                                       ('10', '10')])
    submit = SubmitField('Proceed')
