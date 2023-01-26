# Industrial APIs

Implementing **Industrial APIs** for industrial actors. 

Follow [template.json](actors_api/device_descriptions/template.json) to generate the actors descriptions. The template represents a converter device. The different aspects of the actor are represented as attributes and features. <em>Features</em> can either represent a state with properties (e.g., <code>status</code>, <code>voltage</code>) or a functionality of the actor (e.g., <code>converting</code>), while <em>attributes</em> (e.g., <code>type</code>) hold values that do not change or that change less frequently than the <em>feature</em> property values. Noticeably, for what concerns functionalities, effects can be different if something goes wrong during the execution. For example, if the <code>convert</code> fails, one or more effects could not be verified.

## Instructions
Run the HTTP server that acts as service repository and communication middleware:
```sh
python app.py
```

Run all the services:
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
cd open_client_script
./generate-openapi-client.sh   #if on linux
generate-openapi-client.bat    #if on Windows
```
