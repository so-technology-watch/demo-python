# Python class for run the app
# Created on 2017-08-25 ( Time 18:18:33 )

from bottle import run
import bottle

import resources.Author_resource 
import resources.Badge_resource 
import resources.Book_resource 
import resources.BookOrder_resource 
import resources.BookOrderItem_resource 
import resources.Country_resource 
import resources.Customer_resource 
import resources.Employee_resource 
import resources.EmployeeGroup_resource 
import resources.Publisher_resource 
import resources.Review_resource 
import resources.Shop_resource 
import resources.Synopsis_resource 
import resources.Workgroup_resource 

if __name__ == "__main__":
    run(host='localhost', port=3000)

app = bottle.default_app()
