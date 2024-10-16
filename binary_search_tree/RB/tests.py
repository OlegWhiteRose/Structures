import unittest
import random
from main import Dict

class TestDict(unittest.TestCase):

    def setUp(self):
        self.dict_tree = Dict()

    def test_bulk_insertion_and_retrieval(self):
        num_elements = 1000
        data = {random.randint(1, 10000): f"Value{i}" for i in range(num_elements)}
        for key, value in data.items():
            self.dict_tree[key] = value
        for key, value in data.items():
            self.assertEqual(self.dict_tree[key], value)

    def test_random_deletion(self):
        num_elements = 500
        data = {random.randint(1, 10000): f"Value{i}" for i in range(num_elements)}
        for key, value in data.items():
            self.dict_tree[key] = value
        keys = list(data.keys())
        for _ in range(250):
            key_to_delete = random.choice(keys)
            del self.dict_tree[key_to_delete]
            keys.remove(key_to_delete)
            with self.assertRaises(KeyError):
                _ = self.dict_tree[key_to_delete]
        for key in keys:
            self.assertTrue(key in self.dict_tree)

    def test_update_existing_keys(self):
        num_elements = 100
        data = {random.randint(1, 1000): f"Value{i}" for i in range(num_elements)}
        for key, value in data.items():
            self.dict_tree[key] = value
        for key in data.keys():
            new_value = f"Updated{data[key]}"
            self.dict_tree[key] = new_value
            self.assertEqual(self.dict_tree[key], new_value)

    def test_contains_after_bulk_insertions_and_deletions(self):
        num_elements = 1000
        data = {random.randint(1, 10000): f"Value{i}" for i in range(num_elements)}
        for key, value in data.items():
            self.dict_tree[key] = value
        keys = list(data.keys())
        for _ in range(500):
            key_to_delete = random.choice(keys)
            del self.dict_tree[key_to_delete]
            keys.remove(key_to_delete)
        for key in keys:
            self.assertTrue(key in self.dict_tree)
        for key in data.keys():
            if key not in keys:
                self.assertFalse(key in self.dict_tree)

    def test_len_after_bulk_operations(self):
        num_elements = 1000
        data = {random.randint(1, 10000): f"Value{i}" for i in range(num_elements)}
        for key, value in data.items():
            self.dict_tree[key] = value
        self.assertEqual(len(self.dict_tree), num_elements)
        for _ in range(500):
            key_to_delete = random.choice(list(data.keys()))
            del self.dict_tree[key_to_delete]
            data.pop(key_to_delete)
        self.assertEqual(len(self.dict_tree), 500)

def myTests():
    tree = Dict()
    items = set()
    map = {}
    for i in range(1, 232122):
        item = random.randint(1, 2312233)
        tree[item] = random.randint(1, 3221213)
        map[item] = tree[item]
        items.add(item)

        flag = random.randint(1, 10)
        if flag >= 8:
            del tree[item]
            del map[item]
            items.remove(item)

    print(tree.is_balanced(tree.root))
    print(len(tree) == len(items))

    flag = True 
    for x in map:
        if map[x] != tree[x]:
            flag = False

    print(flag)

    for x in map:
        map[x] = random.randint(1, 13123213)
        tree[x] = map[x]

    flag = True 
    for x in map:
        if map[x] != tree[x]:
            flag = False

    print(flag)

    #print(items)
    for item in items:
        #print(f"Doing {item}")
        #tree.show()
        del tree[item]

    items = set()
    arr = []
    for i in range(1, 300000):
        arr.append(i)
        tree[i] = ""
        items.add(i)
    
    random.shuffle(arr)
    for i in arr[:random.randint(1, 3000)]:
        del tree[i]
        items.remove(i)

    print(len(tree), len(items))

def findedIssue():
    tree = Dict()
    items = [9, 20, 22]
    for i in items:
        tree[i] = '1'
    for i in items:
        print(f"Doing {i}")
        tree.show()
        del tree[i]

def AVL_tests():
    tree = Dict()
    
    tree[40] = 2
    tree[30] = 5
    tree[25] = 18
    tree[15] = 12
    tree[10] = 124
    tree[5] = 124
    tree[2] = 123
    tree[1] = 13123
    tree[7] = 213
    tree[8] = 213
    tree[9] = 213
    tree.show()
    print(tree.is_balanced(tree.root))
    return 
    items = [40, 30, 25, 15, 10, 5, 2, 1, 7, 8, 9]
    random.shuffle(items)

    print(items)
    for item in items:
        print("Deleting: ", item, "...")
        tree.show()
        del tree[item]

if __name__ == "__main__":
    AVL_tests()
    #myTests()
    #findedIssue()
    #unittest.main()
