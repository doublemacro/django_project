import pytest

from tests.to_test import extract_odd_numbers, extract_even_numbers, build_dict, Dog, Heap

def test_extract_odd_numbers():
    list1 = [3, 5, 6, 7, 8, 10]
    list_result = [3, 5, 7]
    assert extract_odd_numbers(list1) == list_result
    assert extract_odd_numbers([33, 45, 1001]) == [33, 45, 1001]
    assert extract_odd_numbers([4, 6, 8]) == []
    assert extract_odd_numbers([]) == []

def test_extract_even_numbers():
    assert extract_even_numbers([1, 3, 4, 6, 8]) == [4, 6, 8]
    assert extract_even_numbers([100]) == [100]
    assert  extract_even_numbers([]) == []

def test_build_dict():
    list1 = [4, 5, 6, 10, 20, 21]
    result = {
        "odd": [5, 21],
        "even": [4, 6, 10, 20]
    }
    assert build_dict(list1) == result
    assert build_dict([]) == {"odd": [], "even": []}
    assert build_dict([-1]) == {"odd": [-1], "even": []}

def test_dog_class():
    # testing from_string method. should receive .from_string("Shadow-4-2")
    dog1 = Dog.from_string("Shadow-4-2")
    assert isinstance(dog1, Dog)
    assert dog1.name == "Shadow"
    assert dog1.legs == 4
    assert dog1.age == 2

    dog2 = Dog("Spot", 4, 2)
    dog3 = Dog("Spot2", 4, 5)
    assert Dog.is_adult(dog2.age) == False
    assert Dog.is_adult(dog3.age) == True

    # Not recommended
    assert dog1.to_string() == "This dog's name is {name}, it has {legs} legs, and is of {age} years of age.".format(name="Shadow", legs=4, age=2)


def test_heap_functionality():
    h = Heap()
    h.push(4)
    assert h.peek() == 4
    assert h.size() == 1

    h.push(20)
    assert h.peek() == 20
    assert h.size() == 2
    assert h.pop() == 20
    assert h.size() == 1

    assert h.is_empty() == False
    h.pop()
    assert h.is_empty() == True
