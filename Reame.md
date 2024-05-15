# Classifier for straight joints and cracks
## Usage:
### Test:
#### Start server:
##### Start with local conda environment:
```
(/Users/boshang/Downloads/converted_keras/.conda) (.conda) (base) ➜  converted_keras (main) conda run gunicorn -c gunicorn_config.py wsgi:app
```
##### Start with docker build:
Docker build:
```
docker build -t my-flask-app .
```
Debug repeatedly:
```
docker container stop my-flask-container                                              
docker container rm my-flask-container     
docker run --restart unless-stopped --name my-flask-container -p 80:8000 my-flask-app                                            
```
Deamon mode:
```
docker run -d --restart unless-stopped --name my-flask-container -p 80:8000 my-flask-app 

```
##### Start with docker compose:
```
docker-compose up -d
```
#### Test:
##### Simple test:
```
(base) ➜  ~  curl -X POST -F image=@"/Users/boshang/Desktop/joint/S1074750.png/straight_cracks/crack_45.png" http://localhost:8000/classify  # Use the new port 

{"class":"straight joints","confidence":0.9942787885665894}
```
##### Verbose mode test:
```
(base) ➜  ~  curl -v -X POST -F image=@"/Users/boshang/Desktop/joint/S1074750.png/straight_cracks/crack_45.png" http://localhost:8000/classify  # Use the new port

Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying [::1]:8000...
* connect to ::1 port 8000 failed: Connection refused
*   Trying 127.0.0.1:8000...
* Connected to localhost (127.0.0.1) port 8000
> POST /classify HTTP/1.1
> Host: localhost:8000
> User-Agent: curl/8.4.0
> Accept: */*
> Content-Length: 450
> Content-Type: multipart/form-data; boundary=------------------------MmM7aZNRt9IQeSuPwDQsTM
> 
* We are completely uploaded and fine
< HTTP/1.1 200 OK
< Server: gunicorn
< Date: Wed, 15 May 2024 20:02:02 GMT
< Connection: close
< Content-Type: application/json
< Content-Length: 60
< 
{"class":"straight joints","confidence":0.9942787885665894}
* Closing connection
```
