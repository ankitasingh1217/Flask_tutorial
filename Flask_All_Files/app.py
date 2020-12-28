from flask import (Flask, render_template, request, url_for, session, redirect, flash)
from Forms_Class import InfoForm1, InfoForm2


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

# @app.errorhandler(404)
# def page_not_found(e):
#     return render_template('404_try.html'), 404

#app.route('/')
@app.route('/home')
def fun1():
    return '<h1>Hello World</h1>'

@app.route('/TY')
def T_Y():
   return '<br><br><center><h1>Thank You</center></h1>'

@app.route('/home/<string:name>/<int:age>')
def fun2(name, age):
    return '<h1>Hello {name}.. you are {age}</h1>'


@app.route('/additon/<float:num1>/<float:num2>')
def add(num1, num2):
    return f'<h1>Addtion of {num1} & {num2} = {num1+num2}</h1>'


@app.route('/multiplication/<int:num1>/<int:num2>')
def mul(num1, num2):
    return f'<h1>Multiplication of {num1} & {num2} = {num1*num2}</h1>'


@app.route('/OG/<string:name>', methods=['GET'])
def only_get(name):
    return f'<h1>Hello {name}.. </br> This is ONLY GET REQUEST</h1>'


@app.route('/PaG/<string:name>', methods=['GET', 'POST'])
def Post_Get(name):
    return f'<h1>Hello {name}.. </br> This is POST & GET REQUEST </h1>'

# TEMPLATES STARTED


@app.route('/temp1_intro')
def f_temp1():
    return render_template('temp1.html')


@app.route('/temp2_intro/<string:FN>')
def f_temp2(FN):
    list_1 = ['Hello', 'Hi']
    dict_1 = {'Age': 23, 'Prof': 'Software Developer',
              'Hobbies': 'Football,Coding,Reading'}
    return render_template('temp2.html', name=FN, mydict=dict_1, mylist=list_1)


@app.route('/temp3_intro/<name>')
def f_temp3(name):
    return render_template('temp3.html', name=name)


@app.route('/temp4_intro')
def f_temp4():
    list_2 = ['Rohit', 'Ankita', 'Dishant']
    return render_template('temp4.html', names=list_2)


@app.route('/temp5_01')
def f_temp5_01():
    return render_template('temp5_01.html')


@app.route('/temp5_02')
def f_temp5_02():
    return render_template('temp5_02.html')


@app.route('/temp5_03', methods=['GET', 'POST'])
def f_temp5_03():
    return render_template('temp5_03.html')


@app.route('/temp6_01')
def f_temp6_01():
    return render_template('temp6_01.html')


@app.route('/temp6_02')
def f_temp6_02():
    return render_template('temp6_02.html')


@app.route('/temp6_03')
def f_temp6_03():
    return render_template('temp6_03.html')


@app.route('/temp6_04', methods=['GET', 'POST'])
def f_temp6_04():
    FN = request.form['yoo']
    LN = request.form['man']
    return render_template('temp6_04.html', first=FN, last=LN)

# ASSIGNMENT / TASK

@app.route('/temp7_01')
def f_temp7_01():
    return render_template('temp7_01.html')


@app.route('/temp7_02')
def f_temp7_02():
    return render_template('temp7_02.html')


@app.route('/temp7_03', methods=['GET', 'POST'])
def f_temp7_03():
    UN = request.form['username']
    # UN = request.args.get('username')

    lower_letter = False
    upper_letter = False
    num_end = False

    lower_letter = any(c.islower() for c in UN)
    upper_letter = any(c.isupper() for c in UN)
    num_end = UN[-1].isdigit()

    # Check if all are True.
    report = lower_letter and upper_letter and num_end

    return render_template('temp7_03.html', report=report, lower=lower_letter, upper=upper_letter, num_end=num_end)

# WTF FORMS
# https://wtforms.readthedocs.io/en/2.3.x/fields/

@app.route('/WTF1', methods=['GET', 'POST'])
def WTF_01():
    # Set the breed to a boolean False.
    # So we can use it in an if statement in the html.
    FN = False
    # Create instance of the form.
    form = InfoForm1()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.
        FN = form.FN.data
        # Reset the form's breed data to be False
        form.FN.data = ''
    return render_template('WTF1_01.html', form=form, FN=FN)


@app.route('/WTF2', methods=['GET', 'POST'])
def WTf_02():

    # Create instance of the form.
    form = InfoForm2()
    # If the form is valid on submission (we'll talk about validation next)
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['FN'] = form.FN.data
        session['VID'] = form.VID.data
        session['GEN'] = form.GEN.data
        session['BC'] = form.BC.data
        session['feedback'] = form.feedback.data

        return redirect(url_for("WTF_03"))

    return render_template('WTF1_02.html', form=form)


@app.route('/WTF3', methods=['GET', 'POST'])
def WTF_03():
    return render_template('WTF1_03.html')


@app.route('/WTF4', methods=['GET', 'POST'])
def WTF_04():
    # FLASING MESSAGES
    # Create instance of the form.
    form = InfoForm1()
    # If the form is valid on submission
    if form.validate_on_submit():
        # Grab the data from the breed on the form.

        session['FN'] = form.FN.data
        flash(f"You just changed your breed to: {session['FN']}")
        return redirect(url_for("WTF_04"))

    return render_template('WTF1_04.html', form=form)

# Object Relational Mapper (ORM) - 'peewee'





if __name__ == "__main__":
    app.run(debug=True)
