from flask import Flask,render_template,request

import random

app =Flask(__name__)

responses=[
"Piss off,twat",
"Buy a guitar,not a brain",
"You're fucked anyway.",
"Punk's not dead,but your hopes are.",
"Go spit on Thatchers's grave.",
"Oi,Get a grip loser.",
"Sod off,romantic wanker.",
"Make chaos not babies",
"Anarchy begins at breakfast.",
 "Ask a real question, poser.",
 "Bleed glitter and beer.",
 "Sid died for your sins.",
 "Go cry to your mum.",
 "Reality is a fascist.",
 "You're just noise in the static.",
 "Dreams are for sober people.",
 "You’re late to your own funeral.",
 "Even Johnny Rotten wouldn't bother with that.",
"Dig a hole. Stay there.",
"Break something. That helps.",
"No gods, no answers, just me."
]
@app.route('/')
def intro():
    return render_template('intro.html')

@app.route('/lair')
def lair():
    return render_template('intro.html')

@app.route('/punkorac', methods=['GET', 'POST'])
def punkorac():
    answer = ""
    if request.method == 'POST':
        answer = random.choice(responses)
    return render_template("punkorac.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
