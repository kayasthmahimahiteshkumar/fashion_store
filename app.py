from flask import Flask, render_template, request, url_for, redirect, flash, g
import sqlite3

app = Flask(__name__)
DATABASE = 'store.db'
app.secret_key = 'your_super_secret_key_here'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    cur = get_db().cursor()
    cur.execute("SELECT * FROM products")
    products = cur.fetchall()
    return render_template('shop.html', products=products)

@app.route('/categories')
def categories():
    cur = get_db().cursor()
    cur.execute("SELECT DISTINCT category FROM products")
    categories = cur.fetchall()
    return render_template('categories.html', categories=categories)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    cur = get_db().cursor()
    cur.execute("SELECT * FROM products WHERE id = ?", (product_id,))
    product = cur.fetchone()
    return render_template('product_detail.html', product=product)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # You can save feedback to database here or just print/log for demo
        print(f"Feedback received: {name}, {email}, {message}")

        flash("Thank you for your feedback!", "success")
        return redirect(url_for('feedback'))

    return render_template('feedback.html')

if __name__ == '__main__':
    app.run(debug=True)
