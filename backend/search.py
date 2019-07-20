from wtforms import Form, StringField, SelectField

class StockSearchForm(Form):
    search = StringField('')