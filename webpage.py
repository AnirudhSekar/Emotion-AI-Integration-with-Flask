from flask import Flask, render_template, request, jsonify
from sentiment_detection_text import analyze_sentiment
from sentiment_detection_audio import analyze_audio
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def text_prompt():
    return render_template("index.html")
@app.route("/text", methods = ['POST', "GET"])
def text():
    if request.method == "GET":
        return render_template("text.html", score = "Neutral")
    if request.method == "POST":
        form_data = list(request.form.items())
        pos = round(analyze_sentiment(form_data[0][1])[1] * 100)
        neg = round(analyze_sentiment(form_data[0][1])[3] * 100)
        neu = round(analyze_sentiment(form_data[0][1])[2] * 100)
        compound = abs(round(analyze_sentiment(form_data[0][1])[4] * 100))
        return render_template("text.html", score =  analyze_sentiment(form_data[0][1])[0], positivity=pos, neutrality = neu, negativity = neg, compound=compound)
@app.route("/audio", methods = ["POST", "GET"])
async def upload_audio():
    
    if request.method == "POST":
        content = request.data
        with open('audio.wav', mode='wb') as f:
            f.write(content)
        actual_audio = await analyze_audio()
        results = analyze_sentiment(actual_audio)
        
        return jsonify({"SCORE":results[0], "POS":results[1],"NEG":results[3],"NEU":results[2], "COMPOUND":results[4]})
    return render_template("audio.html", score="Neutral")




if __name__ == "__main__":
    app.run(debug=True)