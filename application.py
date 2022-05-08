
from flask import Flask,render_template,request
import pickle
import bz2file as bz2

app=Flask(__name__)

@app.route('/')
def index():
   return render_template("index.html")


@app.route('/output',methods=["POST"])
def predict():
    if request.method=='POST':
       formd=request.form["formd"]
       formm=request.form["formm"]
       formy=request.form["formy"]
       formc=request.form["formc"].upper()
       
       if formc=="INDIA":
         data=[[int(formd),int(formm),int(formy)]]
         lr=bz2.open("india.pkl.pbz2","rb") 
         sr= pickle.load(lr)
         prediction=sr.predict(data)[0]
         focu="Rupees/gram only"
         ind=float(prediction)
         ind=ind*10
         ind = "{:.2f}".format(ind)
         indi="Rupees/10grams "
         ind_rs=ind + " "+ indi

       if formc=="USA":
         data=[[int(formd),int(formm),int(formy)]]
         lr=bz2.open("us.pkl.pbz2","rb") 
         sr= pickle.load(lr)
         prediction=sr.predict(data)[0]
         focu="Euros/gram only"
         ind=float(prediction*76.52)
         ind = "{:.2f}".format(ind)
         ind=ind*10
         ind=str(ind)
         indi="Rupees/10grams "
         ind_rs=ind + " "+ indi

       if formc=="EUROPE":
         data=[[int(formd),int(formm),int(formy)]]
         lr=bz2.open("europe.pkl.pbz2","rb") 
         sr= pickle.load(lr)
         prediction=sr.predict(data)[0]
         focu="Euros/gram only"
         ind=float(prediction*80.68)
         ind=ind*10
         ind = "{:.2f}".format(ind)
         ind=str(ind)
         indi="Rupees/10grams "
         ind_rs=ind + " "+ indi

       if formc=="CANADA":
         data=[[int(formd),int(formm),int(formy)]]
         lr=bz2.open("canada.pkl.pbz2","rb") 
         sr= pickle.load(lr)
         prediction=sr.predict(data)[0]
         focu="Canadian dollars/gram only"
         ind=float(prediction*59.59)
         ind=ind*10
         ind = "{:.2f}".format(ind)
         ind=str(ind)
         indi="Rupees/10grams "
         ind_rs=ind + " "+ indi

       if formc=="AUSTRALIA":
         data=[[int(formd),int(formm),int(formy)]]
         lr=bz2.open("australia.pkl.pbz2","rb") 
         sr= pickle.load(lr)
         prediction=sr.predict(data)[0]
         focu="Australian dollars/gram only"
         ind=float(prediction*54.03)
         ind=ind*10
         ind = "{:.2f}".format(ind)
         ind=str(ind)
         indi="Rupees/10grams"
         ind_rs=ind + " "+ indi 
       


        
       if formm=="1":
          formm="JANUARY"
       elif formm=="2":
          formm="FEBRUARY"
       elif formm=="3":
          formm="MARCH"
       elif formm=="4":
          formm="APRIL"
       elif formm=="5":
          formm="MAY"
       elif formm=="6":
          formm="JUNE"
       elif formm=="7":
          formm="JULY"
       elif formm=="8":
          formm="AUGUST"
       elif formm=="9":
          formm="SEPTEMBER"
       elif formm=="10":
          formm="OCTOBER"
       elif formm=="11":
          formm="NOVEMBER"
       elif formm=="12":
          formm="DECEMBER"
     
             
      


    return render_template("output.html",formd=formd,formm=formm,formy=formy,formc=formc,predi=prediction,focu=focu,ind_rs=ind_rs)
          
@app.route('/',methods=["POST"])
def other():
   return render_template("index.html")


if __name__=='__main__':
    app.run(debug=True)
