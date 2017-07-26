import commons.utility_commons as commons_utilitaire
from bottle import request, response, hook, view, template, error, TEMPLATE_PATH, route
from services import Driver_service as commons_driver_service
from entities.Driver import Driver

TEMPLATE_PATH[:] = ['views']

driver_service = commons_driver_service.DriverService("driver")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


def build_contex(driver, form_mode):
    return {
        'driver': driver.to_dict(),
        'mode': form_mode,
        'save_action': "/drivers/" + form_mode
    }


@hook('after_request')
def init_response():
    response.content_type = 'text/html'
    response.headers['Access-Control-Allow-Origin'] = '*'


@route('/')
@route('/home')
@view("navigation_bar.tpl")
def home():
    body = template('home.tpl', root="templates")
    return {"body": body}


@error(404)
@view("navbar.tpl")
def error404(error):
    table = "../../home"
    body = 'Nothing here, sorry (Error 404)'
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@error(500)
@view("navbar.tpl")
def error500(error):
    table = "../../drivers"
    body = commons_utilitaire.error_handler(400, invalid_parameters, response)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/drivers')
@view("navbar.tpl")
def get_all():
    table = "home"
    drivers = driver_service.find_all()
    list = [driver.to_dict() for driver in drivers]
    output = template('show_driver.tpl', list=list)
    footer = template('footer.tpl', table=table)
    return {"body": output, "footer": footer}


@route('/drivers/form/create')
@view("navbar.tpl")
def form_for_create():
    table = "../drivers"
    contex = build_contex(Driver(),'create')
    body = template('driver_form.tpl', contex)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/drivers/form/update/<driver_id>')
@view("navbar.tpl")
def form_for_update(driver_id):
    table = "../../drivers"
    driver = driver_service.find_by_id(driver_id)
    contex = build_contex(driver,'update')
    body = template('driver_form.tpl', contex)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/drivers/show/<driver_id>')
@view("navbar.tpl")
def show(driver_id):
    table = "../drivers"
    driver = driver_service.find_by_id(driver_id)
    contex = build_contex(driver,'show')
    body = template('show_driver_by_id.tpl', contex)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/drivers/create', method='POST')
@view("navbar.tpl")
def create():
    table = "../drivers"
    driver = Driver()
    driver.driver_id = request.forms.get('driver_id')
    driver.driver_name = request.forms.get('driver_name')
    entity = driver_service.create(driver)
    message = commons_utilitaire.json_bool_response(entity)
    test = list(message.values())
    if test[0] == 200:
        footer = template('footer.tpl', table=table)
        return {"body": test[1], "footer": footer}
    else:
        return error500


@route('/drivers/update', method='POST')
@view("navbar.tpl")
def update():
    table = "../drivers"
    driver = Driver()
    driver.driver_id = request.forms.get('driver_id')
    driver.driver_name = request.forms.get('driver_name')
    result = driver_service.update(driver)
    message = commons_utilitaire.json_bool_response(result)
    test = list(message.values())
    if test[0] == 200:
        footer = template('footer.tpl', table=table)
        return {"body": test[1], "footer": footer}
    else:
        return error500


@route('/drivers/delete/<driver_id>')
@view("navbar.tpl")
def delete(driver_id):
    table = "../drivers"
    result = driver_service.delete_by_id(driver_id)
    message = commons_utilitaire.json_bool_response(result)
    test = list(message.values())
    if test[0] == 200:
        footer = template('footer.tpl', table=table)
        return {"body": test[1], "footer": footer}
    else:
        return error500
