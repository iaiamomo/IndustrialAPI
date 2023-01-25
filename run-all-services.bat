@echo off
cd actors_api/device_descriptions
FOR %%s IN (*) DO start /B python ../../run-service.py --spec %%s
PAUSE
cd ../..