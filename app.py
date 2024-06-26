from flask import Flask,render_template, request , flash ,url_for

app=Flask(__name__)
app.secret_key="MyKey"

@app.route('/')
def home():
    flash("Bienvenue ")
    return render_template('index.html' )


@app.route('/se connecter')
def seConnecter():

    return render_template('se Connecter.html' )


@app.route('/propos')
def propos():
    return render_template('propos.html'  )


@app.route('/cours')
def cours():
    return render_template('cours.html'  )


@app.route('/formation')
def formatiion():
    return render_template('formation.html' )


@app.route('/signup',methods=['GET','POST'])
def signup(): 
        flash('Welcome to the signup Page,' , category='error')
        if request.form =='POST':
                email = request.form('email')
                firstName = request.form ('firstName')
                password1 = request.form('password1')
                password2 = request.form ('password2')  
                if len(email) < 4 :  
                    flash("Votre Email Et Deja En Cours")
                   
                elif len(firstName) < 2:
                    flash("firstname must be greater than 2 characters.", category='error') 
                
                elif password1 != password2:
                        flash("pasword don\'t match.", category='error' ) 
                elif len(password1) < 7:
                    flash("password  must be greater tha 7 characters.", category='error')
                else:
                    flash ('welcome ', category='error')  
        return render_template("signup.html")
       
    
@app.route('/book1')
def book1():
    return render_template('book1.html'  )


@app.route('/book1/<int:lesson_id>')
def lesson(lesson_id):
    
    return f'lesson {lesson_id}'

if __name__ =='__main__':
    app.run(debug= True )

