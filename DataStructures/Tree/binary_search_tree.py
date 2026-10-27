from DataStructures.Tree import bst_node
from DataStructures.List import single_linked_list as sll

def new_map():
    my_bst = {"root": None}
    return my_bst

def default_compare(key, element):
    element_key = bst_node.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1

def put(my_bst, key, value):
    my_bst["root"] = insert_node(my_bst["root"], key, value)
    return my_bst


def insert_node(root, key, value):
    if root is None:
        return bst_node.new_node(key, value)

    cmp = default_compare(key, root)
    if cmp < 0:
        root["left"] = insert_node(root["left"], key, value)
    elif cmp > 0:
        root["right"] = insert_node(root["right"], key, value)
    else:
        root["value"] = value

    root["size"] = 1 + size_tree(root["left"]) + size_tree(root["right"])
    return root

def get(my_bst, key):
    node = get_node(my_bst["root"], key)
    if node is None:
        return None
    return bst_node.get_value(node)


def get_node(root, key):
    if root is None:
        return None

    cmp = default_compare(key, root)
    if cmp == 0:
        return root
    elif cmp < 0:
        return get_node(root["left"], key)
    return get_node(root["right"], key)


def size(my_bst):
    return size_tree(my_bst["root"])


def size_tree(root):
    if root is None:
        return 0
    return root["size"]

def remove(my_bst, key):
    my_bst['root'] = remove_node(my_bst['root'], key)
    return my_bst

def remove_node(root, key):
    if root is None:
        return None
    
    cmp = default_compare(key, root)
    if cmp < 0:
        root['left'] = remove_node(root['left'], key)
    elif cmp > 0:
        root['right'] = remove_node(root['right'], key)
    else:
        if root['left'] is None:
            return root['right']
        if root['right'] is None:
            return root['left']
        
        min_key = get_min_node(root['right'])
        root['value'] = get({'root': root['right']}, min_key)
        root['key'] = min_key
        root['right'] = delete_min_tree(root['right'])
        
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def contains(my_bst, key):
    return get(my_bst, key) is not None

def is_empty(my_bst):
    return my_bst['root'] is None

def key_set(my_bst):
    key_list = sll.new_list()
    key_set_tree(my_bst['root'], key_list)
    return key_list

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root['left'], key_list)
        sll.add_last(key_list, bst_node.get_key(root))
        key_set_tree(root['right'], key_list)
    return key_list

def value_set(my_bst):
    value_list = sll.new_list()
    value_set_tree(my_bst['root'], value_list)
    return value_list

def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root['left'], value_list)
        sll.add_last(value_list, bst_node.get_value(root))
        value_set_tree(root['right'], value_list)
    return value_list

def get_min(my_bst):
    if my_bst['root'] is None:
        return None
    return get_min_node(my_bst['root'])

def get_min_node(root):
    if root['left'] is None:
        return bst_node.get_key(root)
    return get_min_node(root['left'])

def get_max(my_bst):
    if my_bst['root'] is None:
        return None
    return get_max_node(my_bst['root'])

def get_max_node(root):
    if root['right'] is None:
        return bst_node.get_key(root)
    return get_max_node(root['right'])

def delete_min(my_bst):
    my_bst['root'] = delete_min_tree(my_bst['root'])
    return my_bst

def delete_min_tree(root):
    if root is None:
        return None
    if root['left'] is None:
        return root['right']
    root['left'] = delete_min_tree(root['left'])
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def delete_max(my_bst):
    my_bst['root'] = delete_max_tree(my_bst['root'])
    return my_bst

def delete_max_tree(root):
    if root is None:
        return None
    if root['right'] is None:
        return root['left']
    root['right'] = delete_max_tree(root['right'])
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def floor(my_bst, key):
    return floor_key(my_bst['root'], key)
    
def floor_key(root, key):
    if root is None:
        return None
    cmp = default_compare(key, root)
    if cmp == 0:
        return bst_node.get_key(root)
    if cmp < 0:
        return floor_key(root['left'], key)
    candidate = floor_key(root['right'], key)
    if candidate is not None:
        return candidate
    return bst_node.get_key(root)

def ceiling(my_bst, key):
    return ceiling_key(my_bst['root'], key)


def ceiling_key(root, key):
    if root is None:
        return None
    cmp = default_compare(key, root)
    if cmp == 0:
        return bst_node.get_key(root)
    if cmp > 0:
        return ceiling_key(root['right'], key)
    candidate = ceiling_key(root['left'], key)
    if candidate is not None:
        return candidate
    return bst_node.get_key(root)


def select(my_bst, pos):
    node = select_key(my_bst['root'], pos)
    if node is None:
        return None
    return bst_node.get_key(node)

def select_key(root, pos):
    if root is None:
        return None
    left_size = size_tree(root['left'])
    if pos < left_size:
        return select_key(root['left'], pos)
    if pos > left_size:
        return select_key(root['right'], pos - left_size - 1)
    return root

def rank(my_bst, key):
    return rank_keys(my_bst['root'], key)

def rank_keys(root, key):
    if root is None:
        return 0
    cmp = default_compare(key, root)
    if cmp < 0:
        return rank_keys(root['left'], key)
    if cmp > 0:
        return 1 + size_tree(root['left']) + rank_keys(root['right'], key)
    return size_tree(root['left'])

def height(my_bst):
    return height_tree(my_bst['root'])

def height_tree(root):
    if root is None:
        return 0
    left_h = height_tree(root['left'])
    right_h = height_tree(root['right'])
    if left_h > right_h:
        return 1 + left_h
    return 1 + right_h

def keys(my_bst, key_initial, key_final):
    key_list = sll.new_list()
    keys_range(my_bst['root'], key_initial, key_final, key_list)
    return key_list
    
def keys_range(root, key_initial, key_final, key_list):
    if root is None:
        return key_list
    key = bst_node.get_key(root)
    
    if key_initial < key:
        keys_range(root['left'], key_initial, key_final, key_list)
    
    if key_initial <= key <= key_final:
        sll.add_last(key_list, key)
        
    if key < key_final:
        keys_range(root['right'], key_initial, key_final, key_list)
    
    return key_list

def values(my_bst, key_initial, key_final):
    value_list = sll.new_list()
    values_range(my_bst["root"], key_initial, key_final, value_list)
    return value_list


def values_range(root, key_initial, key_final, value_list):
    if root is None:
        return value_list
    key = bst_node.get_key(root)
    if key_initial < key:
        values_range(root["left"], key_initial, key_final, value_list)
    if key_initial <= key <= key_final:
        sll.add_last(value_list, bst_node.get_value(root))
    if key < key_final:
        values_range(root["right"], key_initial, key_final, value_list)
    return value_list