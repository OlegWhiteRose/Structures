class Node:
    def __init__(self, key = None, value = None):
        # for common
        self.left = None
        self.right = None
        self.key = key
        self.value = value
        # for AVL
        self.height = 1
        self.parent = None
        

class Dict:
  def __init__(self):
        self.size = 0
        self.root = None    
  

  def height(self, p):
      if p is None:
          return 0
      return p.height


  def bfactor(self, p):
      if p is None:
          return 0
      return self.height(p.right) - self.height(p.left)

  
  def produce_height(self, p):
      hl = self.height(p.left)
      hr = self.height(p.right)
      p.height = max(hl, hr) + 1
  

  def rotate_right(self, p):
      q = p.left

      p.left = q.right
      if q.right is not None:
        q.right.parent = p

      q.right = p
      if p is not None:
        p.parent = q
      
      self.produce_height(p)
      self.produce_height(q)
      
      return q

  
  def rotate_left(self, q):
      p = q.right 

      q.right = p.left
      if p.left is not None:
        p.left.parent = q

      p.left = q
      if q is not None:
        q.parent = p

      self.produce_height(q)
      self.produce_height(p)

      return p
        

  def balance(self, p):
      if p is None:
          return

      self.produce_height(p)
      
      if abs(self.bfactor(p)) < 2:
          return self.balance(p.parent)
      
      parent = p.parent
      if parent is not None:
        if parent.right is not None and parent.right.key == p.key:
            parent = (parent, "r")
        elif parent.left is not None and parent.left.key == p.key:
            parent = (parent, "l")
    
      if self.bfactor(p) == 2:
          if self.bfactor(p.right) < 0:
              p.right = self.rotate_right(p.right)
          
          p = self.rotate_left(p)
      
      if self.bfactor(p) == -2:
          if self.bfactor(p.left) > 0:
              p.left = self.rotate_left(p.left)
          
          p = self.rotate_right(p)

      if parent is None:
          self.root = p
          p.parent = None
          return self.root
      
      if parent[1] == "r":
          parent[0].right = p
          p.parent = parent[0]
      if parent[1] == "l":
          parent[0].left = p
          p.parent = parent[0]
      
      return self.balance(p.parent)
  
  
  def is_balanced(self, v):
      if v is None:
          return True
      
      if abs(self.bfactor(v)) == 2:
          return False
      
      return self.is_balanced(v.left) and self.is_balanced(v.right)


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
        new_node.parent = parent
        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        self.balance(new_node)

        self.size += 1

    
  def __getitem__(self, key):
        parent = self.find_parent(key)
        if parent is not None and parent.key == key:
            return parent.value

        raise KeyError(f"Key {key} not found")
    
    
  def __delitem__(self, key):
        parent = self.find_parent(key)
        saved_bro = None
        
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
                prev.left.parent = prev
                
            node.left = parent.left
            node.right = parent.right

            saved_bro = prev
          
        elif parent.left is not None:
          node = parent.left
        
        else:
          node = None
        
        
        if node is not None:
            if node.right is not None:
                node.right.parent = node
            if node.left is not None:
                node.left.parent = node

        if parent.key == self.root.key:
            self.root = node
            if node is not None:
                node.parent = None
                self.balance(node)
        else:
          root = parent.parent
          if root.right is not None and root.right.key == parent.key:
            root.right = node
          elif root.left is not None and root.left.key == parent.key:
            root.left = node
          else:
            raise RuntimeError("Something GO FUCKING WRONG")
          
          if node is not None:
            node.parent = root 
            self.balance(node) 
          
          self.balance(root)


        if saved_bro is not None:
           self.balance(saved_bro)

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