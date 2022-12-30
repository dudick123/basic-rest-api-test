# Getting Started
- Create a virtual environment `python -m venv`
- Activate the virtual environment
  - Source it `source /venv/bin/activate`
- Install Packages
    - `python3 -m pip install requests`
    - `python3 -m pip install pytest`
- Freeze packages into requirements.txt `pip3 freeze > requirements.txt`
- Open the app folder and run the docker container `make run`
- Start-up Check On The API [endpoint](http://localhost:8080/docs)
  - `curl http://localhost:8080/docs`
  - `curl http://localhost:8080/health`

# Start Executing Tests
Open a terminal and navigate to the 'tests' folder. Then run:
`pytest ./health/test_health_endpoints.py`
