from flask import Flask,jsonify
import csv
app=Flask(__name__)
all_articles=[]
with open("articles.csv",encoding="utf-8")as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        all_articles.append(i)

@app.route("/")
def app_():
    return "<h1>Article recommendation API,get request at /get-article,post request at /liked-article /disliked-article</h1>"
@app.route("/get-article")
def data_():
    return jsonify(all_articles[1])
app.run()