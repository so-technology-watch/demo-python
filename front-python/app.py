from bottle import run
import bottle
import ressources.Car_ressource
import ressources.Driver_ressource
import ressources.Person_ressource
import ressources.Manufacturer_ressource

if __name__ == "__main__":
    run(host='localhost', port=8081)

app = bottle.default_app()
