from flask import render_template, request, flash, redirect, url_for
from website.forms import RegistrationForm, LoginForm, BookingForm
from website.models import User, Booking
from website import app, db, bcrypt
from flask_login import login_user, current_user, logout_user


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/sign-up', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))
    return render_template('sign_up.html', title='Register', form=form)


movie = 1


@app.route('/helper', methods=['GET', 'POST'])
def helper():
    movieid = request.get_data().decode('utf-8')
    movie_list = {
        "1": "The Fallout",
        "2": "Gold",
        "3": "The 355",
        "4": "Dracula"
    }
    global movie
    movie = movie_list.get(movieid)
    return


@app.route('/book_now', methods=['GET', 'POST'])
def book_now():
    hall_name = None
    seat = {
        "Normal": 150,
        "Executive": 200,
        "Premium": 250
    }
    form = BookingForm()
    total_price = 0
    if form.validate_on_submit():
        hall_name = form.hall_name.data
        seat_price = int(seat.get(form.seat_type.data))
        print(form.seat_type.data)
        print(seat_price)
        total_price = seat_price*int(form.no_of_seats.data)
        print(total_price)
        ticket = Booking(movie_name=movie, hall_name=form.hall_name.data,
                         date=form.date.data, time=form.time.data,
                         no_of_seats=form.no_of_seats.data,
                         user_id=current_user.id, seat_type=form.seat_type.data,
                         total_price=total_price)
        db.session.add(ticket)
        db.session.commit()
        flash(f'Ticket booked for {form.hall_name.data}!', 'success')  # 'for {form.username.data}'

    return render_template("book_now.html", form=form, hall_name=hall_name, user=current_user,
                           movie=movie, total_price=total_price, date=form.date.data,
                           time=form.time.data, no_of_seats=form.no_of_seats.data,
                           seat_type=form.seat_type.data)


@app.route('/my-bookings')
def my_bookings():
    return render_template("my_bookings.html", user=current_user)
