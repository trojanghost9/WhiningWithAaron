from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators, SelectField

class WineForm(Form):
    # List of wine color, used for dropdown menu - red or white
    wine_color = [('', ''), ('Red', 'Red'), ('White', 'White')]

    # List of wine sweetness, used for dropdown menu - sweet, semi-dry, or dry
    wine_sweetness = [('', ''), ('Sweet', 'Sweet'), ('Semi-dry', 'Semi-dry'), ('Dry', 'Dry')]

    # Rank how the wine tasted, used for dropdown menu
    # May give error if don't have ie ('Ehh','Ehh') which is ('submitted', 'displayed')
    wine_taste = [('', ''), ('Hated It!', 'Hated It!'), ('Didnt like it', 'Didnt like it'),
                  ('Ehh', 'Ehh'), ('Okay', 'Okay'), ('Good', 'Good'),
                  ('Really Good', 'Really Good'), ('I will take a case', 'I will take a case')]

    color_selector = SelectField("Wine Color", choices=wine_color)

    sweetness_selector = SelectField("How Sweet", choices=wine_sweetness)

    taste_selector = SelectField("How much did I like it", choices=wine_taste)

    # Type of wine tasted.  Example Pinot
    wine_type = StringField('Type (Example: Pinot) *', [validators.DataRequired('Please enter the wine type.')])

    # Name of wine tasted.
    wine_name = StringField('Name *', [validators.DataRequired('Please enter the name of the wine.')])

    # Vintage of wine tasted.
    wine_vintage = StringField('Vintage *', [validators.DataRequired('Please enter the vintage of the wine.')])

    # Country of wine tasted.
    wine_country = StringField('Country *', [validators.DataRequired('Please enter the wines country of origin.')])

    # State of wine tasted.
    wine_state = StringField('State *', [validators.DataRequired('Please enter the wines state of origin.')])

    # Vineyard of wine tasted.
    wine_vineyard = StringField('Vineyard *', [validators.DataRequired('Please enter the wines vineyard  of origin.')])

    # Comments section.  Expandable text field to enter any comments.  Not required.
    wine_comments = TextAreaField('Any comments or additional notes?')

    # Submit form.
    submit = SubmitField('Submit My Review')