# Project name
Cold Meats

# Project description
*Importance of the project*

Introducing the Django project I built during my bootcamp 🚀. I'm thrilled to share this hands-on experience where I delved into the world of web development and created a dynamic platform that's both engaging and user-friendly. The project features database-driven components that require user login and authentication for access, making it a secure and personalized space for meat enthusiasts.

🧑‍💻Here's what you can explore on the Cold Meats Website:

[1]Catalogue: Dive into a mouthwatering assortment of cold meats, all neatly categorised and easily accessible once you log in.

[2] Blog: Stay updated with the latest meaty news, recipes, and industry insights in our blog section.

[3] Polls: Cast your votes and see what fellow meat aficionados have to say about your favorite cuts and flavours.

*What the project does*

+ Create a Django application that can be used by the business Cold Meats and its clientelle. The program should allow the user to:
    + register a new user
    + login a user    
    + view the catalogue of cold meats
    + contact the business to place an order
	+ add new blog posts
	+ view all blog posts
    + subscribe to the blog 
	+ vote on polls relevant to the business
	
+ Create a database for the blog posts and polls
+ Add blog entries
+ Add polls and choices for each poll

# Installation section
*Tell other users how to install your project locally*

Outline the steps necessary to build and run your application with venv and Docker:

1. Open the Command Prompt
1. Create a Virtual Environment:
    + in Command Prompt (powershell)
    + create a folder for new virtual env: mkdir Virtual_env
    + cd Virtual_env
    + create virtual env: virtualenv my_django
    + you will see Scripts in my_django
    + change to Command Prompt (admin) 
    
1. Activate the Virtual Environment:
    + On Windows (Command Prompt):
        + cd to path to Scripts "C:\Users\kisha\Dropbox\KC22070003466\3 - Advanced Software Engineering\L3T10 - Capstone Project - Consolidation\Capstone_Project\Virtual_env\my_django\Scripts"
        + activate.bat
   
1. Download Python to run the program @ https://www.python.org/downloads/
1. Run the Python Installer
1. Check the Box for "Add Python to PATH"
In cmd:
1. Verify pip installation: `pip --version`

*Note: Django Secret Key and Database Admin login is in the .env*
You will need to set up your custom Secret Key before running the website
1. Clone this repository
1. Create a `.env` file in the project's root directory with the following content:
    + DJANGO_SECRET_KEY=mysecretkeygoeshere
1. Install Packages:
    + pip install [package_name]
    
    OR
    + python -m pip install -r requirements.txt

# Usage section
*Instruct others on how to use your project after they’ve installed it*

In the Command Prompt:
+ cd to project root directory and run the command: python manage.py runserver

The docker image can be found at: 
+ https://hub.docker.com/repository/docker/kcse1/cold-meats/general

Outline the steps necessary to build and run your application with venv and Docker:
+ Install Docker desktop @ https://www.docker.com/products/docker-desktop
+ Open the Command Prompt
    Follow the commands:
    + docker run hello-world
    + docker build -t django-app . (Notice the '/' left off at the end)    
    + docker run -d -p 80:80 django-app    
    + docker tag django-app [user]]/[repo]]:[tag-name]
    + docker login
    + docker push [user]]/[repo]]:[tag-name]
    + docker run -d -p 80:80 [user]]/[repo]]

1. Deactivate the Virtual Environment:
    + deactivate

*View user-friendly software documentation generated with Sphinx*

+ docstrings were created for a few functions, classes and modules/scripts
+ locate the HTML file in the _build/html folder
+ open index.html file in a browser

*Include screenshots of your project in action*

![Login](screenshots/login.png)

![Register](screenshots/register.png)

![Catalogue](screenshots/catalogue.png)

![Reviews](screenshots/reviews.png)

![Subscribe](screenshots/subscribe.png)

![Blog-post](screenshots/blog_post.png)

![Poll](screenshots/poll1.png)

![Poll](screenshots/poll.png)

![Poll](screenshots/poll3.png)

![Sphinx1](screenshots/sphinx_software_doc1.png){width = 250x}

![Sphinx2](screenshots/sphinx_software_doc2.png){width = 250x}

![Sphinx3](screenshots/sphinx_software_doc3.png){width = 250x}

![Sphinx4](screenshots/sphinx_software_doc4.png){width = 250x}

![Sphinx5](screenshots/sphinx_software_doc5.png){width = 250x}

# Credits
*Highlights and links to the authors of your project if the project has been created by more than one person*

@KC-software-en

# Add a URL to your GitHub repository

https://github.com/KC-software-en/L3T10-repo
