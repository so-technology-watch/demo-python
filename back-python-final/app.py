from bottle import run
import bottle

import ressources.Author_ressource 
import ressources.Badge_ressource 
import ressources.Book_ressource 
import ressources.BookOrder_ressource 
import ressources.BookOrderItem_ressource 
import ressources.Country_ressource 
import ressources.Customer_ressource 
import ressources.Employee_ressource 
import ressources.EmployeeGroup_ressource 
import ressources.Publisher_ressource 
import ressources.Review_ressource 
import ressources.Shop_ressource 
import ressources.Synopsis_ressource 
import ressources.Workgroup_ressource 

if __name__ == "__main__":
    run(host='localhost', port=3000)

app = bottle.default_app()
