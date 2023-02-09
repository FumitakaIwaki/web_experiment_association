# AWS EC2へのssh接続
# ssh -i ~/.ssh/iwaki.pem ec2-user@  {Public IPv4 DNS}
# 起動(本番)
# waitress-serve --port=5000 app:app

from flask import Flask, render_template, request, jsonify
import pandas as pd
 
app = Flask(__name__)
# カウンター
CNT = -1

# 導入画面
@app.route("/")
def index():
    return render_template('header.html')
 
# 実験画面
@app.route("/experiment")
def experiment():
    global CNT
    CNT+=1

    return render_template('index.html', cnt=CNT)

# データポスト
@app.route("/post_data", methods=['GET', 'POST'])
def post():
    data = request.get_json()
    res_df = pd.DataFrame(data, index=[data['counter']])
    res_df.to_csv(f"data/res{data['counter']}.csv", index=False)

    return jsonify(data)

# 終了画面（承認されなかった場合）
@app.route("/finish", methods=['GET', 'POST'])
def fin():
    return render_template('finish.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)