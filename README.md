

### Prepare environment

python -m virtualenv .venv
source .venv/bin/activate

pip install flask
pip install python-dotenv
pip install flask-cors
pip install RestrictedPython

(TO-DO)
pip install -r requirements.txt

### Documentation

https://docs.battlesnake.com/api/webhooks




How to create a bot:
/snake/<string:user>/

### Run

```sh
export $(xargs <.env)
python -m flask run --reload -p 8080
```

```sh
python -m flask run --reload -p 8080 --debug
```

### ngrok

```sh
ngrok http 8080
```
