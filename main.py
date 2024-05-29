from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = URLField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Close Time e.g. 5:30PM', validators=[DataRequired()])
    cof_rate = StringField('Coffee Rating', validators=[DataRequired()])    
    wifi_rate = StringField('Wifi Strength Rating', validators=[DataRequired()])
    pow_rate = StringField('Power Socket Availability', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a', newline='', encoding='utf-8') as file:
            write_file = csv.writer(file)
            write_file.writerow([form.cafe.data, form.cafe_location.data, form.open_time.data, form.close_time.data, form.cof_rate.data, form.wifi_rate.data, form.pow_rate.data])
        # print(f"{form.cafe.data}\n{form.cafe_location.data}\n{form.open_time.data}\n{form.close_time.data}\n{form.cof_rate.data}\n{form.wifi_rate.data}\n{form.pow_rate.data}")
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form, data1=[{'coffee':'☕️'},{'coffee':'☕️☕️'},{'coffee':'☕️☕️☕️'},{'coffee':'☕️☕️☕️☕️'},{'coffee':'☕️☕️☕️☕️☕️'}], data2=[{'wifi':'✘'},{'wifi':'💪'},{'wifi':'💪💪'},{'wifi':'💪💪💪'},{'wifi':'💪💪💪💪'},{'wifi':'💪💪💪💪💪'}], data3=[{'power':'✘'},{'power':'🔌'},{'power':'🔌🔌'},{'power':'🔌🔌🔌'},{'power':'🔌🔌🔌🔌'},{'power':'🔌🔌🔌🔌🔌'}])


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
