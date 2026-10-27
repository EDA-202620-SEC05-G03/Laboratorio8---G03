def new_list():
    new_list = {
        'elements': [],
        'size': 0,
    }
    return new_list

def add_first (my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list
    
def add_last (my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def first_element (my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["elements"][0]


def last_element (my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        return my_list["elements"][-1]

def size (my_list):
    return my_list["size"]

def get_element(my_list, pos):
    if 0 <= pos and pos < my_list["size"]:
        return my_list["elements"][pos]
    else:
        raise Exception('IndexError: list index out of range')
 

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def is_empty(my_list):
    return my_list["size"] == 0

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["elements"].pop(0)
        my_list["size"] -= 1
    return elem

def remove_last(my_list):
    if is_empty(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        elem = my_list["elements"].pop(-1)
        my_list["size"] -= 1
    return elem

def delete_element(my_list, pos):
    if 0 <= pos and pos < my_list["size"]:
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def insert_element(my_list, element, pos):
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    my_list["elements"].insert(pos, element)
    my_list["size"] += 1
    return my_list

def change_info(my_list, pos, new_info):
    if 0 <= pos and pos < size(my_list):
        my_list["elements"][pos] = new_info
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def exchange(my_list, pos_1, pos_2):
    if (0 <= pos_1 and pos_1 < size(my_list)) and (0 <= pos_2 and pos_2 < size(my_list)):
        elem_1 = my_list["elements"][pos_1] 
        elem_2 = my_list["elements"][pos_2]
        my_list["elements"][pos_1] = elem_2
        my_list["elements"][pos_2] = elem_1
    else:
        raise Exception('IndexError: list index out of range')
    return my_list

def sub_list(my_list, pos_i, num_elements):
    if 0 <= pos_i and pos_i < size(my_list):
        nueva_lista = new_list()
        for i in range(pos_i, pos_i + num_elements):
            elem = my_list["elements"][i]
            nueva_lista = add_last(nueva_lista, elem)
    else:
        raise Exception('IndexError: list index out of range')
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

def selection_sort (my_list, sort_crit):
    n = size(my_list)
    
    for i in range(0, n-1):
        min_index = i
        for j in range (i+1, n):
            elem = get_element(my_list, j)
            min_elem = get_element(my_list, min_index)
            if sort_crit(elem, min_elem) is True:
                min_index = j
        if min_index != i:
            my_list = exchange(my_list, i, min_index)

    return my_list

# ==============
# INSERTION SORT
# ==============
        
def insertion_sort (my_list, sort_crit):
    
    for i in range(1, size(my_list)):
        elem_actual = get_element(my_list, i)
        j = i
        while j > 0 and sort_crit(elem_actual, get_element(my_list, j-1)):
            my_list = exchange(my_list, j-1, j)
            j -= 1
    
    return my_list

# ==========
# SHELL SORT
# ==========

def shell_sort(my_list, sort_crit):
    
    gap = size(my_list) // 2

    while gap > 0:
        for i in range(gap, size(my_list)):
            elem_actual = get_element(my_list, i)
            j = i
            while j >= gap and sort_crit(elem_actual, get_element(my_list, j-gap)):
                
                my_list = exchange(my_list, j-gap, j)
                j -= gap
        gap = gap // 2
        
    return  my_list

# ==========
# MERGE SORT
# ==========

def merge_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list
    aux_list = sub_list(my_list, 0, size(my_list))
    merge_sort_rec(my_list, aux_list, sort_crit, 0, size(my_list) - 1)
    return my_list


def merge_sort_rec(my_list, aux_list, sort_crit, low, high):
    if high <= low:
        return
    mid = (high + low) // 2
    merge_sort_rec(my_list, aux_list, sort_crit, low, mid)
    merge_sort_rec(my_list, aux_list, sort_crit, mid + 1, high)
    merge(my_list, aux_list, sort_crit, low, mid, high)


def merge(my_list, aux_list, sort_crit, low, mid, high):
    for k in range(low, high + 1):
        valor = get_element(my_list, k)
        aux_list = change_info(aux_list, k, valor)

    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        elem_izquierda = get_element(aux_list, i)
        elem_derecha = get_element(aux_list, j)

        if sort_crit(elem_izquierda, elem_derecha):
            my_list = change_info(my_list, k, elem_izquierda)
            i += 1
        else:
            my_list = change_info(my_list, k, elem_derecha)
            j += 1

        k += 1

    while i <= mid:
        elem_izquierda = get_element(aux_list, i)
        my_list = change_info(my_list, k, elem_izquierda)
        i += 1
        k += 1

    while j <= high:
        elem_derecha = get_element(aux_list, j)
        my_list = change_info(my_list, k, elem_derecha)
        j += 1
        k += 1

    return my_list

# ==========
# QUICK SORT
# ==========

def quick_sort(my_list, sort_crit): 
    if size(my_list) <= 1:
        return my_list
    quick_sort_rec(my_list, sort_crit, 0, size(my_list) - 1)
    return my_list
    

def quick_sort_rec(my_list, sort_crit, low, high): 
    if high <= low: 
        return my_list
    
    pos_pivote = partition(my_list, sort_crit, low, high) 
    quick_sort_rec(my_list, sort_crit, low, pos_pivote - 1) 
    quick_sort_rec(my_list, sort_crit, pos_pivote + 1, high)
    
def partition(my_list, sort_crit, low, high): 
    pivote = get_element(my_list, high)
    i = low - 1
    
    for j in range(low, high): 
        if sort_crit(get_element(my_list, j), pivote):
            i += 1 
            exchange(my_list, i, j) 
    
    exchange(my_list, i + 1, high) 
    return i + 1

