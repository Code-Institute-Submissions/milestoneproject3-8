# Pennsylvania Dutch Recipe Swap

My third Milestone project is called KOCHBUCH, a site where viewers can look at a collection of Pennsylvania Dutch cooking recipes, and if they want leave some recipes of their own.  This site features Python's web framework, Flask.

## UX

The target audience of this project are people who are in search of recipes of Pennsylvania Dutch cooking, a Pennsylvania German-based cusine which specializes in folk recipes and mayonnaise-blended salads.  This is the only recipe-swapping web site of this cusine. 

The Pennsylvania Dutch Recipe Swap is essentially a database, using the Mongo DB Atlas.  The project offers the audience use the CRUD operations, the four operations that can be used in a database. The user can easily create, read, update or delete the contents of the recipe.

The user can easily search the website for any named-item in the recipe, as well as the name of the dish or which of the four meal-courses it is: Entree, side dish, salad, or desert.

The design of the site makes both the reading of recipes and the entering recipes both easy and simple to do.



## Features

The viewers have come to the Pennsylvania Dutch Recipe Swap, a website where they may read and exchange recipes from Pennsylvania's Pennsylvania Dutch culture.  First, the viewers will see that the site is sponsered by a local cooking supply company.  Then they will see the collection of recipes, where each recipe is made up of four different entries:  The course, which is either an entree, side dish, salad or desert; the name of the dish; the ingredients; and, finally, how to prepare the dish.  On the face of each recipe, viewers will see the name of the dish, and two buttons, the Update button, which will let them change the recipe, and the Delete button, which will eliminate the recipe.  The Update button will take the viewers to another page, the Update page, where the recipe is displayed.  They may change the recipe and then save it.  The recipe will reappear on the Home page.  Lets go back to the Home page, where, underneath the collection of recipes, viewers will see a Search bar, with which they can find any recipe, food item or name of meal course.  The last page is the Add Recipe page, which can be found by hitting the Add Recipe button on the Nav Bar.  There viewers will see a big field with four different entries, which looks the same as the Update recipe page, where they can leave a recipe and save it.

## Technologies

1. HTML
2. CSS
3. JavaScript
4. Python
5. Mongo DB Atlas
6. Heroku Cloud Platform
7. Materialize Library
8. Flask
9. Pymongo
10. Jinja

## Testing

The HTML and CSS were checked by W3School's code validator to see if they were correct. All of the code was tested with DevTools. The site was viewed on devices of several different sizes to ensure that the code behaved responsively.


## Deployment to Heroku

1. Login to Heroku.
2. Click on New button.
3. Click on Create New App and name it.
4. Choose geographical region.
5. Go to Github Terminal and create a requirements.txt by running the command pip3 freeze --local > requirements.txt.
6. Create Procfile by running the command echo web: python app.py > Procfile.
7. Push each file to the staging area.
8. Go back to Heroku and click on Deploy.
9. Go to Deployment Method and click on Connect to Github.
10. Add the repository name and click on Search.
11. Once it finds the repository click on Connect.
12. Click on Settings and then Reveal Config Vars.
13. In Config Vars enter the file env.py values.
14. Go back to Deploy and click on Enable Automatic Deploys.
15. Click on Deploy Branch and wait for the message that the app was deployed.
16. Click on View to launch the Deployed app. 

## Wireframes

I used [Balsamiq](https://balsamiq.com) to create three different wireframes-each for a different screen size-which show how the project's appearance was initially conceived.

-[Wireframes in PDF](/workspace/milestoneproject3/static/wireframes/wireframe1.pdf)


## Credit

Much of my projects' technology came from Code Institute's Task Manager mini-project.