# swell-campaign-service
swell-campaign-service
## start up
```
git clone https://github.com/njtc-pod/swell-campaign-service.git
cd swell-campaign-service
git checkout -b develop
git flow init -d
docker build -t swell-campaign-service .
docker run -p 80:80 swell-campaign-service:latest
```

### File structure breakdown

* **app/main.py:**
    * Instantiates the service by mapping all of the application code and logic
      into a single runtime entry point.

* **app/models.py:**
    * This is where the structure of your table is defined.

* **app/schemas.py:**
    * This is where the structure of how your table supports CRUD functions is defined.

* **app/actions/pushItRealGood.py**
    * This is where to define how your data is queried and filtered.

* **app/routers/pushItRealGood.py**
    * This is where to define if and how requests should be routed and actioned.