## Service for Task2

#### Description:
Recreate a service that runs every hour and fetches random xkcd comic strip.

Acceptance Criteria:
* service is scheduled to run every hour
* service won’t download the same picture twice in a row
* service stores maximum two images on local filesystem
* please don’t spam xkcd too often, we don’t want to create a DDOS attack

#### Stack:
* Python3
* Celery
* Redis
* Docker

#### Implementation
App uses celery scheduler(beat) to execute periodical tasks and redis as a message broker.
Download code is in `download.py` file.

#### Run
`docker-compose up`
