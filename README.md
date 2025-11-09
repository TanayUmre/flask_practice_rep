# flask_practice_rep
## Normal Sample Code:-
```bash
from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>This is the main page of the website</h1>'

@app.route('/about')
def about_page():
    return '<h1>This is the about page of the website</h1>'
```

-----
### To run this code:-
#### In CMD:-
```bash
set FLASK_APP=filename.py
flask run
```

#### In Powershell:-
```bash
$env:FLASK_APP = "filename.py"
$env:FLASK_DEBUG = "1"
flask run
```

#### More Simple:-
```bash
flask --app filename.py --debug run
```
