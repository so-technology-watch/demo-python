def find_by_id(dao, request):
    exist = dao.do_exists(request)
    if exist:
        return dao.do_select(request)
    else:
        return False


def find_all(dao):
    return dao.do_select_all()


def insert(dao, request, entity):
    exist = dao.do_exists(request)
    if exist:
        return False
    else:
        return dao.do_insert(entity)
    

def update(dao, request, entity):
    exist = dao.do_exists(request)
    if exist:
        return dao.do_update(entity, request)
    else:
        return False
    

def save(dao, request, entity):
    update = dao.do_update(entity, request)
    if update:
        return {
            'entity': entity,
            'isNew': False
        }
    else:
        return {
            'entity': dao.do_insert(entity),
            'isNew': True
        }


def delete_by_id(dao, request):
    exist = dao.do_exists(request)
    if exist:
        return dao.do_delete(request)
    else:
        return False
    
    
def delete(dao, request):
    return dao.do_delete(request)
    

def exists_by_id(dao, request):
    return dao.do_exists(request)


def exists(dao, request):
    return dao.do_exists(request)


def count_all(dao):
    return dao.do_count_all()
