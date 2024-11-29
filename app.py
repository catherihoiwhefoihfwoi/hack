





from flask import Flask, render_template, redirect, url_for, request, session


app = Flask(__name__)
app.secret_key = "hello"

status = {"good": 0, "bad": 0}

@app.route('/')
def home():
  return render_template('1home.html')

@app.route('/button_click', methods=['POST'])
def button_click():
  return 'Button clicked'

@app.route('/about_page')
def about():
  return render_template('about_page.html')

@app.route('/name', methods=["GET","POST"])
def name():
  if request.method == 'POST':
    session['user'] = request.form.get('firstName')
    return render_template('intro.html', userName = session['user'])
  else:
    return render_template('name.html')

@app.route('/intro')
def intro():
  return render_template('intro.html')

@app.route('/test')
def test():
  return redirect(url_for('question5N'))

#Questions
#1
@app.route('/question1', methods=["GET", "POST"])
def question1():
    return render_template('question1.html', userName = session['user'])

  
#2
@app.route('/question2Y', methods=["GET", "POST"])
def question2Y():
  if request.method == 'POST':
    if request.form.get("choice") == 'I am a big fan of jelly and jams.':
        status["good"] += 1
        return redirect(url_for('question3Y'))
    if request.form.get("choice") == 'I am a fiend for cookies.':
        status["bad"] += 1
        return redirect(url_for('question3N'))
  else:
    return render_template('question2Y.html')

@app.route('/question2N', methods=["GET", "POST"])
def question2N():
  # print("question2N",status)
  # if request.method == 'POST':
  #   if request.form.get("choice") == 'I am a big fan of jelly and jams.':
  #       status["good"] += 1
  #       return redirect(url_for('question3Y'))
  #   if request.form.get("choice") == 'I am a fiend for cookies.':
  #       status["bad"] += 1
  #       return redirect(url_for('question3N'))
  # else: 
    return render_template('question2N.html', yay = status["good"], nay =  status["bad"])

#3
@app.route('/question3N', methods=["GET", "POST"])
def question3N():
  if request.method == 'POST':
    if request.form.get("choice") == "Night owl, definitely. Nothing beats the view of the moon as I pour toxic waste into my neighbour's yard.":
        status["good"] += 1
        return redirect(url_for('question4Y'))
    if request.form.get("choice") == "Early bird for sure. I love feeling superior to other people because I wake up at 5AM.":
        status["bad"] += 1
        return redirect(url_for('question4N'))
  else:
    return render_template('question3N.html')

@app.route('/question3Y', methods=["GET", "POST"])
def question3Y():
  if request.method == 'POST':
    if request.form.get("choice") == "Night owl, definitely. Nothing beats the view of the moon as I pour toxic waste into my neighbour's yard.":
        status["good"] += 1
        return redirect(url_for('question4Y'))
    if request.form.get("choice") == "Early bird for sure. I love feeling superior to other people because I wake up at 5AM.":
        status["bad"] += 1
        return redirect(url_for('question4N'))
  else:
    return render_template('question3Y.html')

#4
@app.route('/question4N', methods=["GET", "POST"])
def question4N():
  if request.method == 'POST':
    if request.form.get("choice") == "Private jet to Cancun. Sipping on coconuts, tanning at the beach. Knocking over people's sand castles.":
        status["good"] += 1
        
        return redirect(url_for('question5Y'))
    if request.form.get("choice") == "Head to the ski resort. When I am tired, I go over to the beginner section to watch them trip and fall.":
        status["bad"] += 1
        return redirect(url_for('question5N'))
  else:
    return render_template('question4N.html')

@app.route('/question4Y', methods=["GET", "POST"])
def question4Y():
  if request.method == 'POST':
    if request.form.get("choice") == "Private jet to Cancun. Sipping on coconuts, tanning at the beach. Knocking over people's sand castles.":
        status["good"] += 1
        return redirect(url_for('question5Y'))
    if request.form.get("choice") == "Head to the ski resort. When I am tired, I go over to the beginner section to watch them trip and fall.":
        status["bad"] += 1
        return redirect(url_for('question5N'))
  else:
    return render_template('question4Y.html')

#5
@app.route('/question5N', methods=["GET", "POST"])
def question5N():
  if request.method == 'POST':
    if request.form.get("choice") == 'Probably as the Monarch of England after I forcefully seize the throne.':
        status["good"] += 1
        return redirect(url_for('question6Y'))
    if request.form.get("choice") == "Probably locked up in prison for tax fraud.":
        status["bad"] += 1
        return redirect(url_for('question6N'))
  else:
    return render_template('question5N.html')

@app.route('/question5Y', methods=["GET", "POST"])
def question5Y():
  if request.method == 'POST':
    if request.form.get("choice") == 'Probably as the Monarch of England after I forcefully seize the throne.':
        status["good"] += 1
        return redirect(url_for('question6Y'))
    if request.form.get("choice") == "Probably locked up in prison for tax fraud.":
        status["bad"] += 1
        return redirect(url_for('question6N'))
  else:
    return render_template('question5Y.html')

#6
@app.route('/question6N', methods=["GET", "POST"])
def question6N():
  if request.method == 'POST':
    if request.form.get("choice") == "* You take out your tranquiliser dart gun and shoot Vector *":
        status["good"] += 1
        return redirect(url_for('question7Y'))
    if request.form.get("choice") == "Yeah, you're right. Why would they let you in, Vector?":
        status["bad"] += 1
        return redirect(url_for('question7N'))
  else:
    return render_template('question6N.html')

@app.route('/question6Y', methods=["GET", "POST"])
def question6Y():
  if request.method == 'POST':
    if request.form.get("choice") == "* You take out your tranquiliser dart gun and shoot Vector *":
        status["good"] += 1
        return redirect(url_for('question7Y'))
    if request.form.get("choice") == "Yeah, you're right. Why would they let you in, Vector?":
        status["bad"] += 1
        return redirect(url_for('question7N'))
  else:
    return render_template('question6Y.html')

#7
@app.route('/question7N', methods=["GET", "POST"])
def question7N():
  if request.method == 'POST':
    if request.form.get("choice") == "How do you get your head so shiny?":
        status["good"] += 1
        return redirect(url_for('question8Y'))
    if request.form.get("choice") == "Have you ever thought about wearing a wig?":
        status["bad"] += 1
        return redirect(url_for('question8N'))
  else:
    return render_template('question7N.html')

@app.route('/question7Y', methods=["GET", "POST"])
def question7Y():
  if request.method == 'POST':
    if request.form.get("choice") == "How do you get your head so shiny?":
        status["good"] += 1
        return redirect(url_for('question8Y'))
    if request.form.get("choice") == "Have you ever thought about wearing a wig?":
        status["bad"] += 1
        return redirect(url_for('question8N'))
  else:
    return render_template('question7Y.html')

#8
@app.route('/question8N', methods=["GET", "POST"])
def question8N():
  if request.method == 'POST':
    if status["good"] > status["bad"]:
        return redirect(url_for('good_ending'))
    if status["bad"] > status["good"]:
        return redirect(url_for('bad_ending'))
  else:
    return render_template('question8N.html')

@app.route('/question8Y', methods=["GET", "POST"])
def question8Y():
  if request.method == 'POST':
    if status["good"] > status["bad"]:
        return redirect(url_for('good_ending'))
    if status["bad"] > status["good"]:
        return redirect(url_for('bad_ending'))
  else:
    return render_template('question8Y.html')

@app.route('/good_ending')
def good_ending():
  return render_template('good_ending.html')

@app.route('/bad_ending')
def bad_ending():
  return render_template('bad_ending.html')

