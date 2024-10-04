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
# robo-pi

