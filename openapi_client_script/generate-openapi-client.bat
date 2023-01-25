rmdir /s industrial-api-client
rmdir /s ../actors_api/client

openapi-python-client generate --path ../actors_api/spec.yml

move industrial-api-client/industrial_api_client ../actors_api/client

rmdir /s industrial-api-client
