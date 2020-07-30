from flask import Flask,render_template
app=Flask(__name__)

Employee = {"Fname":"Redwan","Lname":"Omer","Age":32}


@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/about')
def about():
    return render_template('about.html', Employeerec= Employee )

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/product')
def product():
    return render_template('product.html')


if __name__ == "__main__":
     app.config[ ' TEMPLATES_AUTO_RELOAD']=True
     app.run(debug= True,use_reloader=True)
