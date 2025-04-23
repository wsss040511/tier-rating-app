from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # 这个会加载 templates 文件夹里的 index.html

if __name__ == '__main__':
    app.run(debug=True)
