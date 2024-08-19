from flask import Flask,render_template, request , flash ,url_for ,session
from werkzeug.security import generate_password_hash , check_password_hash
from model import *
from flask_login import current_user , login_user,  logout_user , login_required


@app.route('/home')
@login_required
def home():
    return render_template('index.html',user=current_user )


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method =='POST':         
        email = request.form.get('email')
        password = request.form.get ('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password , password):
                flash(" welcome you are connected" , category='success')
                login_user(user,remember=True)
                return redirect(url_for('home'))
            else:
                flash("Invalide Password " , category='error')
        else:
            flash("Email invalide" , category='error')       

     
    return render_template('login.html',user=current_user )


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
    

@app.route('/propos')
def propos():
    return render_template('propos.html' ,user=current_user  )


@app.route('/cours')
def cours():
    return render_template('cours.html'  )


@app.route('/formation')
def formatiion():
    return render_template('formation.html',user=current_user  )


@app.route('/signup',methods=['GET','POST'])
def signup(): 
    if request.method =='POST':         
        email = request.form.get('email')
        firstName = request.form.get ('firstName')
        password = request.form .get('Password1')
        password2 = request.form .get('Password2')  

        user = User.query.filter_by(email=email).first()
        if user: 
            flash("this email already exists." , category='error')
        elif len(email) < 4 :  
            flash("very short email" , category='error')
            
        elif len(firstName) < 2:
            flash("first name must be greater than 2 characters.", category='error' ) 
        
        elif password != password2:
                flash("pasword don\'t match.", category='error' ) 
        elif len(password) < 7:
            flash("password  must be greater tha 7 characters.", category='error')
        else:
            nouvelle_Utilisateur = User(Nom=firstName,email=email,password=generate_password_hash(password))
            db.session.add(nouvelle_Utilisateur)
            db.session.commit()
            return redirect(url_for('login'))
            flash ('welcome ', category='succes')  
                

    return render_template("signup.html" ,user=current_user)
       
    
@app.route('/book1')
@login_required
def book1():
    
    return render_template('book1.html'  ,user=current_user )


@app.route('/book1/<int:lesson_id>')
def lesson(lesson_id):
    
    return f'lesson  {lesson_id }'
  
@app.route('/book2')
@login_required
def book2():
    
    return render_template('book2.html' ,user=current_user  )


@app.route('/book2/<int:lessons_id>')
def lessons(lessons_id):
    
    return f'lesson  {lessons_id }'
 


 
@app.route('/book3')
@login_required
def book3():
    
    return render_template('book3.html' ,user=current_user  )


@app.route('/book3/<int:lessons1_id>')
def lessons1(lessons_id):
    
    return f'lesson  {lessons_id }'




if __name__ =='__main__':
    app.run(debug= True )

