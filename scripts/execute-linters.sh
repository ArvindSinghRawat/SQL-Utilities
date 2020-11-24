flake8 ./app --count --select=E9,F63,F7,F82 --show-source --statistics
flake8 ./app --count --exit-zero --max-complexity=10 --max-line-length=79 --statistics
pylint --load-plugins pylint_flask_sqlalchemy,pylint_flask ./app
