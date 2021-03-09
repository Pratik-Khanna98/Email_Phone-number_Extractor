from flask import Flask, request, render_template, url_for
import re

app = Flask(__name__, template_folder="C:\\Data Science\\python\\python_projects\\Email_phone_extractor\\templates")

# pratik@gmail.com
# [\w\.-]+@[\w\.-]+
email_reg = re.compile(r"[\w\.-]+@[\w\.]+")
# 9029556862
# \d{10}
phone_num = re.compile(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        choice = request.form['taskoption']
        if choice == 'email':
            rawtext = request.form['rawtext']
            results = email_reg.findall(rawtext)
            num_of_results = len(results)
        if choice == 'phone':
            rawtext = request.form['rawtext']
            results = phone_num.findall(rawtext)
            num_of_results = len(results)
        if choice == 'email_phone':
            rawtext = request.form['rawtext']
            results = email_reg.findall(rawtext) + phone_num.findall(rawtext)
            num_of_results = len(results)

    return render_template('index.html', results=results, num_of_results=num_of_results)


# def about():


if __name__ == '__main__':
    app.run()
