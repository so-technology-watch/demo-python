from bottle import view, request, route, error, response, hook, TEMPLATE_PATH, template, redirect
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
    table = "../../Manufacturer"
    body = "error 500"
    footer = template('footer.tpl', table=table)
    return {"body": body, "footer": footer}


@route('/Manufacturer')
@view("navigation_bar.tpl")
def get_all():
    resp = requests.get('http://localhost:3000/api/v1/Manufacturer')
    if resp.status_code == 200:
        output = template('Manufacturer.tpl', list=resp.json(), footer="")
        return {"body": output}
    else:
        return error500


@route('/Manufacturer/show/<id>')
@view("navigation_bar.tpl")
def get_by_id(id):
    resp = requests.get('http://localhost:3000/api/v1/Manufacturer/{}'.format(id))
    if resp.status_code == 200:
        entity = resp.json()
        output = template('Manufacturer_by_id.tpl', Manufacturer=entity, footer="")
        return {"body": output}
    else:
        return error500


@route('/Manufacturer/form/create')
@view("navigation_bar.tpl")
def form_for_create():
    try:
        output = template('Manufacturer_form_create.tpl', footer="")
        return {"body": output}
    except TypeError:
        return error500


@route('/Manufacturer/form/update/<id>')
@view("navigation_bar.tpl")
def form_for_update(id):
    resp = requests.get('http://localhost:3000/api/v1/Manufacturer/{}'.format(id))
    try:
        output = template('Manufacturer_form_update.tpl', Manufacturer=resp.json(), footer="")
        return {"body": output}
    except TypeError:
        return error500


@route('/Manufacturer/create', method='POST')
@view("navigation_bar.tpl")
def create():
    id = request.forms.get('id')
    name = request.forms.get('name')
    entity = {"id": id, "name": name}
    resp = requests.post('http://localhost:3000/api/v1/Manufacturer', json=entity)
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Manufacturer_by_id.tpl', Manufacturer=entity, footer=footer)
        return {"body": body}
    else:
        return error500


@route('/Manufacturer/update/:id', method='POST')
@view("navigation_bar.tpl")
def update(id):
    id = id
    name = request.forms.get('name')
    entity = {"id": id, "name": name}
    resp = requests.put('http://localhost:3000/api/v1/Manufacturer', json=entity)
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Manufacturer_by_id.tpl', Manufacturer=entity, footer=footer)
        return {"body": body}
    else:
        return error500


@route('/Manufacturer/delete/:id')
@view("navigation_bar.tpl")
def delete(id):
    resp = requests.delete('http://localhost:3000/api/v1/Manufacturer/{}'.format(id))
    answer = list(resp.json().values())
    if resp.status_code == 200:
        if answer[0] == 200:
            mode = 'success'
        else:
            mode = 'danger'
        resp2 = requests.get('http://localhost:3000/api/v1/Manufacturer')
        footer = template('footer.tpl', code=answer[0], message=answer[1], mode=mode)
        body = template('Manufacturer.tpl', list=resp2.json(), footer=footer)
        return {"body": body}
    else:
        return error500
