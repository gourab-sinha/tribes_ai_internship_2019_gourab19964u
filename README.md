# Tribes Internship Project
This project is the part of Tribes Internship Hiring Process.
# Application Summary
The goal of this project to create a Standard Data Processor(SDP) using Python, Neo4j and Flask Framework. The application will take json file as input and it will create the nodes as per the given excel sheet or schema. 
# Software Requirements
This application runs on local environment.
So it is important to have all the required software/framework/api to run the application. The required software/framework/api are listed below:
1. [Python - 3.6](https://www.python.org/download/releases/3.0/)
2. [Git](https://git-scm.com/download/mac)
3. [Neo4j Desktop](https://neo4j.com/download/)
4. Virtual Environment
5. Flask Framework
6. Neo4j Python Driver
7. Jinja2
8. Pycodestyle(Optional)
# How to run the project
A. Download(If not available on machine):
1. [Python - 3.6](https://www.python.org/download/releases/3.0/)
2. [Git](https://git-scm.com/download/mac)
3. [Neo4j Desktop](https://neo4j.com/download/)

B. Installation(If not installed):
1. Git
2. Neo4j Desktop 
3. Virtual Environment(Terminal: pip3 install virtualenv)
4. Setting Virtual Environment:
5. Clone the git repository https://github.com/gourab-sinha/tribes_ai_internship_2019_gourab19964u.git using git clone repo_link after step 3.
6. Go inside the folder which you cloned.
7. Create Virtual Environment(Terminal:virtualenv -p python3 Tribes_Internship).
8. To run on virtual environment(Terminal:source Tribes_Internship/bin/activate).
9. Notice the present path on terminal(will look something like (Tribes_Internship) %).
10. [Python Neo4j Driver(Terminal:pip3 install neo4j)](https://neo4j.com/developer/python/).
11. Flask Framework(Terminal:pip3 install Flask).
12. Pycodestyle(Terminal: pip3 install pycodestyle) (Optional).


C. Run
1. Create graph database in the Neo4j Desktop Application
2. Do select Neo4j version Neo4j 3.5.12
3. Provide database username as "tribes_db" and password as "Gaurabh@1234" excluding the double quotes.
7. Do check whether server database is up or not, inorder to check it visit http://localhost:7474
8. If it is up then proceed with the following otherwise see the troubleshoot section.
9. Now we setup all the required software/framework/api. It time to run the application.
10. Switch back to virtual environment and type "python3 run.py" excluding double quotes.
11. It will run the flask application on port 5000.

# Navigation in application
1. 'https://localhost:5000/teams/' or 'https://localhost:5000/team/' or 'https://localhost:5000/Teams/' or 'https://localhost:5000/Team/'
2. 'https://localhost:5000/grounds/' or 'https://localhost:5000/ground/' or 'https://localhost:5000/Ground/' or 'https://localhost:5000/Grounds/'
3. 'https://localhost:5000/members/<string:team_name>/ or 'https://localhost:5000/member/<string:team_name>/ or 'https://localhost:5000/Members/<string:team_name>/ or 'https://localhost:5000/Member/<string:team_name>/

# Troubleshoot
1. If virtual environment is not getting setup properly please follow the link: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/
2. If packages or modules are not getting install then try to uninstall the previous verison with the command pip3 uninstall "Packagename" and then install them with proper version.
3. If Neo4j Database is not getting connected then try to turn off the authentication by going inside the Neo4j Desktop Application and select manage then settings and dbms.security.auth_enabled=false
4. If port is busy then go inside the run.py and change the port number where 5000 is written to your desire port number make sure that, that is not busy.
5. If any python3 file show formating error then you might have running on different os and that format needs to be converted to desired format. To do that please install dos2unix

# Note
1. If you are trying to see members without specifying the team name inside the url then you will get error message.
2. Do not install drivers with pip as it will install for python 2.X which is not required by the application. Make sure whenever you are installing anything on virtual environment using pip wheel, put pip3 instead pip
