# python-web-flask-rocksdb-counter

## Description
A POC python flask web counter
that uses rocksdb as a datastore.

Rocksdb is not a database that persists data
neither is it a websocket that updates multiple
clients.

Testing frameworks: *testify* and *selenium*

## Tech stack
- python
  - flask
  - testify
  - selenium
- rocksdb

## Docker stack
- python:latest
- selenium:latest

## To run
`sudo ./install.sh -u`
Available at http://localhost

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`

## Credits
- https://github.com/Congyuwang/RocksDict/tree/main/examples
