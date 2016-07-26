# Flaskr

A microframework in Python 3.5.

* Pyenv with Python 3.5.1
* Editorconfig for python
* requirements.txt according environment
* Configuration handling: developement, unit & integration tests, staging, production configuration
* Sub-domains routing via blueprint. JSON, XML api, and multiple front-ends.
* Custom Error handling, send in the right format according the blueprint
* Static files Management
* Celery: redis lock, to manage single tasks processing. @single_instance.
* Flask-SQL-Alchemy: SQLite for developer, PostgreSQL for staging and production. 
* Flask-SQL-Alchemy-Models
* Database migration support via alembic
* Logging: Console in development, syslog daemon in staging and production.
* Loging: custom log format


## Next steps
* File yaml configuration
* Celery: monitor and clean the queue
* 404 error management according blueprint format (consumption format)


## Deployment
