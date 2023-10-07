from flask import Flask, render_template, request
import cups
import os

app = Flask(__name__)
conn = cups.Connection(host="app-cups-container-1",port=631)

# printer_uri = "ipp://192.168.1.2/ipp/"
# conn = cups.IPPConnection(printer_uri)

# Replace 'Your_Printer_Name' with your printer's name
printer_name = 'Test'

# Define a route for the main page
@app.route('/')
def index():
    return render_template('./index.html')

# Define a route for handling form submissions
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get the value of the 'name' field from the form
        name = request.form['name']

        # Print the name
        print_to_printer(name, printer_name)

        return render_template('submit.html', name=name)
    
    
def print_to_printer(name, printer_name):
    

    # Create a temporary file with the name to print
    temp_file_path = '/tmp/print.txt'  # Adjust the path as needed
    with open(temp_file_path, 'w') as temp_file:
        temp_file.write(f'Name: {name}')

    # Print the file
    # job_id = conn.printFile(printer_uri, file_path, "Print Job", options)
    conn.printFile("Test", temp_file_path, 'Name Print Job', {'copies': '1'})

    os.remove(temp_file_path)


# def print_to_printer(name):
#     # Get default print options
#     options = conn.getDefault()

#     # Get printer information to obtain the URI
#     printers = conn.getPrinters()
    
#     if printer_name not in printers:
#         print(f"Printer '{printer_name}' not found.")
#         return

#     printer_info = printers[printer_name]
#     printer_uri = printer_info['device-uri']

#     # Create a temporary file with the name to print
#     temp_file_path = '/tmp/print.txt'  # Adjust the path as needed
#     with open(temp_file_path, 'w') as temp_file:
#         temp_file.write(f'Name: {name}')

#     # Print the file
#     conn.printFile(printer_name, temp_file_path, 'Name Print Job', {'copies': '1'})

#     # Optionally, you can remove the temporary file
#     os.remove(temp_file_path)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
