An implement of the Falsky project based on the flask web framework

To run this project, pull this repository and then:

1. Create a virtual environment - 'python -m venv env'
2. Install python dependencies - 'pip install -r requirements.txt'
3. Create database - 'flask db upgrade'
4. Start the web server: 
                        dev server: 'flask run'
                        prod server: 'waitress-serve --listen=*:5000 wsgi:app'