
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'


users = {}

cart = []

books = [
    {"id": 1, "title": "Black Night", "author": "Youssef", "price": "$19.99", "description": "A gripping psychological thriller about a protagonist trapped in a city of secrets and danger.", "photo": "book-1.png"},
    {"id": 2, "title": "About The First Night", "author": "Mustafa", "price": "$15.99", "description": "A captivating tale of new beginnings, following a protagonist embarking on a journey of self-discovery.", "photo": "book-2.png"},
    {"id": 3, "title": "Open The Sky", "author": "Mohamed", "price": "$15.99", "description": "A journey through the mysteries of the cosmos, exploring the infinite possibilities that lie beyond Earth's atmosphere.", "photo": "book-3.png"},
    {"id": 4, "title": "Book", "author": "Deyaa", "price": "$15.99", "description": "A comprehensive guide to the wonders of science, breaking down complex concepts into fascinating discoveries.", "photo": "book-4.png"},
    {"id": 5, "title": "The Big Book Of Science", "author": "Mohamed", "price": "$15.99", "description": "A poetic narrative capturing the beauty and freedom of life from above, where the sky meets endless horizons.", "photo": "book-5.png"},
    {"id": 6, "title": "By The Air", "author": "Hosam", "price": "$15.99", "description": "A poetic narrative capturing the beauty and freedom of life from above, where the sky meets endless horizons.", "photo": "book-6.png"},
    {"id": 7, "title": "Murdering Last Year", "author": "Omar", "price": "$15.99", "description": "A gripping murder mystery that unravels the secrets of a chilling case with unexpected twists.", "photo": "book-7.png"},
    {"id": 8, "title": "The Workout", "author": "Ewis", "price": "$15.99", "description": "A practical guide to building fitness habits, with exercises and tips for a healthier lifestyle.", "photo": "book-8.png"},
    {"id": 9, "title": "Self Care", "author": "Ahmed", "price": "$15.99", "description": "A heartfelt manual on prioritizing mental and physical well-being, filled with actionable advice and self-love practices.", "photo": "book-9.png"},
    {"id": 10, "title": "Welcome To Space", "author": "Tamer", "price": "$15.99", "description": "An engaging exploration of the universe, perfect for anyone curious about stars, planets, and space travel.", "photo": "book-10.png"},
    {"id": 11, "title": "Monsoon", "author": "Ismail", "price": "$15.99", "description": "A vivid tale set in the monsoon season, blending drama and romance with the raw power of nature.", "photo": "book-11.png"},
    {"id": 12, "title": "Every Thing You Never", "author": "Shahd", "price": "$15.99", "description": "A thought-provoking book that delves into forgotten histories and untold stories.", "photo": "book-12.png"},
    {"id": 13, "title": "Graphic Design School", "author": "Amira", "price": "$15.99", "description": "A comprehensive guide for aspiring designers, covering principles, tools, and techniques to master the craft.", "photo": "book-13.png"},
    {"id": 14, "title": "Hungry?", "author": "Rana", "price": "$15.99", "description": "A fun and practical cookbook for quick and delicious meals, perfect for food lovers on the go.", "photo": "book-14.png"},
    {"id": 15, "title": "Design", "author": "Yamour", "price": "$15.99", "description": "A deep dive into the world of design, highlighting iconic projects and innovative ideas.", "photo": "book-15.png"},
    {"id": 16, "title": "World News", "author": "Zizo", "price": "$15.99", "description": "A compelling account of global events, providing insights into politics, culture, and humanity’s shared journey.", "photo": "book-16.png"},

]

@app.route('/')
def home():
    if 'username' in session:
        
        return render_template('home.html', username=session['username'])
    
    return render_template('home.html')  

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        
        if username in users:
            flash('Username already exists. Please choose another.', 'error')
        else:
            
            users[username] = password
            flash('Signup successful! Please log in.', 'success')

            
            #return redirect(url_for('index'))   
    
    return render_template('index.html')  

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        
        if username in users and users[username] == password:
            session['username'] = username  
            flash('Login successful!', 'success')
            return redirect(url_for('home')) 
        else:
            flash('Invalid username or password.', 'error')  
    
    return render_template('index.html')  



@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/shop')
def shop():
    return render_template('shop.html', books=books)

@app.route('/book/<int:book_id>')
def book_details(book_id):
    # Find the book by ID
    book = next((book for book in books if book["id"] == book_id), None)
    if not book:
        return "Book not found!", 404
    return render_template('book_details.html', book=book)

# Add to Cart route
@app.route('/add_to_cart/<int:book_id>', methods=['GET'])
def add_to_cart(book_id):
    # Find the book by ID
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        cart.append(book)  # Add the book to the cart
        flash(f'{book["title"]} has been added to your cart!', 'success')
    else:
        flash('Book not found!', 'error')
    return redirect(url_for('book_details', book_id=book_id))

@app.route('/cart')
def view_cart():
    return render_template('cart.html', cart=cart)


@app.route('/cart')
def cart_page():
    total_price = sum(float(book["price"].strip('$')) for book in cart)
    return render_template('cart.html', cart=cart, total_price=total_price)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if not cart:
        flash('Your cart is empty!', 'error')
        return redirect(url_for('shop'))
    
    # Calculate total price
    total_price = sum(float(book["price"].strip('$')) for book in cart)

    if request.method == 'POST':
        # Handle payment information here (for simplicity, we will just show a success message)
        name = request.form.get('name')
        address = request.form.get('address')
        payment_method = request.form.get('payment_method')

        # Normally, you'd process the payment here and clear the cart after a successful purchase.
        cart.clear()  # Empty the cart after checkout
        flash('Your order has been placed successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('checkout.html', cart=cart, total_price=total_price)


@app.route('/logout')
def logout():
    session.pop('username', None)  
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))  

if __name__ == '__main__':
    app.run(debug=True)





