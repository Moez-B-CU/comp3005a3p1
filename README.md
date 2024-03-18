
# COMP 3005 Assignment 3 Part 1

Submission for Assignment 3 Part 1 by Moez Bajwa. Database Access Object implementation, including functions getAllStudents(), addStudent(), updateStudentEmail() and deleteStudent().  
  
The language of choice is Python, and interaction with the database is done using Psycopg2. SQL file for initial table creation and data entry has also been included as 'create_db.sql'.



## Instructions

Requires Python 3.12 and Psycopg2 to be installed.

```bash
  cd project_directory
  pip install psycopg2
```
When running script, database name, user, password, and host must be provided via command line arguments in the above order. Host may be omitted, and will default to localhost if database is running locally. Example:

```bash
  py main.py comp3005a3 postgres pw localhost
```

Where `comp3005a3` is the database name, `postgres` is the user, `pw` is the users password, and `localhost` is the database host. Host can be omitted if the database is running on localhost but was shown for demonstration purposed.
    