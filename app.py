#!/usr/bin/env python3
import connexion
import json


config_json = json.load(open('config.json', 'r'))
mode = config_json['mode']

if mode == 'plan':
    from actors_api_plan.server import server
else:
    from actors_api_mdp.server import server

app = connexion.AioHttpApp(__name__, only_one_api=True)
app.add_api(f'actors_api_{mode}/spec.yml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app


if __name__ == '__main__':
    server.run()
    