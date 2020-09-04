from flask import Flask,session, render_template, request, redirect, url_for


app=Flask(__name__)

app.config['SECRET_KEY']='pret'


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/set-background/<mode>')
def set_background(mode):
    session['mode']=mode
    return redirect(url_for('index'))


@app.route('/drop-session')
def drop_session():
    session.pop('mode',None)
    return redirect(url_for('index'))
    











if __name__=='__main__':
    app.run(debug=True)


