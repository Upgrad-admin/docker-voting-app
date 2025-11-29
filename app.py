from flask import Flask, render_template, request
app = Flask(__name__)

votes = {"cats": 0, "dogs": 0}

@app.route('/', methods=['GET', 'POST'])
def home():
    global votes
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice in votes:
            votes[choice] += 1
    total = sum(votes.values())
    if total == 0:
        percentages = {"cats": 0, "dogs": 0}
    else:
        percentages = {k: round(v/total*100,2) for k,v in votes.items()}
    return render_template('index.html', votes=votes, percentages=percentages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
