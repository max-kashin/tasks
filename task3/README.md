## App for Task3

#### Description:
Simple web app that displays details about you saving the world.

Acceptance Criteria:
- Every time you save the world, you make a database record saving the following
information: “when you saved the world”; “How you saved the world”, “Who you thank for
being so awesome”.
- People you are thankful to are a separate list that you can modify, only name is important.
- Database is postgresql, structure is your decision.
- App is dockerised

#### Stack:
backend
* Python3
* FastAPI
* Pydantic
* Sqlalchemy
* PostgreSQL
* Uvicorn
* Docker
* Docker-compose

frontend
* React
* React-router
* Antd


#### Running the app
* backend
`docker-compose up`
* frontend
`npm run start`
