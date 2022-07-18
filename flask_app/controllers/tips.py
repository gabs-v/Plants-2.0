from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.tip import Tip
from flask_app.models.user import User

@app.route('/new/tip')
def new_tip():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('new_tip.html',user=User.get_by_id(data))

@app.route('/helpful/links')
def helpful_links():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('helpful_links.html',user=User.get_by_id(data))



@app.route('/create/tip',methods=['POST'])
def create_tip():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tip.validate_tip(request.form):
        return redirect('/new/tip')
    data = {
        "tip": request.form["tip"],
        "user_id": session["user_id"]
    }
    Tip.save(data)
    return redirect('/tip/all')
    

@app.route('/edit/tip/<int:id>')
def edit_tip(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id 
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_tip.html",edit=Tip.get_one(data),user=User.get_by_id(user_data))

@app.route('/update/tip/<int:id>',methods=['POST'])
def update_tip(id): 
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tip.validate_tip(request.form):
        return redirect('/new/tip')
    data = {
        "tip": request.form["tip"],
        "id": id
    }
    Tip.update(data)
    return redirect('/tip/all')

@app.route('/delete/tip/<int:id>')
def delete_sighting(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id 
    }
    Tip.delete(data)
    return redirect('/tip/all') 


@app.route('/tip/<int:id>')
def show_tip(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("details.html",tip=Tip.get_one(data),user=User.get_by_id(user_data))


@app.route('/tip/all')
def tip_all():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('show_tip.html',tips=Tip.get_all(),user=User.get_by_id(data))