from bottle import view, request, route, error, response, hook, TEMPLATE_PATH, template, redirect
import requests

TEMPLATE_PATH[:] = ['templates']

invalid_parameters = "Invalid arguments"
entity_not_found = "Entity not found"


def build_context(entity):
    return {
        'Car': entity.to_dict(),
    }


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
    table = "../../Car"
    body = "error 500"
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/Car')
@view("navigation_bar.tpl")
def get_all():
    resp = requests.get('http://localhost:3000/api/v1/Car')
    if resp.status_code == 200:
        output = template('Car.tpl', list=resp.json(), footer="")
        return {"body": output}
    else:
        return error500


@route('/Car/show/<id>')
@view("navigation_bar.tpl")
def get_by_id(id):
    resp = requests.get('http://localhost:3000/api/v1/Car/{}'.format(id))
    if resp.status_code == 200:
        entity = resp.json()
        output = template('Car_by_id.tpl', Car=entity, footer="")
        return {"body": output}
    else:
        return error500


@route('/Car/form/create')
@view("navigation_bar.tpl")
def form_for_create():
    resp = requests.get('http://localhost:3000/api/v1/Manufacturer')
    try:
        output = template('Car_form_create.tpl', list=resp.json() , footer="")
        return {"body": output}
    except TypeError:
        return error500


@route('/Car/form/update/<id>')
@view("navigation_bar.tpl")
def form_for_update(id):
    resp1 = requests.get('http://localhost:3000/api/v1/Car/{}'.format(id))
    resp2 = requests.get('http://localhost:3000/api/v1/Manufacturer')
    try:
        output = template('Car_form_update.tpl', Car=resp1.json(), list=resp2.json(), footer="")
        return {"body": output}
    except TypeError:
        return error500


@route('/Car/create', method='POST')
@view("navigation_bar.tpl")
def create():
    id = request.forms.get('id')
    manufacturer_id = request.forms.get('manufacturer_id')
    model = request.forms.get('model')
    year = request.forms.get('year')
    color = request.forms.get('color')
    entity = {"id": id, "manufacturer_id": manufacturer_id, "model": model, "year": year, "color": color}
    resp = requests.post('http://localhost:3000/api/v1/Car', json=entity)
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Car_by_id.tpl', Car=entity, footer=footer)
        return {"body": body}
    else:
        return error500


@route('/Car/update/:id', method='POST')
@view("navigation_bar.tpl")
def update(id):
    id = id
    manufacturer_id = request.forms.get('manufacturer_id')
    model = request.forms.get('model')
    year = request.forms.get('year')
    color = request.forms.get('color')
    entity = {"id": id, "manufacturer_id": manufacturer_id, "model": model, "year": year, "color": color}
    resp = requests.put('http://localhost:3000/api/v1/Car', json=entity)
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Car_by_id.tpl', Car=entity, footer=footer)
        return {"body": body}
    else:
        return error500


@route('/Car/delete/:id')
@view("navigation_bar.tpl")
def delete(id):
    resp = requests.delete('http://localhost:3000/api/v1/Car/{}'.format(id))
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        resp2 = requests.get('http://localhost:3000/api/v1/Car')
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Car.tpl', list=resp2.json(), footer=footer)
        return {"body": body}
    else:
        return error500
