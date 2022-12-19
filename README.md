# WPRDC Tools Server
Where all the cool stuff is.

## Installation
### Preparation
Before you begin, copy `.env.example` to `.env` and set the values for your needs
```shell
mv .env.example .env
```

### (Option 🐳) With docker-compose
The first time you deploy this project, the database will take longer to prepare than django is willing to wait.
```shell
docker-compose up -d db
```

Examine the process of the `db` service's deployment with
```shell
docker-compose logs -f db
```

Once it says it's ready to accept connections, you can stop following the logs and 
```shell
docker-compose up -d
```
to start any unstarted services (for now just the django service: `web`)

### (Option 🐿) Install from source
Set up your own postgres database and configure it with the credentials in your `.env` file
and then run 
```shell
./manage.py runserver
```

## Services
 - downstream *(coming soon)*
 - valet *(coming soon)*
 - property api *(coming soon)*
 - spork *(coming soon)*
