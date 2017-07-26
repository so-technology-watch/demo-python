import commons.utility_commons as commons_utilitaire
from bottle import view, request, route, error, response, hook, TEMPLATE_PATH, template
from services import Car_service as commons_car_service
from entities.Car import Car

TEMPLATE_PATH[:] = ['templates']

car_service = commons_car_service.CarService("Car")
invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


def build_contex(Car, form_mode):
    return {
        'car': Car.to_dict(),
        'mode': form_mode,
        'save_action': "/Car/" + form_mode
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
@view("navigation_bar.tpl")
def error404(error):
    table = "../../home"
    body = 'Nothing here, sorry (Error 404)'
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@error(500)
@view("navigation_bar.tpl")
def error500(error):
    table = "../../Car"
    body = "error 500"
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/Car')
@view("navigation_bar.tpl")
def get_all():
    try:
        cars = car_service.find_all()
        list = [_car.to_dict() for _car in cars]
        output = template('Car.tpl', list=list, footer="")
        return {"body": output}
    except TypeError:
        return error500


@route('/Car/show/<id>')
@view("navigation_bar.tpl")
def get_by_id(id):
    try:
        car = car_service.find_by_id(id)
        contex = build_contex(car,'show')
        body = template('Car_by_id.tpl', contex, footer="")
        return {"body": body}
    except TypeError:
        return error500


@route('/Car/form/create')
@view("navigation_bar.tpl")
def form_for_create():
    try:
        contex = build_contex(Car(),'create')
        body = template('Car_form_create.tpl', contex, footer="")
        return {"body": body}
    except TypeError:
        return error500


@route('/Car/form/update/<id>')
@view("navigation_bar.tpl")
def form_for_update(id):
    car = car_service.find_by_id(id)
    contex = build_contex(car,'update')
    body = template('Car_form_update.tpl', contex)
    return {"body": body}


@route('/Car/create', method='POST')
@view("navigation_bar.tpl")
def create():
    car = Car()
    car.car_id = request.forms.get('car_id')
    car.car_name = request.forms.get('car_name')
    car.driver_id = request.forms.get('driver_id')
    entity = car_service.insert(car)
    message = commons_utilitaire.json_bool_response(entity)
    test = list(message.values())
    if test[0] == 200:
        return {"body": test[1]}
    else:
        return error500


@route('/Car/update', method='POST')
@view("navigation_bar.tpl")
def update():
    car = Car()
    car.car_id = request.forms.get('car_id')
    car.car_name = request.forms.get('car_name')
    car.driver_id = request.forms.get('driver_id')
    entity = car_service.update(car)
    message = commons_utilitaire.json_bool_response(entity)
    test = list(message.values())
    if test[0] == 200:
        return {"body": test[1]}
    else:
        return error500


@route('/Car/delete/:car_id')
@view("navigation_bar.tpl")
def delete(car_id):
    result = car_service.delete_by_id(car_id)
    message = commons_utilitaire.json_bool_response(result)
    test = list(message.values())
    if test[0] == 200:
        return {"body": test[1]}
    else:
        return error500
