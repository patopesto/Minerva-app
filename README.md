This is the repository for the Minerva API hacky project.
Maintainer: ALM (bambinito.dev@gmail.com)

Based on the original crappy python script ran with cron.
Later added a REST API using Falcon to manage tasks + scheduler with APScheduler.
Then refactored everything to make configurable and deployable app.
Then Dockerized the app.

Instructions:

- To run Locally:
Clone the repo.
Install MongoDB and have it running on `http://localhost:27017` (default port) then,
```shell
python3 -m venv venv
pip install -r requirements.txt
```

To run app:
```shell
python run.py
```
(use --help to see all configuration arguments)
API should be available on `http://localhost:5000/`

- To create new Task:
POST request at `http://localhost:5000/tasks` with a body of the form:
```json
{
	"course": {
		"dept": "ECSE",
		"code": "308",
		"crn": "15974",
		"term": "Winter2021"
	},
	"email": "bambinito.dev@gmail.com"
}
```



- To run Dev: (app running in local Docker container)
Pull and run mongo as a Docker container
```shell
docker pull mongo
docker run --detach --name mongodb mongo:latest
```

Pull Docker image:
(https://hub.docker.com/repository/docker/n8zjgu6r9/api/general)
```shell
docker pull n8zjgu6r9/api:1.0
```

OR build Docker image:
```shell
docker build -t api:1.0 .
```

Finally run container:
```shell
docker run -it --detach --publish 5000:5000 --link mongodb:mongodb --name api -e APP_ENV_NAME="DEV" api:1.0
```
