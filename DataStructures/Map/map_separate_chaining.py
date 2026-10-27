import random
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf


def new_map(num_elements, load_factor, prime=109345121):
    capacity = mf.next_prime(num_elements / load_factor)
    table = al.new_list()
    for i in range(capacity):
        al.add_last(table, sl.new_list())
    my_map = {
        "prime": prime,
        "capacity": capacity,
        "scale": random.randint(1, prime - 1),
        "shift": random.randint(0, prime - 1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0,
    }
    return my_map


def default_compare(key, element):
    if key == me.get_key(element):
        return 0
    elif key > me.get_key(element):
        return 1
    return -1


def find_node(bucket, key):
    node = bucket["first"]
    while node is not None:
        if default_compare(key, node["info"]) == 0:
            return node
        node = node["next"]
    return None


def put(my_map, key, value):
    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], pos)
    node = find_node(bucket, key)
    if node is not None:
        me.set_value(node["info"], value)
    else:
        sl.add_last(bucket, me.new_map_entry(key, value))
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
        al.add_last(new_table, sl.new_list())
    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    my_map["size"] = 0
    for i in range(al.size(old_table)):
        node = al.get_element(old_table, i)["first"]
        while node is not None:
            put(my_map, me.get_key(node["info"]), me.get_value(node["info"]))
            node = node["next"]
    return my_map


def contains(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], pos)
    return find_node(bucket, key) is not None


def get(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], pos)
    node = find_node(bucket, key)
    if node is None:
        return None
    return me.get_value(node["info"])


def remove(my_map, key):
    pos = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], pos)
    node = bucket["first"]
    i = 0
    while node is not None:
        if default_compare(key, node["info"]) == 0:
            sl.delete_element(bucket, i)
            my_map["size"] -= 1
            return my_map
        node = node["next"]
        i += 1
    return my_map


def size(my_map):
    return my_map["size"]


def is_empty(my_map):
    return my_map["size"] == 0


def key_set(my_map):
    keys = al.new_list()
    for i in range(al.size(my_map["table"])):
        node = al.get_element(my_map["table"], i)["first"]
        while node is not None:
            al.add_last(keys, me.get_key(node["info"]))
            node = node["next"]
    return keys


def value_set(my_map):
    values = al.new_list()
    for i in range(al.size(my_map["table"])):
        node = al.get_element(my_map["table"], i)["first"]
        while node is not None:
            al.add_last(values, me.get_value(node["info"]))
            node = node["next"]
    return values


