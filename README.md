# loco-pi
## Steps to run the program
### Tools required
- Raspberry Pi
- TODO
### Generate certs
This script enables SSL context for the API by generating a self-signed SSL certificate and key using OpenSSL.

```
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
```

The generated certificate and key files, cert.pem and key.pem, are then used to configure the SSL context in the Flask application.

The API provides two routes:
- /start: Starts a separate process by executing the 'main.py' script using the subprocess module.
- /stop: Terminates the running process if it exists.

To run the API, execute this script directly.

Note: Make sure to have OpenSSL installed on your system before running this script.
### Create virtual env
- Navigate to your project's directory:
    ```
    cd /path/to/your/project
    ```
- Create a new virtual environment. Replace env with the name you want to give to your virtual environment:
    ```
    python3 -m venv env
    ```
- Activate the virtual environment:
    ```
    source env/bin/activate
    ```
- Install the packages from requirements.txt
    ```
    pip install -r requirements.txt
    ```
- Run the program. It exposes '/start' and '/stop' trigger APIs. Triggers for the start and stop APIs can be access through index.html page at https://raspberry-pi-IP:PORT/
    ```
    python3 api.py
    ```
#### Deactivate or remove venv
- Run the command below to deactivate venv, if it is already activated
    ```
    deactivate
    ```
- remove venv 
    ```
    rm -rf <venv name>
    ```


