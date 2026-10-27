import random
 
from DataStructures.List import array_list as al
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf

def new_map(num_elements, load_factor, prime=109345121):

    capacity = mf.next_prime(num_elements/load_factor)

    table = al.new_list()
    
    for _ in range(capacity):
        al.add_last(table, me.new_map_entry(None, None))

    tabla ={
        'prime': prime,
        'capacity': capacity,
        'scale': random.randint(1, prime - 1),
        'shift': random.randint(0, prime - 1),
        'table': table,
        'current_factor': 0,
        'limit_factor': load_factor,
        'size': 0
    }
    
    return tabla

def default_compare(key, entry):
    if key == me.get_key(entry):
        return 0
    elif key > me.get_key(entry):
        return 1
    return -1


def is_available(table, pos):
    entry = al.get_element(table, pos)
    if me.get_key(entry) is None or me.get_key(entry) == "__EMPTY__":
        return True
    return False


def find_slot(my_map, key, hash_value):
    first_avail = None
    found = False
    ocupied = False
    while not found:
        if is_available(my_map["table"], hash_value):
            if first_avail is None:
                first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if me.get_key(entry) is None:
                found = True
        elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
        hash_value = (hash_value + 1) % my_map["capacity"]
    return ocupied, first_avail


def put(my_map, key, value):
    hash_v = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_v)
    if found:
        entry = al.get_element(my_map["table"], pos)
        me.set_value(entry, value)
    else:
        al.change_info(my_map["table"], pos, me.new_map_entry(key, value))
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            my_map = rehash(my_map)
    return my_map


def rehash(my_map):
    new_capacity = mf.next_prime(2 * my_map["capacity"])
    old_table = my_map["table"]
    new_table = al.new_list()
    for i in range(new_capacity):
        al.add_last(new_table, me.new_map_entry(None, None))
    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    my_map["size"] = 0
    my_map["current_factor"] = 0
    for i in range(al.size(old_table)):
        entry = al.get_element(old_table, i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            put(my_map, key, me.get_value(entry))
    return my_map


def contains(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_v)
    return found


def get(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_v)
    if found:
        entry = al.get_element(my_map["table"], pos)
        return me.get_value(entry)
    return None


def remove(my_map, key):
    hash_v = mf.hash_value(my_map, key)
    found, pos = find_slot(my_map, key, hash_v)
    if found:
        al.change_info(my_map["table"], pos, me.new_map_entry("__EMPTY__", "__EMPTY__"))
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
    return my_map


def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return my_map["size"] == 0


def key_set(my_map):
    keys = al.new_list()
    for i in range(al.size(my_map["table"])):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            al.add_last(keys, key)
    return keys


def value_set(my_map):
    values = al.new_list()
    for i in range(al.size(my_map["table"])):
        entry = al.get_element(my_map["table"], i)
        key = me.get_key(entry)
        if key is not None and key != "__EMPTY__":
            al.add_last(values, me.get_value(entry))
    return values



