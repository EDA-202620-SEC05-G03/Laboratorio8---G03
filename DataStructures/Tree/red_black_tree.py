from DataStructures.Tree import rbt_node
from DataStructures.List import single_linked_list as sl


def new_map():
    my_rbt = {'root': None,
              'type': 'RBT'
              }
    return my_rbt


def default_compare(key, element):
    element_key = rbt_node.get_key(element)
    if key == element_key:
        return 0
    elif key > element_key:
        return 1
    return -1


def size_tree(node):
    if node is None:
        return 0
    return node['size']


def is_red(node):
    if node is None:
        return False
    return rbt_node.is_red(node)


def flip_node_color(node_rbt):
    if node_rbt is not None:
        if rbt_node.is_red(node_rbt):
            rbt_node.change_color(node_rbt, rbt_node.BLACK)
        else:
            rbt_node.change_color(node_rbt, rbt_node.RED)


def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    flip_node_color(node_rbt['left'])
    flip_node_color(node_rbt['right'])


def rotate_left(node_rbt):
    x = node_rbt['right']
    node_rbt['right'] = x['left']
    x['left'] = node_rbt

    rbt_node.change_color(x, node_rbt['color'])
    rbt_node.change_color(node_rbt, rbt_node.RED)

    x['size'] = node_rbt['size']
    node_rbt['size'] = 1 + size_tree(node_rbt['left']) + size_tree(node_rbt['right'])
    return x


def rotate_right(node_rbt):
    x = node_rbt['left']
    node_rbt['left'] = x['right']
    x['right'] = node_rbt

    rbt_node.change_color(x, node_rbt['color'])
    rbt_node.change_color(node_rbt, rbt_node.RED)

    x['size'] = node_rbt['size']
    node_rbt['size'] = 1 + size_tree(node_rbt['left']) + size_tree(node_rbt['right'])
    return x


def balance(root):
    if is_red(root['right']) and not is_red(root['left']):
        root = rotate_left(root)
    if is_red(root['left']) and is_red(root['left']['left']):
        root = rotate_right(root)
    if is_red(root['left']) and is_red(root['right']):
        flip_colors(root)
    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root


def move_red_left(root):
    flip_colors(root)
    if is_red(root['right']['left']):
        root['right'] = rotate_right(root['right'])
        root = rotate_left(root)
        flip_colors(root)
    return root


def move_red_right(root):
    flip_colors(root)
    if is_red(root['left']['left']):
        root = rotate_right(root)
        flip_colors(root)
    return root

def put(my_rbt, key, value):
    my_rbt['root'] = insert_node(my_rbt['root'], key, value)
    rbt_node.change_color(my_rbt['root'], rbt_node.BLACK)
    return my_rbt


def insert_node(root, key, value):
    if root is None:
        return rbt_node.new_node(key, value)

    cmp = default_compare(key, root)
    if cmp < 0:
        root['left'] = insert_node(root['left'], key, value)
    elif cmp > 0:
        root['right'] = insert_node(root['right'], key, value)
    else:
        root['value'] = value

    if is_red(root['right']) and not is_red(root['left']):
        root = rotate_left(root)
    if is_red(root['left']) and is_red(root['left']['left']):
        root = rotate_right(root)
    if is_red(root['left']) and is_red(root['right']):
        flip_colors(root)

    root['size'] = 1 + size_tree(root['left']) + size_tree(root['right'])
    return root

def get(my_rbt, key):
    return get_node(my_rbt['root'], key)


def get_node(root, key):
    if root is None:
        return None

    cmp = default_compare(key, root)
    if cmp == 0:
        return rbt_node.get_value(root)
    elif cmp < 0:
        return get_node(root['left'], key)
    return get_node(root['right'], key)


def contains(my_rbt, key):
    return get(my_rbt, key) is not None


def size(my_rbt):
    return size_tree(my_rbt['root'])


def is_empty(my_rbt):
    return my_rbt['root'] is None

def key_set(my_rbt):
    key_list = sl.new_list()
    key_set_tree(my_rbt['root'], key_list)
    return key_list


def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root['left'], key_list)
        sl.add_last(key_list, rbt_node.get_key(root))
        key_set_tree(root['right'], key_list)
    return key_list


def value_set(my_rbt):
    value_list = sl.new_list()
    value_set_tree(my_rbt['root'], value_list)
    return value_list


def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root['left'], value_list)
        sl.add_last(value_list, rbt_node.get_value(root))
        value_set_tree(root['right'], value_list)
    return value_list

def get_min(my_rbt):
    min_node = get_min_node(my_rbt['root'])
    if min_node is None:
        return None
    return rbt_node.get_key(min_node)


def get_min_node(root):
    if root is None:
        return None
    if root['left'] is None:
        return root
    return get_min_node(root['left'])


def get_max(my_rbt):
    max_node = get_max_node(my_rbt['root'])
    if max_node is None:
        return None
    return rbt_node.get_key(max_node)


def get_max_node(root):
    if root is None:
        return None
    if root['right'] is None:
        return root
    return get_max_node(root['right'])

def delete_min(my_rbt):
    root = my_rbt['root']
    if root is None:
        return my_rbt
    if not is_red(root['left']) and not is_red(root['right']):
        rbt_node.change_color(root, rbt_node.RED)
    my_rbt['root'] = delete_min_tree(root)
    if my_rbt['root'] is not None:
        rbt_node.change_color(my_rbt['root'], rbt_node.BLACK)
    return my_rbt


def delete_min_tree(root):
    if root['left'] is None:
        return None
    if not is_red(root['left']) and not is_red(root['left']['left']):
        root = move_red_left(root)
    root['left'] = delete_min_tree(root['left'])
    return balance(root)


def delete_max(my_rbt):
    root = my_rbt['root']
    if root is None:
        return my_rbt
    if not is_red(root['left']) and not is_red(root['right']):
        rbt_node.change_color(root, rbt_node.RED)
    my_rbt['root'] = delete_max_tree(root)
    if my_rbt['root'] is not None:
        rbt_node.change_color(my_rbt['root'], rbt_node.BLACK)
    return my_rbt


def delete_max_tree(root):
    if is_red(root['left']):
        root = rotate_right(root)
    if root['right'] is None:
        return None
    if not is_red(root['right']) and not is_red(root['right']['left']):
        root = move_red_right(root)
    root['right'] = delete_max_tree(root['right'])
    return balance(root)


def remove(my_rbt, key):
    if not contains(my_rbt, key):
        return my_rbt
    root = my_rbt['root']
    if not is_red(root['left']) and not is_red(root['right']):
        rbt_node.change_color(root, rbt_node.RED)
    my_rbt['root'] = remove_node(root, key)
    if my_rbt['root'] is not None:
        rbt_node.change_color(my_rbt['root'], rbt_node.BLACK)
    return my_rbt


def remove_node(root, key):
    if default_compare(key, root) < 0:
        if not is_red(root['left']) and not is_red(root['left']['left']):
            root = move_red_left(root)
        root['left'] = remove_node(root['left'], key)
    else:
        if is_red(root['left']):
            root = rotate_right(root)
        if default_compare(key, root) == 0 and root['right'] is None:
            return None
        if not is_red(root['right']) and not is_red(root['right']['left']):
            root = move_red_right(root)
        if default_compare(key, root) == 0:
            min_node = get_min_node(root['right'])
            root['key'] = rbt_node.get_key(min_node)
            root['value'] = rbt_node.get_value(min_node)
            root['right'] = delete_min_tree(root['right'])
        else:
            root['right'] = remove_node(root['right'], key)
    return balance(root)

def floor(my_rbt, key):
    return floor_key(my_rbt['root'], key)


def floor_key(root, key):
    if root is None:
        return None
    cmp = default_compare(key, root)
    if cmp == 0:
        return rbt_node.get_key(root)
    if cmp < 0:
        return floor_key(root['left'], key)
    candidate = floor_key(root['right'], key)
    if candidate is not None:
        return candidate
    return rbt_node.get_key(root)


def ceiling(my_rbt, key):
    return ceiling_key(my_rbt['root'], key)


def ceiling_key(root, key):
    if root is None:
        return None
    cmp = default_compare(key, root)
    if cmp == 0:
        return rbt_node.get_key(root)
    if cmp > 0:
        return ceiling_key(root['right'], key)
    candidate = ceiling_key(root['left'], key)
    if candidate is not None:
        return candidate
    return rbt_node.get_key(root)


def select(my_rbt, pos):
    node = select_key(my_rbt['root'], pos)
    if node is None:
        return None
    return rbt_node.get_key(node)


def select_key(root, pos):
    if root is None:
        return None
    left_size = size_tree(root['left'])
    if pos < left_size:
        return select_key(root['left'], pos)
    if pos > left_size:
        return select_key(root['right'], pos - left_size - 1)
    return root


def rank(my_rbt, key):
    return rank_keys(my_rbt['root'], key)


def rank_keys(root, key):
    if root is None:
        return 0
    cmp = default_compare(key, root)
    if cmp < 0:
        return rank_keys(root['left'], key)
    if cmp > 0:
        return 1 + size_tree(root['left']) + rank_keys(root['right'], key)
    return size_tree(root['left'])

def height(my_rbt):
    return height_tree(my_rbt['root'])


def height_tree(root):
    if root is None:
        return 0
    left_h = height_tree(root['left'])
    right_h = height_tree(root['right'])
    if left_h > right_h:
        return 1 + left_h
    return 1 + right_h

def keys(my_rbt, key_initial, key_final):
    key_list = sl.new_list()
    keys_range(my_rbt['root'], key_initial, key_final, key_list)
    return key_list


def keys_range(root, key_initial, key_final, key_list):
    if root is None:
        return key_list
    key = rbt_node.get_key(root)

    if key_initial < key:
        keys_range(root['left'], key_initial, key_final, key_list)
    if key_initial <= key <= key_final:
        sl.add_last(key_list, key)
    if key < key_final:
        keys_range(root['right'], key_initial, key_final, key_list)

    return key_list


def values(my_rbt, key_initial, key_final):
    value_list = sl.new_list()
    values_range(my_rbt['root'], key_initial, key_final, value_list)
    return value_list


def values_range(root, key_initial, key_final, value_list):
    if root is None:
        return value_list
    key = rbt_node.get_key(root)

    if key_initial < key:
        values_range(root['left'], key_initial, key_final, value_list)
    if key_initial <= key <= key_final:
        sl.add_last(value_list, rbt_node.get_value(root))
    if key < key_final:
        values_range(root['right'], key_initial, key_final, value_list)

    return value_list

    