#!/usr/bin/env python3
import connexion
import sys

from actors_api_mdp.server import server as mdp_server
from actors_api_plan.server import server as plan_server

app = connexion.AioHttpApp(__name__, only_one_api=True)
app.add_api('actors_api\spec.yml')
# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app


if __name__ == '__main__':
    mode = sys.argv[0]
    if mode == 'mdp':
        mdp_server.run()
    elif mode == 'plan':
        plan_server.run()
    else:
        print('Unknown mode: {}, insert mdp or plan'.format(mode))
