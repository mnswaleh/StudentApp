## Student App

## set up

- Check that python 3, pip, virtualenv and SQL Server are installed are installed

- Clone the Student app repo and cd to root folder
    ```
    git clone https://github.com/mnswaleh/StudentApp.git
    ```

- Create Application environment variables and save them in .env file on root folder
    ```
    FLASK_ENV=development
    FLASK_APP=manage.py
    SECRET_KEY="examplesecretkey"
    DATABASE_URL="DRIVER={SQL Server Native Client 11.0};SERVER=SQLSERNAME;DATABASE=DatabaseName;UID=UserName;PWD=UserPassword;Trusted_Connection=yes"

    ```
- Create virtual env
    ```
    virtualenv venv
    ```
- Activate virtual env
    ```
    source venv/bin/activate or .\venv\Scripts\activate 
    ```
- Install dependencies
    ```
    pip install -r requirements.txt
    ```
- Running migrations

    - Upgrade the database
        ```
        flask db upgrade
        ```
- Run application.
    ```
    flask run
    ```

## Built with
- Python version  3
- Flask
- jinja2
- SQL Server
