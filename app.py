from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# --- 1. Flask Routing for the Homepage ---
# This route will render the index.html template when someone visits the main URL ('/').
@app.route('/')
def home():
    """Renders the homepage."""
    return render_template('index.html')

# --- 2. Flask Routing for the Contact Form Submission ---
# This route will handle the data submitted from the contact form.
# It's set to accept POST requests.
@app.route('/contact', methods=['POST'])
def contact():
    """Handles the contact form submission."""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For this example, we'll just print the data to the console.
        # In a real application, you might send an email or save it to a database.
        print(f"Contact Form Submission:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        # You can return a simple confirmation message or redirect to a 'thank you' page.
        return "Thank you for your message! I will get back to you soon."

# This line allows you to run the app directly using 'python app.py'
if __name__ == '__main__':
    app.run(debug=True)
