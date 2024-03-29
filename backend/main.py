from flask import Flask, flash, render_template, request, redirect
from search import StockSearchForm
import sqlite3

app = Flask(__name__)

### initialize database with table to store data if empty
conn = sqlite3.connect('database/database.db')
c = conn.cursor()
c.execute('''CREATE TABLE stocks
            (date text, symbol text, sentiment real, retweet_count real, favorite_count real''')

@app.route('/', methods=['GET', 'POST'])
def home():
    # PLANNED: Search bar with autocomplete for NASDAQ stocks
    #          Trending section for stocks with lots of activity
    #          About page
    search = StockSearchForm(request.form)
    if request.method == 'POST':
        return page(search)
    
    return render_template('main.html', form=search)

@app.route('/<stock>')
def page(stock):
    # PLANNED: Standard page for stock report   
    #          Include graph and blurb
    stock_string = stock.data['search']
    return 'Auxiliary ' + stock_string + ' Page Placeholder'

if __name__ == "__main__":
    app.run(debug=True)
