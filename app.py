from flask import Flask,render_template,request,redirect
from dbhelper import *

app = Flask(__name__)
upload_folder="static/images"
app.config["UPLOAD_FOLDER"]=upload_folder

@app.route("/upload",methods=['POST', 'GET'])
def upload():
    if request.method=="POST":
        file = request.files['webcam']
        idno = request.args.get("idno")
        lastname = request.args.get("lastname")
        firstname = request.args.get("firstname")
        course = request.args.get("course")
        level = request.args.get("level")
        imagename=upload_folder+"/"+idno+".jpg"
        file.save(imagename)
        okey: bool = add_record('students',idno=idno,lastname=lastname,firstname=firstname,course=course,level=level,image=imagename)
        return redirect("/")

@app.route("/")
def index():
    return render_template("index.html")
if __name__=="__main__":
    app.run(debug=True)