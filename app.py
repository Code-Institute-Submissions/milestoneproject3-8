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
@app.route("/get_recipe")
def get_recipe():
    tasks = list(mongo.db.recipe.find())
    return render_template("recipe.html", tasks=tasks)


@app.route ("/search", methods=["GET", "POST"])   
def search():
    query=request.form.get("query")
    tasks = list(mongo.db.recipe.find({"$text": {"$search": query}}))
    return render_template("recipe.html", tasks=tasks)


@app.route("/add_recipe", methods = ["GET", "POST"]) 
def add_recipe():
    if request.method == "POST":
        task = {
            "course": request.form.get("course"),
            "dish": request.form.get("dish"),
            "ingredients": request.form.get("ingredients"),
            "prep": request.form.get("prep")
        }
        mongo.db.recipe.insert_one(task)
        flash ("Recipe Added!") 
        return redirect(url_for("get_recipe"))  

    categories = mongo.db.course.find().sort("course", 1)
    return render_template("add_recipe.html", categories=categories)  




@app.route ("/edit_recipe/<task_id>", methods=["GET", "POST"])
def edit_recipe(task_id):
    if request.method == "POST":
        submit = {
            "course": request.form.get("course"),
            "dish": request.form.get("dish"),
            "ingredients": request.form.get("ingredients"),
            "prep": request.form.get("prep")
        }
        mongo.db.recipe.update({"_id": ObjectId(task_id)}, submit)
        flash ("Recipe Updated!") 
        return redirect(url_for("get_recipe"))   


    
    task = mongo.db.recipe.find_one({"_id": ObjectId(task_id)})
    categories = mongo.db.course.find().sort("dish", 1)   
    return render_template("edit_recipe.html", task=task, categories=categories)    



@app.route ("/delete_recipe/<task_id>")
def delete_recipe(task_id):
    mongo.db.recipe.remove({"_id": ObjectId(task_id)})
    flash ("Recipe Deleted!")
    return redirect(url_for("get_recipe"))    




if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
            