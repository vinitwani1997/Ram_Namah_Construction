from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Dummy Property Data
properties = [
    {"id": 1, "name": "Luxury Villa", "location": "Mumbai", "price": 200000000, "display_price": "₹2 Cr", "type": "Villa", "image": "house1.jpg", "description": "A luxury villa in the heart of Mumbai."},
    {"id": 2, "name": "3BHK Apartment", "location": "Pune", "price": 80000000, "display_price": "₹80 Lakh", "type": "Apartment", "image": "house2.png", "description": "A modern 3BHK apartment with great amenities."},
    {"id": 3, "name": "Beach House", "location": "Goa", "price": 150000000, "display_price": "₹1.5 Cr", "type": "Villa", "image": "house3.jpg", "description": "A beautiful beach house with an ocean view."}
]

# Email Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'ramnamahconstructions@gmail.com'
app.config['MAIL_PASSWORD'] = 'tefo ewqt tqzo vfqm'  # Use Google App Password
app.config['MAIL_DEFAULT_SENDER'] = 'ramnamahconstructions@gmail.com'

mail = Mail(app)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Handle Contact Form Submission (AJAX Support)
@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        name = request.form['name']
        mobile = request.form['number']
        email = request.form['email']
        message = request.form['message']

        # Create Email Message
        msg = Message(subject="New Inquiry from Contact Form", recipients=["ramnamahconstructions@gmail.com"])
        msg.body = f"Name: {name}\nMobile: {mobile}\nEmail: {email}\nMessage: {message}"
        mail.send(msg)

        return jsonify({"success": True, "message": "Message sent successfully!"})  # Respond with JSON for popup

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# Properties Page
@app.route('/properties')
def properties_page():
    return render_template('properties.html', properties=properties)

# Property Details Page
@app.route('/property/<int:property_id>')
def property_details(property_id):
    property_data = next((p for p in properties if p["id"] == property_id), None)
    if property_data:
        return render_template('property_details.html', property=property_data)
    else:
        return "<h1>Property Not Found</h1>", 404

# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)
