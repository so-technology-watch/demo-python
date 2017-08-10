from bottle import run
import bottle
import ressources.Cours_ressource
import ressources.Eleve_ressource
import ressources.Note_ressource
import ressources.Typemention_ressource
import ressources.Typesexe_ressource

if __name__ == "__main__":
    run(host='localhost', port=3000)

app = bottle.default_app()
