from flask import Flask,render_template, request , flash ,url_for ,session

app=Flask(__name__)

app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'

@app.route('/')
def home():
    
    return render_template('index.html' )


@app.route('/login')
def login():
     

     data=request.form

     return render_template('login.html' )


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

  
    if request.form =='POST':
            
                email = request.form.get('email')
                firstName = request.form.get ('firstName')
                password1 = request.form .get('password1')
                password2 = request.form .get('password2')  
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
    
    return f'lesson  {lesson_id }'
  
@app.route('/book2')
def book2():
    
    return render_template('book2.html'  )


@app.route('/book2/<int:lessons_id>')
def lessons(lessons_id):
    
    return f'lesson  {lessons_id }'
 


 
@app.route('/book3')
def book3():
    
    return render_template('book3.html'  )


@app.route('/book3/<int:lessons1_id>')
def lessons1(lessons_id):
    
    return f'lesson  {lessons_id }'




if __name__ =='__main__':
    app.run(debug= True )

