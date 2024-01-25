# Industrial API platform

Implementing **Industrial API** platform for managing manufacturing actors (devices, machines, humans,...) digital services. 

The following **template** is used to generate the actors descriptions. The information of the actor are represented as attributes and features. <em>Features</em> represent a state with properties (e.g., <code>status</code>), while <em>attributes</em> (e.g., <code>type</code>, <code>actions</code>, <code>transitions</code>) represent functionalities and values that do not change over time.
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
The configuration file [conf.json](conf.json) contains the basic information needed to run the platform.
```json
{
    "mode": "plan",
    "phase": 0,
    "version": "v4",
    "size": "large"
}
```
The JSON key <code>mode</code> accept the value <code>plan</code>, the key <code>phase</code> accepts the value <code>0</code> (representing the chip chain manufacturing case study), and the key <code>size</code> accepts <code>[xsmall, small, medium, large]</code> values (related to the number of involved services).

[descriptions_phase](descriptions_phase0_v4) contains the description of the manufacturing actors.


## How to run the Industrial API platform
- Run the server (a middleware exposing HTTP server and a websocket server):
  ```sh
  python app.py
  ```

- Run the services (which communicate with the server through websocket):
  ```sh
  python launch_devices.py
  ```

## Preliminaries
- Install required Python packages:
  ```sh
  pip install -r requirements.txt
  ```

- Generate Python client from OpenAPI v3.0 specification:
  ```sh
  cd actors_api_plan/open_client_script
  ./generate-openapi-client.sh
  ```

