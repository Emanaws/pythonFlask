from flask import Flask, render_template
app=Flask(__name__)
@app.route('/')

def home():

    return render_template('Home.html')

@app.route('/about')

def About():

    return render_template('about.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')



if __name__ == "__main__":
     app.config[ ' TEMPLATES_AUTO_RELOAD']=True
     app.run(debug= True,use_reloader=True)