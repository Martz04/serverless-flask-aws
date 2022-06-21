# Basic Example of REST CRUD API using serverless, AWS and Python.
If you either need to quickly deploy a small API or just decided to migrate your codebase to leverage the advantages of AWS Lambda, you can use a powerful combo of Flask and Serverless framework.

## Usual installation

    virtualenv venv -p python3
    . venv/bin/activate.fish# install Flask and freeze requirements
    (venv) pip install Flask
    (venv) pip freeze > requirements.txt

Install serverless plugins

    sls plugin install -n serverless-wsgi
    sls plugin install -n serverless-python-requirements

## Custom installation

There is also a Makefile available to run this application using docker

    make build
    make up
    make build-table
