from bottle import run
import bottle
import rest.car_ressource
import rest.driver_ressource

if __name__ == "__main__":
    run(host='localhost', port=3000)

app = bottle.default_app()
