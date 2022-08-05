#!/bin/bash

# load .env
source .env

# Initialize flask db, migrate and upgrade it
flask db init
flask db migrate
flask db upgrade
