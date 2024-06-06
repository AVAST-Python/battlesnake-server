

### Prepare environment

python -m virtualenv .venv
source .venv/bin/activate

pip install flask

(TO-DO)
pip install -r requirements.txt

### Documentation

https://docs.battlesnake.com/api/webhooks


### Run

```sh
python -m flask run --reload
```

### ngrok

```sh
ngrok http --domain=becoming-formally-lab.ngrok-free.app 80
```
