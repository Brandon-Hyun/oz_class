from flask import Flask, render_template

app = Flask(__name__)



# 루트 URLd에 사용자 목록을 보여주는 뷰 함수
@app.route("/")
def index():
    users = [{"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
    ]
    return render_template("index.html", users=users)


if __name__ == "__main__":
    app.run(debug=True)

