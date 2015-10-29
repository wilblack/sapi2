## Notes

The full list of commands

```
docker-machine create --d virtualbox --virtualbox-memory 8096 dev
eval "$(docker-machine env dev)"
docker-compose build
docker-compose up -d

docker-compose run web /usr/local/bin/python manage.py migrate
docker-compose run web /usr/local/bin/python manage.py collectstatic --noinput
docker-compose run web /usr/local/bin/python manage.py load_init_data


```


Inspect a container, use `docker ps` to list contianers.

```
docker inspect -f {{.Volumes}}
```


If you get the "no space left on device" on the build, recreate the machine with more memory

```
docker-machine create --d virtualbox --virtualbox-memory 8096 dev
```



# Production Deployment

```
docker-machine create -d digitalocean --digitalocean-access-token=bb4d0bdcaaf911ccc109eadb9399ae9027f4c1e7f235dd29b4af9e9696b1af6a production


eval "$(docker-machine env production)


```