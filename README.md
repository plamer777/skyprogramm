## The Skyprogramm
The application is a very simple example of social network kind of Instagram.
This project was created by Randomizer team by the following people:

 1. Aleksey Mavrin
 2. Nick Drozdovskiy
 3. Ivan Makarau

---

**The projects' structure**:

 - app - all blueprints
 - confing - constants and DAO class' instance
 - dao - PostsDao class
 - data - JSON files with posts, comments and bookmarks data
 - logs - log file
 - static - CSS and image files
 - tests - test classes for PostsDao and API
 - run.py - main Flask application file
 - utils.py - there's a function for quickly creating a logger

--- 

 **The following functions are implemented in the application**:
 -  A main page with all posts loading from JSON file
 -  A single post page with detailed posts content and comments
 -  A search page with posts found by keyword
 -  A user posts page with all posts placed by user
 -  A tag page with posts found by tag
 -  A bookmarks page with posts loaded from JSON file that were saved by user
 
---

**How to start the project:**
To start the app just follow the next steps:
 - Clone the repository
 - Install python 3.8.6 or newer and another base requirements such as pip and python3-venv
 - Create and activate virtual environment `python3 -m venv venv` and `. venv/bin/activate`(for Linux)
and `venv\Scripts\activate` (for Windows)
 - Install requirements by the command `pip install -r requirements.txt`
 - Run the app by the command `flask --app run:app run`  
 - After that application is ready to work

 All tests were implemented by using the pytest package. All methods of PostsDao and API views were tested and works correctly.
 
 
