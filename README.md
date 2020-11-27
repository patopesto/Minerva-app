# Minerva App
This is the repository for the backend of the [Minerva App](https://app.minerva.bambinito.co) hacky project.  
Maintainer: ALM (bambinito.dev@gmail.com)  

The purpose of this api is to schedule tasks that will check available spaces at regular intervals for a McGill course.   
If a space is found, it will send you an email notification.   
This app significantly increases your chance of getting a space in the course you want...   

You can try it out at: https://app.minerva.bambinito.co   
The api used by the app is available at https://api.minerva.bambinito.co   
 
!!! This repository is depreciated and has been moved to [Gitlab](https://gitlab.com/patopest/api) !!!   
-> The repository for the web frontend can also be found on [Gitlab](https://gitlab.com/patopest/web)   

----------------------------------------------------------------------------------------------------------------------------------------
Based on the original crappy python script ran with cron.  
Later added a REST API using Falcon to manage tasks + scheduler with APScheduler.  
Then refactored everything to make configurable and deployable app.  
Then Dockerized the app.   
Then refactored everything a couple extra times....   

"Inspired" (a lot) by alexferl's [falcon-boilerplate](https://github.com/alexferl/falcon-boilerplate)  
  

## Instructions:  

### To run Locally:  
- Clone the repo.  
- Install MongoDB (using brew) and have it running on `localhost:27017` (default port) then,
```shell
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```
- In case you get a python thread crash:
```shell
echo 'export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES' >> venv/bin/activate
```
  
- To run app:  
```shell
python run.py
```
(use --help to see all configuration arguments)  
API should be available on `http://localhost:5000/`  
  
### Usage: 
- Create new user at POST `http://localhost:5000/register` with body: 
```json
{
	"email": "your.email@whatever.com",
	"password": "your_password"
}
```
- Use provided token in the `Authorization` header. 

To create new Task: 
- POST request at `http://localhost:5000/users/{{ user_id }}/tasks` with a body of the form: 
```json
{
	"course": {
		"dept": "COMP",
		"code": "101",
		"crn": "12345",
		"term": "Winter2056"
	},
	"email": "your.email@whatever.com"
}
```
  
  
  
### To run Dev:  
(app running in local Docker container)  
- Pull and run mongo as a Docker container  
```shell
docker pull mongo
docker run --detach --name mongodb mongo:latest
```

- Pull Docker image:
(https://gitlab.com/patopest/api/container_registry)
```shell
docker pull registry.gitlab.com/patopest/api
```

- OR build Docker image:
```shell
docker build -t api:1.0 .
```

- Finally run container:
```shell
docker run -it --detach --publish 5000:5000 --link mongodb:mongodb --name api -e APP_ENV_NAME="DEV" api:1.0
```
