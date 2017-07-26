from bottle import run
import bottle
import rest.Car_ressource
import rest.Driver_ressource
import rest.Person_ressource
import rest.Manufacturer_ressource

if __name__ == "__main__":
    run(host='localhost', port=8081)

app = bottle.default_app()
