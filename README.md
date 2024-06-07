

### Prepare environment

python -m virtualenv .venv
source .venv/bin/activate

pip install flask
pip install python-dotenv
pip install flask-cors

(TO-DO)
pip install -r requirements.txt

### Documentation

https://docs.battlesnake.com/api/webhooks


### Run

```sh
export $(xargs <.env)
python -m flask run --reload -p 8080
```

### ngrok

```sh
ngrok http --domain=becoming-formally-lab.ngrok-free.app 80
```
