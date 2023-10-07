# SaMDB (Series and Movies Database)


## Dokku Deploy

    dokku apps:create samdb

    dokku postgres:create samdb
    dokku postgres:link samdb samdb

    dokku config:set sambdb SECRET_KEY="django-secret-key"
    dokku config:set samdb ENVIROMENT="PRODUCTION"
    dokku config:set samdb DEBUG=off
    dokku config:set samdb ALLOWED_HOSTS="127.0.0.1;localhost"
    dokku config:set samdb DISABLE_COLLECTSTATIC=1
    dokku config:set samdb MEDIA_ROOT="/storage" 

    sudo mkdir -p /var/lib/dokku/data/storage/samdb
    dokku storage:mount samdb /var/lib/dokku/data/storage/samdb:/storage
    sudo chmod a+w /var/lib/dokku/data/storage/samdb

