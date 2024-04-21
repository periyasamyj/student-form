from flask import Flask,render_template,request,redirect,flash,g,session
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

app=Flask(__name__)
app.secret_key = '1a2b3c4d5e6d7g8h9i10'

# Create a new client and connect to the server
client = MongoClient(os.getenv("uri"), server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db_name="studentdatabase"
database=client[db_name]
collection_name="student_details"
registerdetails=database[collection_name]
databasedata=registerdetails.find()

@app.route('/')
def studentdetails():
    return render_template('index.html')

@app.route('/form/submit',methods=['GET','POST'])
def insertvalues():
    name=request.form.get("name")
    email=request.form.get("email")
    phone=request.form.get("phone")
    birthdate=request.form.get("birthdate")
    gender=request.form.get("gender")
    address1=request.form.get("address1")
    address2=request.form.get("address2")
    country=request.form.get("country")
    city=request.form.get("city")
    region=request.form.get("region")
    postal=request.form.get("postalcode")
    data={
        "name":name,
        "email":email,
        "phone":phone,
        "date of birth":birthdate,
        "gender":gender,
        "address 1":address1,
        "address 2":address2,
        "country":country,
        "city":city,
        "region":region,
        "postal":postal
    }
    registerdetails.insert_one(data)
    return render_template('success.html')
if __name__=='__main__':
    app.run()
