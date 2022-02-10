from datetime import datetime
from website import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    bookings = db.relationship('Booking', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Booking(db.Model):
    ticket_no = db.Column(db.Integer, primary_key=True)
    movie_name = db.Column(db.String(100), nullable=False)
    hall_name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(10), nullable=True, default=datetime.utcnow)
    time = db.Column(db.String(10), nullable=True, default=datetime.utcnow)
    seat_type = db.Column(db.String(100), nullable=False)
    no_of_seats = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Ticket('{self.ticket_no}', '{self.movie_name}', {self.hall_name}, {self.date}, {self.time}, {self.seat_type}, {self.no_of_seats}, {self.total_price}) "