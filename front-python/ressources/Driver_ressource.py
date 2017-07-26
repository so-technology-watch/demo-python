from bottle import view, request, route, error, response, hook, redirect, TEMPLATE_PATH, template
import requests

TEMPLATE_PATH[:] = ['templates']

invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


@hook('after_request')
def init_response():
    response.content_type = 'text/html'
    response.headers['Access-Control-Allow-Origin'] = '*'


@route('/')
@route('/home')
@view("navigation_bar.tpl")
def home():
    body = template('home.tpl', root="views")
    return {"body": body}


@error(404)
@view("navigation_bar.tpl")
def error404():
    table = "../../home"
    body = 'Nothing here, sorry (Error 404)'
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@error(500)
@view("navigation_bar.tpl")
def error500():
    table = "../../Driver"
    body = "error 500"
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/Driver')
@view("navigation_bar.tpl")
def get_all():
    resp = requests.get('http://localhost:3000/api/v1/Driver')
    if resp.status_code == 200:
        output = template('Driver.tpl', list=resp.json(), footer="")
        return {"body": output}
    else:
        return error500


@route('/Driver/show/<person_id>/<car_id>')
@view("navigation_bar.tpl")
def get_by_id(person_id, car_id):
    resp = requests.get('http://localhost:3000/api/v1/Driver/{}/{}'.format(person_id, car_id))
    if resp.status_code == 200:
        entity = resp.json()
        output = template('Driver_by_id.tpl', Driver=entity, footer="")
        return {"body": output}
    else:
        return error500


@route('/Driver/form/create')
@view("navigation_bar.tpl")
def form_for_create():
    resp1 = requests.get('http://localhost:3000/api/v1/Person')
    resp2 = requests.get('http://localhost:3000/api/v1/Car')
    try:
        output = template('Driver_form_create.tpl', list=resp1.json(), list2=resp2.json(), footer="")
        return {"body": output}
    except TypeError:
        return error500


@route('/Driver/form/update/<person_id>/<car_id>')
@view("navigation_bar.tpl")
def form_for_update(person_id, car_id):
    resp1 = requests.get('http://localhost:3000/api/v1/Person')
    resp2 = requests.get('http://localhost:3000/api/v1/Car')
    resp3 = requests.get('http://localhost:3000/api/v1/Driver/{}/{}'.format(person_id, car_id))
    try:
        output = template('Driver_form_update.tpl', list=resp1.json(), list2=resp2.json(), Driver=resp3.json(), footer="")
        return {"body": output}
    except TypeError:
        return error500


@route('/Driver/create', method='POST')
@view("navigation_bar.tpl")
def create():
    person_id = request.forms.get('person_id')
    car_id = request.forms.get('car_id')
    licence_number = request.forms.get('licence_number')
    licence_date = request.forms.get('licence_date')
    entity = {"person_id": person_id, "car_id": car_id, "licence_number":licence_number, "licence_date": licence_date}
    resp = requests.post('http://localhost:3000/api/v1/Driver', json=entity)
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Driver_by_id.tpl', Driver=entity, footer=footer)
        return {"body": body}
    else:
        return error500


@route('/Driver/update/:person_id/:car_id', method='POST')
@view("navigation_bar.tpl")
def update(person_id, car_id):
    person_id = person_id
    car_id = car_id
    licence_number = request.forms.get('licence_number')
    licence_date = request.forms.get('licence_date')
    entity = {"person_id": person_id, "car_id": car_id, "licence_number": licence_number, "licence_date": licence_date}
    resp = requests.put('http://localhost:3000/api/v1/Driver', json=entity)
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Driver_by_id.tpl', Driver=entity, footer=footer)
        return {"body": body}
    else:
        return error500


@route('/Driver/delete/:person_id/:car_id')
@view("navigation_bar.tpl")
def delete(person_id, car_id):
    resp = requests.delete('http://localhost:3000/api/v1/Driver/{}/{}'.format(person_id, car_id))
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        resp2 = requests.get('http://localhost:3000/api/v1/Driver')
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Driver.tpl', list=resp2.json(), footer=footer)
        return {"body": body}
    else:
        return error500
