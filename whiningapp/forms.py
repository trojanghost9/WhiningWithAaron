from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField, validators

class WineForm(Form):
    # List of wine color, used for dropdown menu - red or white
    wine_color = [(''), ('Red'), ('White')]

    # List of wine sweetness, used for dropdown menu - sweet, semi-dry, or dry
    wine_sweetness = [(''), ('Sweet'), ('Semi-dry'), ('Dry')]

    # Rank how the wine tasted, used for dropdown menu
    # May give error if don't have ie ('Ehh','Ehh') which is ('submitted', 'displayed')
    wine_taste = [(''), ('Hated It!'), ('Didnt like it'), ('Ehh'), ('Okay'), ('Good'), ('Really Good'), ('I will take a case')]

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