# Industrial API platform

Implementing **Industrial API** platform for manufacturing actors (devices, machines, humans,...). 

The following **template** is used to generate the actors descriptions. The different aspects of the actor are represented as attributes and features. <em>Features</em> represent a state with properties (e.g., <code>status</code>), while <em>attributes</em> (e.g., <code>type</code>, <code>actions</code>, <code>transitions</code>) represent functionalities and values that do not change over time.
```json
{
  "id": "<service_name>",
  "attributes": {
      "type": "<service_type>",
      "_comment": "static properties"
  },
  "features": {
      "_comment": "dynamic properties"
  }
}
```

## Chip Supply Chain case study
- The configuration file [conf.json](https://github.com/iaiamomo/IndustrialAPI/tree/main/conf.json) contains the basic information needed to run the platform. The JSON key <code>mode</code> accept only the value <code>plan</code>, the key <code>phase</code> accepts <code>[1,2]</code> values (representing the assortment and manufacturing phases respectively), and the key <code>size</code> accepts <code>[small, manageable1, manageable2, complex]</code> values (related to the number of involved services).

- [actors_api_plan](https://github.com/iaiamomo/IndustrialAPI/tree/main/actors_api_plan) contains the description of the manufacturing actors.

- [context.py](context.py) contains the contextual information.

## How to run the server
Run the server (a middleware exposing HTTP server and a websocket server):
```sh
python app.py
```

Run the services (which communicate with the server through websocket):
```sh
python launch_devices.py
```

## Preliminaries
Install required Python packages:
```sh
pip install -r requirements.txt
```

Generate Python client from OpenAPI v3.0 specification:
```sh
cd actors_api_plan/open_client_script
./generate-openapi-client.sh
```

## Note
In order to execute the Industrial API with the MDP-based controller make some changes in [app.py](app.py) and [launch_devices.py](launch_devices.py) files.
