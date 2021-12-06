from random import randint

import pytest

from bst import BST


TEST_DATA = 10, 10, 5, 3, 20, 15, 70, 30, 8, 7, 4, 9, 2, 2


@pytest.fixture
def bst():
    return BST(*TEST_DATA)


def test_bst_contains(bst):
    for value in TEST_DATA:
        assert bst.contains(value)
    for value in [i if i not in TEST_DATA else -1 for i in [randint(0, 100) for _ in range(0, 100)]]:
        assert not bst.contains(value)


def test_bst_contains_with_exception(bst):
    with pytest.raises(TypeError):
        bst.contains({1: 2})


def test_bst_insert(bst):
    to_add = 21
    expected = list(set(TEST_DATA))
    expected.append(to_add)
    expected = tuple(sorted(expected))

    bst.insert(to_add)

    assert bst.contains(to_add)
    assert tuple(bst.dft('inorder')) == expected


def test_bst_insert_with_exception(bst):
    with pytest.raises(TypeError):
        bst.insert('12')


def test_bst_remove(bst):
    to_remove = 20
    expected = list(set(TEST_DATA))
    del expected[expected.index(to_remove)]
    expected = tuple(sorted(expected))

    bst.remove(to_remove)

    assert not bst.contains(to_remove)
    assert tuple(bst.dft('inorder')) == expected


def test_bst_remove_with_exception(bst):
    with pytest.raises(TypeError):
        bst.remove([1, 2, 3])


@pytest.mark.parametrize(
    'data, expected',
    (
        (TEST_DATA, (10, 5, 20, 3, 8, 15, 70, 2, 4, 7, 9, 30)),
        ((), ()),
        ((10,), (10,)),
    )
)
def test_bst_bft(data, expected):
    bst = BST(*data)
    assert tuple(bst.bft()) == expected


@pytest.mark.parametrize(
    'order, data, expected',
    (
        ('inorder', TEST_DATA, (2, 3, 4, 5, 7, 8, 9, 10, 15, 20, 30, 70)),
        ('inorder', (), ()),
        ('inorder', (10,), (10,)),
        ('preorder', TEST_DATA, (10, 5, 3, 2, 4, 8, 7, 9, 20, 15, 70, 30)),
        ('preorder', (), ()),
        ('preorder', (10,), (10,)),
        ('postorder', TEST_DATA, (2, 4, 3, 7, 9, 8, 5, 15, 30, 70, 20, 10)),
        ('postorder', (), ()),
        ('postorder', (10,), (10,)),
    )
)
def test_bst_dft(order, data, expected):
    bst = BST(*data)
    assert tuple(bst.dft(order)) == expected
