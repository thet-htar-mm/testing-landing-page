**Setting Up the Project**

To get the project up and running, follow these steps:

1. Build the Docker Containers : `docker-compose up --build`

2. Deploy Database Changes with Sqitch : `docker-compose exec backend sqitch --chdir /app/sqitch deploy`
