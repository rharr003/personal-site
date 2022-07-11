from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, EmailField, TextAreaField
from wtforms.validators import DataRequired, URL, Email
from mailer import Mailer



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)



class ContactForm(FlaskForm):
    Name = StringField('Name:', validators=[DataRequired()])
    Email = EmailField("Email:", validators=[DataRequired(), Email()])
    Message = TextAreaField("Message:", validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/", methods=['GET', 'POST'])
def home():
    form = ContactForm()
    if request.method == "POST":
        if form.validate_on_submit():
            email = form.Email.data
            name = form.Name.data
            message = form.Message.data
            mailer = Mailer(receiver='7574776187')
            message_to_send = f"Name: {name}\n\nEmail Address: {email}\n\nMessage: {message}"
            mailer.sendmail(message_to_send)
            flash(f"Thanks {name.split(' ')[0]}! I will get back to you as soon as I can!")
            return redirect(url_for('home'))
    return render_template("index.html", form=form)




if __name__ == '__main__':
    app.run(debug=True)