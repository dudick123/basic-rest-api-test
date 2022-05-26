# Getting Started
- Create a virtual environment
- Activate the virtual environment
- Source it
- Install Packages
    - python3 -m pip install requests
    - python3 -m pip install pytest
- Freeze packages into requirements.txt
    - pip3 freeze > requirements.txt

# For Mac
```
$ python3.9 -m venv venv
$ source env/bin/activate
```

# For Windows
## Create the Virtual Environment
```
python -m venv C:\source\basic-rest-api-test
```

## Activate the Virtual Environment
```
.\Scripts\Activate.ps1
```

# Start the test server

## For Mac
Naviagate to the basic-restapi-app folder
```
make dev
```

## For Windows
```
.\bring-up-docker.ps1
```
