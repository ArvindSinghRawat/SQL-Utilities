# Development Setup on Local Machine

1. Install Python 3.8.5 <br/>
  [Download](https://www.python.org/downloads/)

2. MYSQL 8.0 Database <br/>
  [Download](https://dev.mysql.com/downloads/)
  > User is not limited to any specific db vendor. However, connector for database will change.

3. Download Repository <br/>
  ```console
  git clone https://github.com/ArvindSinghRawat/SQL-Utilities.git
  ```

4. In the downloaded repository, create a virtual environment
  ```console
  python3 -m pip install --user virtualenv
  python3 -m venv flask_env
  ```
  > Use of virtual environemt is not compulsory, but recommended.

5. Activate newly created virtual environment
  ```console
  source flask_env/bin/activate
  ```

6. Installing Project Dependencies
  ```console
  pip install -r requirements.txt
  ```

7. Add `.env` file with environment variables
  ```console
  export FLASK_APP=manage.py
  export FLASK_ENV=development
  export DEV_DB_URL=''
  export TEST_DB_URL=''
  export PROD_DB_URL=''
  ```
  > Replace your connection string with the DEV_DB_URL value. 

8. Run Flask Project
  ```console
  flask run
  ```
  **Output**
  ```console
    * Serving Flask app "manage.py" (lazy loading)
    * Environment: development
    * Debug mode: on
    * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
    * Restarting with stat
    * Debugger is active!
    * Debugger PIN: 668-259-024
  ```

9. Run (Localhost Url)[http://127.0.0.1:5000/] in any web browser
