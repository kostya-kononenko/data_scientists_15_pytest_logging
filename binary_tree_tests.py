import pytest
from binary_tree import Tree

my_tree = Tree(12)


def test_check_my_node_True():
    assert my_tree.check_my_node(12) is True


def test_check_my_node_False():
    assert my_tree.check_my_node(4) is False


def test_add_list_True():
    my_tree.add_from_list([1, 2, 10, 11])
    assert my_tree.check_my_node(1) and my_tree.check_my_node(2) and my_tree.check_my_node(10) \
           and my_tree.check_my_node(11) is True


def test_add_list_False():
    my_tree.add_from_list([1, 2, 10, 11])
    assert my_tree.check_my_node(1) and my_tree.check_my_node(2) and my_tree.check_my_node(10) \
           and my_tree.check_my_node(12) is False


def test_min_node_True():
    assert my_tree.find_min_node() == 1


def test_min_node_False():
    assert my_tree.find_min_node() != 2


def test_max_node_True():
    assert my_tree.find_max_node() == 11


def test_max_node_False():
    assert my_tree.find_max_node() != 10


def test_del_node():
    my_tree.delete_some_node(10)
    assert my_tree.check_my_node(10) is False
