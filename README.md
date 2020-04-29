# API-POC

A toy API.  Creates, deletes, and lists comments, allowing upvotes and downvotes.  Built with [Hug](https://www.hug.rest), [PyMongo](https://pymongo.readthedocs.io/en/stable/), [NGINX](https://www.nginx.com), [Gunicorn](https://gunicorn.org), and [Docker](https://docs.docker.com).

### Installation
To build and run, use

```sh
$ docker-compose up --build -d
```

### Documentation
Once you bring it up, the API is documented at http://localhost:8000/docs .
The proxying gets hug slightly confused, so where the examples say `http://localhost,localhost/`
you will need `http://localhost:8000/` before the remainder of the path.

### Influences
This approach is influenced by two examples from the hug project:
https://github.com/hugapi/hug/tree/develop/examples/docker_compose_with_mongodb and
https://github.com/hugapi/hug/tree/develop/examples/docker_nginx
