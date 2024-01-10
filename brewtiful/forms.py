from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email
from wtforms import SelectField

countries = ['Australia', 'Austria', 'Burkina Faso', 'Comoros', 'Dominican Republic', 'Eswatini', 'Guyana', 'Guinea-Bissau', 'Iceland', 'Jordan', 'Kyrgyzstan', 'Lebanon', 'Liberia', 'Malawi', 'Marshall Islands', 'Mauritania', 'Micronesia', 'Mozambique', 'Nauru', 'Nicaragua', 'Niger', 'Papua New Guinea', 'Saint Lucia', 'Sierra Leone', 'Solomon Islands', 'South Sudan', 'Tajikistan', 'Togo', 'United Kingdom', 'Venezuela', 'Vietnam']

# form used in basket
class PayWithForm(FlaskForm):
    card_number = StringField("Card number", validators=[InputRequired()])
    expiry = StringField("Expiry", validators=[InputRequired()])
    cvv = StringField("CVV", validators=[InputRequired()])


class SendToForm(FlaskForm):
    firstname = StringField("Your first name", validators=[InputRequired()])
    surname = StringField("Your surname", validators=[InputRequired()])
    street = StringField("Your street address", validators=[InputRequired()])
    suburb = StringField("Your suburb", validators=[InputRequired()])
    country = SelectField("Select Country", validators=[InputRequired()])
    postcode = StringField("Your postcode", validators=[InputRequired()])
    email = StringField("Your email", validators=[InputRequired(), email()])
    phone = StringField("Your phone number", validators=[InputRequired()])
    submit = SubmitField("Confirm & Pay")

    def __init__(self, *args, **kwargs):
            super(SendToForm, self).__init__(*args, **kwargs)
            self.country.choices = [(country, country) for country in countries]