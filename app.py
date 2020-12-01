import os
from flask import Flask, flash, render_template, redirect, request, session, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"): 
    import env


app = Flask(__name__)  


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tasks")
def get_tasks():
    tasks = list(mongo.db.tasks.find())
    return render_template("tasks.html", tasks=tasks)
    

@app.route("/add_task", methods = ["GET", "POST"]) 
def add_task():
    if request.method == "POST":
        task = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description")
        }
        mongo.db.tasks.insert_one(task)
        flash ("Task Sucessfully Added") 
        return redirect(url_for("get_tasks"))  

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_task.html", categories=categories)  




@app.route ("/edit_task/<task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name"),
            "task_name": request.form.get("task_name"),
            "task_description": request.form.get("task_description")
        }
        mongo.db.tasks.update({"_id": ObjectId(task_id)}, submit)
        flash ("Task Sucessfully Updated")    


    
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)   
    return render_template("edit_task.html", task=task, categories=categories)    



@app.route ("/delete_task/<task_id>")
def delete_task(task_id):
    mongo.db.tasks.remove({"_id": ObjectId(task_id)})
    flash ("Task Successfully Deleted")
    return redirect(url_for("get_tasks"))    




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

            
    
    
