# Industrial APIs

Implementing **Industrial APIs** for industrial actors (devices, machines, humans,...). 

Follow the [template.json](actors_api/device_descriptions/template.json) to generate the actors descriptions. The template represents a designer human. The different aspects of the actor are represented as attributes and features. <em>Features</em> represent a state with properties (e.g., <code>status</code>), while <em>attributes</em> (e.g., <code>type</code>, <code>actions</code>) represent functionalities (e.g., <code>converting</code>) and values that do not change or that change less frequently than the <em>features</em> property values.

## Instructions
Run the server representing a middleware exposing HTTP server and a websocket server:
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
