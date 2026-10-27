from DataStructures.List import list_node as ln

def new_list():
    new_list = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return new_list

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
    
    if not is_in_array:
        count = -1
    return count

def is_empty(my_list):
    return my_list["size"] == 0

def add_first(my_list, element):
    my_list["first"] = {"info": element, "next": my_list["first"]}
    if my_list["size"] == 0:
        my_list["last"] = my_list["first"]
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    new_node = {"info": element, "next": None}
    if my_list["size"] == 0:
        my_list["first"] = new_node
    else:
        my_list["last"]["next"] = new_node
    my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["first"]["info"]

def last_element(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["last"]["info"]
    
def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["first"]["info"]
        my_list["first"] = my_list["first"]["next"]
        my_list["size"] -= 1
        if my_list["size"] == 0:
            my_list["last"] = None
        return elem
    
def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["last"]["info"]
        if my_list["size"] == 1:
            my_list["first"] = None
            my_list["last"] = None
        else:
            node = my_list["first"]
            for i in range(my_list["size"]-2):
                node = node["next"]
            node["next"] = None
            my_list["last"] = node
        my_list["size"] -= 1
    return elem

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        if pos == 0:
            my_list = add_first(my_list, element)
        elif pos == size(my_list):
           my_list = add_last(my_list, element)
        else:
            new_node = {'info': element, 'next': None}
            node = my_list["first"]
            for i in range(pos-1):
                node = node["next"]
            new_node["next"] = node["next"]
            node["next"] = new_node
            my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if pos < 0 or pos >= size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        if pos == 0:
            remove_first(my_list)
        elif pos == size(my_list) - 1:
            remove_last(my_list)
        else:
            actual = my_list["first"]
            for i in range(1, pos):
                actual = actual["next"]
            actual["next"] = actual["next"]["next"]
            my_list["size"] -= 1
        return my_list
    
def change_info (my_list, pos, new_info):
    if pos < 0 or pos >= size(my_list):
        raise IndexError('list index out of range')
    else:
        node = my_list["first"]
        for i in range(pos):
            node = node["next"]
        node["info"] = new_info
    return my_list

def exchange(my_list, pos_1, pos_2):
    if pos_1 < 0 or pos_1 >= size(my_list) or pos_2 < 0 or pos_2 >= size(my_list):
        raise IndexError('list index out of range')
    else:
        node_1 = my_list["first"]
        for i in range(pos_1):
            node_1 = node_1["next"]
        node_2 = my_list["first"]
        for i in range(pos_2):
            node_2 = node_2["next"]
        node_1["info"], node_2["info"] = node_2["info"], node_1["info"]
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if pos_i < 0 or pos_i >= size(my_list) or num_elements < 0 or pos_i + num_elements > size(my_list):
        raise IndexError('list index out of range')
    else:
        nueva_lista = new_list()
        node = my_list["first"]
        for i in range(pos_i):
            node = node["next"]
        for i in range(num_elements):
            nueva_lista = add_last(nueva_lista, node["info"])
            node = node["next"]
    return nueva_lista

# =====================
# DEFAULT SORT CRITERIA
# =====================

def default_sort_criteria (element_1, element_2):
    
    is_sorted = False
    if element_1 < element_2:
        is_sorted = True
    
    return is_sorted

# ==============
# SELECTION SORT
# ==============

def selection_sort(my_list, sort_crit):

    actual = my_list['first']
    
    while actual is not None and actual['next'] is not None:
        min_node = actual
        runner = actual['next']
        
        while runner is not None:
            if sort_crit(runner['info'], min_node['info']):
                min_node = runner
            runner = runner['next']
            
        if min_node != actual:
            actual['info'], min_node['info']= min_node['info'], actual['info']
           
        actual = actual['next']
        
    return my_list

# ==============
# INSERTION SORT
# ==============
        
def insertion_sort(my_list, sort_crit):
    if my_list['first'] is None or my_list['first']['next'] is None:
        return my_list

    sorted_head = my_list['first']
    actual = sorted_head['next']
    sorted_head['next'] = None   

    while actual is not None:
        siguiente = actual['next']
        actual['next'] = None

        if sort_crit(actual['info'], sorted_head['info']):
            actual['next'] = sorted_head
            sorted_head = actual
        else:
            buscador = sorted_head
            while buscador['next'] is not None and not sort_crit(actual['info'], buscador['next']['info']):
                buscador = buscador['next']
            actual['next'] = buscador['next']
            buscador['next'] = actual

        actual = siguiente

    my_list['first'] = sorted_head
    nodo = my_list['first']
    while nodo['next'] is not None:
        nodo = nodo['next']
    my_list['last'] = nodo

    return my_list

# ==========
# SHELL SORT
# ==========

def shell_sort(my_list, sort_crit):
    n = size(my_list)
    gap = n // 2

    while gap > 0:
        i = gap
        while i < n:
            actual = get_element(my_list, i)          
            j = i
            while j >= gap and sort_crit(actual, get_element(my_list, j - gap)):
                
                val_atras = get_element(my_list, j - gap)
                my_list = change_info(my_list, j, val_atras)
                my_list = change_info(my_list, j - gap, actual)
                j -= gap
            i += 1
        gap = gap // 2

    return my_list


# ==========
# MERGE SORT
# ==========

def merge_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list

    my_list['first'] = merge_sort_rec(my_list['first'], sort_crit)
    
    nodo = my_list['first']
    
    while nodo['next'] is not None:
        nodo = nodo['next']
    my_list['last'] = nodo
    
    return my_list
    
def merge_sort_rec(head, sort_crit):

    if head is None or head['next'] is None:
        return head
    
    slow = head
    fast = head['next']

    while fast is not None and fast['next'] is not None:
        slow = slow['next']
        fast = fast['next']['next']
    
    mitad = slow['next']
    slow['next'] = None
    
    izquierda = merge_sort_rec(head, sort_crit)
    derecha = merge_sort_rec(mitad, sort_crit)
    
    return merge(izquierda, derecha, sort_crit)

def merge(izquierda, derecha, sort_crit):
    
    dummy = ln.new_single_node(None)
    cola = dummy
    
    while izquierda is not None and derecha is not None:
        if sort_crit(izquierda['info'], derecha['info']):
            cola['next'] = izquierda
            izquierda = izquierda['next']
        else:
            cola['next'] = derecha
            derecha = derecha['next']
        cola = cola['next']
    
    if izquierda is not None:
        cola['next'] = izquierda
    else:
        cola['next'] = derecha
        
    return dummy['next']
     


# ==========
# QUICK SORT
# ==========

def quick_sort(my_list, sort_crit): 
    if size(my_list) <= 1:
        return my_list

    my_list['first'] = quick_sort_rec(my_list['first'], sort_crit)

    nodo = my_list['first']
    while nodo['next'] is not None:
        nodo = nodo['next']
    
    my_list['last'] = nodo
    
    return my_list

def quick_sort_rec(head, sort_crit):
    
    if head is None or head['next'] is None:
        return head
    
    pivote, menores_head, mayores_head = partition(head, sort_crit)
    
    menores_ordenados = quick_sort_rec(menores_head, sort_crit)
    mayores_ordenados = quick_sort_rec(mayores_head, sort_crit)
    
    if menores_ordenados is None:
        nueva_cabeza = pivote
    else:
        nueva_cabeza = menores_ordenados
        cola = menores_ordenados
        while cola['next'] is not None:
            cola = cola['next']
        cola['next'] = pivote
        
    pivote['next'] = mayores_ordenados
    
    return nueva_cabeza

def partition(head, sort_crit):
    
    penultimo = None
    actual = head
    
    while actual['next'] is not None:
        penultimo = actual
        actual = actual['next']
    
    pivote = actual
    penultimo['next'] = None
    
    menores_head = None
    menores_cola = None
    mayores_head = None
    mayores_cola = None
    
    nodo = head
    
    while nodo is not None:
        siguiente = nodo['next']
        nodo['next'] = None
        
        if sort_crit(nodo['info'], pivote['info']):
            if menores_head is None:
                menores_head = nodo
                menores_cola = nodo
            else:
                menores_cola['next'] = nodo
                menores_cola = nodo
        else:
            if mayores_head is None:
                mayores_head = nodo
                mayores_cola = nodo
            else:
                mayores_cola['next'] = nodo
                mayores_cola = nodo
        
        nodo = siguiente
        
    return pivote, menores_head, mayores_head