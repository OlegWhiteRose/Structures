class Node:
    def __init__(self, key = None, value = None):
        self.left = None
        self.right = None
        self.key = key
        self.parent_key = None
        self.value = value

class Dict:
  def __init__(self):
        self.size = 0
        self.root = None
            

  def find_parent(self, key):
        parent = None
        cur = self.root
        while cur is not None:
            if key < cur.key:
                if cur.left is None:
                    return cur

                parent = cur
                cur = cur.left

            elif key > cur.key:
                if cur.right is None:
                    return cur

                parent = cur
                cur = cur.right

            elif key == cur.key:
                return cur

        return parent
              
    
  def __setitem__(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
            self.size = 1
            return
      
        parent = self.find_parent(key)
        if parent is not None and parent.key == key:
            parent.value = value
            return
    
        new_node = Node(key, value)
        new_node.parent_key = parent.key
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
            
        self.size += 1

    
  def __getitem__(self, key):
        parent = self.find_parent(key)
        if parent is not None and parent.key == key:
            return parent.value

        raise KeyError(f"Key {key} not found")
    
    
  def __delitem__(self, key):
        parent = self.find_parent(key)
        
        if parent is None or parent.key != key:
            raise KeyError(f"Key {key} not found")
          
        node = None
        if parent.right is not None:
          node = parent.right
          
          if node.left is None:
            node.left = parent.left
          else:
            prev = None
            while node.left is not None:
              prev = node
              node = node.left
            
            prev.left = node.right
            if prev.left is not None:
                prev.left.parent_key = prev.key
            node.left = parent.left
            node.right = parent.right
            
          
        elif parent.left is not None:
          node = parent.left
        
        else:
          node = None
        
        
        if node is not None:
            if node.right is not None:
                node.right.parent_key = node.key
            if node.left is not None:
                node.left.parent_key = node.key

        if parent.key == self.root.key:
            self.root = node
        else:
          root = self.find_parent(parent.parent_key)
          if root.right is not None and root.right.key == parent.key:
            root.right = node
          elif root.left is not None and root.left.key == parent.key:
            root.left = node
          else:
            raise RuntimeError("Something GO FUCKING WRONG")
          
          if node is not None:
            node.parent_key = root.key  
          
        self.size -= 1

    
  def __len__(self):
        return self.size

    
  def __contains__(self, key):
        try:
            self[key]
            return True
        except:
            return False


  def show(self):
        print(self.root.key)
        arr = [self.root.left, self.root.right]
        cnt = 0
        while len(set(arr)) > 1 and cnt < 5:
            for x in arr:
                if x is None:
                    print([], end=" ")
                else:
                    print(x.key, end=" ")
            print()
    
            new_arr = []
            for i in arr:
                if i is None:
                    new_arr += [None, None]
                    continue
                new_arr += [i.left, i.right]
            arr = new_arr[:]

            cnt += 1
    
# import sys
# exec(sys.stdin.read())