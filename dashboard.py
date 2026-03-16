from flask import Flask, render_template
import pandas as pd, os, csv

app = Flask(__name__)

file_path = 'cheating_log.csv'

# Check if the file exists before writing to it
if not os.path.exists(file_path):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Violation", "Details"])  # Example header row

@app.route('/')
def home():
    if os.path.getsize(file_path) == 0:
        data = []  # No data to show
    else:
        try:
            df = pd.read_csv(file_path)
            data = df.tail(20).to_dict(orient='records')
        except pd.errors.EmptyDataError:
            data = []  # Handle empty CSV safely
    return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
