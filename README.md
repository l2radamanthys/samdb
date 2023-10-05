# SaMDB (Series and Movies Database)


## Dokku Deploy

    dokku apps:create samdb

    dokku postgres:create samdb
    dokku postgres:link samdb samdb

    SECRET_KEY="django-secret-key"
    dokku config:set samdb ENVIROMENT="PRODUCTION"
    dokku config:set samdb DEBUG=off
    dokku config:set samdb ALLOWED_HOSTS="127.0.0.1;localhost"
    dokku config:set DISABLE_COLLECTSTATIC=1


