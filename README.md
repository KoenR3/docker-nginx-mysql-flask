# docker-nginx-mysql-flask
Skeleton for docker-compose nginx/flask-mysql containers.

This is a skeleton that shows how to use Nginx with a flask application and a mysql data container.  It uses docker-compose to instantiate everything.

Simple use

```docker-compose up```

To start the process.

A data directory for mysql is created so that the data is persistent if you remove the container.  The flask application is mounted into the container as to make it easier to incorporate changes.

If you change something in the application and wish to bring them into effect, just use:

```docker-compose restart```
