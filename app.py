import sys
import os
import marko
from flask import Flask, render_template

args = sys.argv

if len(args) < 2:
    print("Please provide a file name to parse")
    exit(1);

file_name = args[1]

if not os.path.isfile(file_name) or not file_name.lower().endswith('.md'):
    print("Please provide a valid file to parse")
    exit(1)


app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            contents = file.read()
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        exit(1)

    parsed_contents = marko.convert(contents)
    return render_template('index.html', contents=parsed_contents)

if __name__ == "__main__":
    app.run(debug=True)

