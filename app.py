from flask import Flask, render_template, request, redirect, session
import os

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == 'password':
            session['logged_in'] = True
            return redirect('/')
        return "Invalid credentials", 401
    return '''
    <form method="post" style="padding:40px;font-family:sans-serif;background:#1a072e;color:#0ff;">
        <h2>Login</h2>
        <input name="username" placeholder="Username" style="padding:10px;"/><br><br>
        <input type="password" name="password" placeholder="Password" style="padding:10px;"/><br><br>
        <button type="submit" style="padding:10px;background:#0ff;border:none;">Login</button>
    </form>
    '''

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
