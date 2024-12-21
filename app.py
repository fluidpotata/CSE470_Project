from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return '<h1>Welcome to the Volunteer and User Dashboard System</h1><p>Visit <a href="/resources">Resources Dashboard</a> to view resources.</p>'

# Route to display the Resources Dashboard
@app.route('/resources')
def resources_dashboard():
    # Connect to SQLite database
    conn = sqlite3.connect('resources.db')  # Replace 'resources.db' with your database file name
    cursor = conn.cursor()

    # Query to fetch resources
    cursor.execute('SELECT id, type, quantity, location FROM resources')
    resources = [
        {'id': row[0], 'type': row[1], 'quantity': row[2], 'location': row[3]}
        for row in cursor.fetchall()
    ]
    
    conn.close()

    # Render the resources_dashboard.html template
    return render_template('resources_dashboard.html', resources=resources)

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)




