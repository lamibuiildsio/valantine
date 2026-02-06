from flask import Flask

app = Flask(__name__)

# This is the main page
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Be My Valentine?</title>
    <style>
        body { background-color: #ffb6c1; text-align: center; font-family: 'Arial', sans-serif; height: 100vh; overflow: hidden; display: flex; flex-direction: column; justify-content: center; align-items: center; }
        h1 { color: #d1001c; font-size: 50px; }
        .btn-container { position: relative; width: 100%; height: 200px; }
        button { padding: 15px 30px; font-size: 20px; border-radius: 50px; border: none; cursor: pointer; position: absolute; }
        #yesBtn { background-color: #ff4d6d; color: white; left: 40%; transform: translateX(-50%); }
        #noBtn { background-color: white; color: #ff4d6d; left: 60%; transform: translateX(-50%); transition: 0.1s; }
    </style>
</head>
<body>
    <h1>Will you be my Valentine? ❤️</h1>
    <div class="btn-container">
        <button id="yesBtn" onclick="document.body.innerHTML = '<h1>💖 I already knew that! 💖</h1>'">Yes</button>
        <button id="noBtn">No</button>
    </div>

    <script>
        const noBtn = document.getElementById('noBtn');
        const moveButton = () => {
            const x = Math.random() * (window.innerWidth - 100);
            const y = Math.random() * (window.innerHeight - 50);
            noBtn.style.position = 'fixed';
            noBtn.style.left = x + 'px';
            noBtn.style.top = y + 'px';
        };
        noBtn.addEventListener('mouseover', moveButton);
        noBtn.addEventListener('touchstart', moveButton);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return html_content

if __name__ == '__main__':
    app.run(debug=True, port=5000)