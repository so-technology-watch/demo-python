import commons.commons_utilitaire as commons_utilitaire
from bottle import view, request, route, error, response, hook, TEMPLATE_PATH, template
from services import car_service as commons_car_service
from entities.car import Car

TEMPLATE_PATH[:] = ['views']

car_service = commons_car_service.CarService("car")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


def build_contex(car, form_mode):
    return {
        'car': car.to_dict(),
        'mode': form_mode,
        'save_action': "/cars/" + form_mode
    }


@hook('after_request')
def init_response():
    response.content_type = 'text/html'
    response.headers['Access-Control-Allow-Origin'] = '*'


@route('/')
@route('/home')
@view("navbar.tpl")
def home():
    body = template('home.tpl', root="views")
    return {"body": body, "footer": ""}


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
    table = "../../cars"
    body = commons_utilitaire.error_handler(400, invalid_parameters, response)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/cars')
@view("navbar.tpl")
def get_all():
    table = "home"
    cars = car_service.find_all()
    list = [_car.to_dict() for _car in cars]
    output = template('show_car.tpl', list=list)
    footer = template('footer.tpl', table=table)
    return {"body": output, "footer": footer}


@route('/cars/form/create')
@view("navbar.tpl")
def form_for_create():
    table = "../cars"
    contex = build_contex(Car(),'create')
    body = template('car_form.tpl', contex)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/cars/form/update/<car_id>')
@view("navbar.tpl")
def form_for_update(car_id):
    table = "../../cars"
    car = car_service.find_by_id(car_id)
    contex = build_contex(car,'update')
    body = template('car_form.tpl', contex)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/cars/show/<car_id>')
@view("navbar.tpl")
def show(car_id):
    table = "../cars"
    car = car_service.find_by_id(car_id)
    contex = build_contex(car,'show')
    body = template('show_car_by_id.tpl', contex)
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/cars/create', method='POST')
@view("navbar.tpl")
def create():
    table = "../cars"
    car = Car()
    car.car_id = request.forms.get('car_id')
    car.car_name = request.forms.get('car_name')
    car.driver_id = request.forms.get('driver_id')
    entity = car_service.create(car)
    message = commons_utilitaire.json_bool_response(entity)
    test = list(message.values())
    if test[0] == 200:
        footer = template('footer.tpl', table=table)
        return {"body": test[1], "footer": footer}
    else:
        return error500


@route('/cars/update', method='POST')
@view("navbar.tpl")
def update():
    table = "../cars"
    car = Car()
    car.car_id = request.forms.get('car_id')
    car.car_name = request.forms.get('car_name')
    car.driver_id = request.forms.get('driver_id')
    entity = car_service.update(car)
    message = commons_utilitaire.json_bool_response(entity)
    test = list(message.values())
    if test[0] == 200:
        footer = template('footer.tpl', table=table)
        return {"body": test[1], "footer": footer}
    else:
        return error500


@route('/cars/delete/:car_id')
@view("navbar.tpl")
def delete(car_id):
    table = "../cars"
    result = car_service.delete_by_id(car_id)
    message = commons_utilitaire.json_bool_response(result)
    test = list(message.values())
    if test[0] == 200:
        footer = template('footer.tpl', table=table)
        return {"body": test[1], "footer": footer}
    else:
        return error500
