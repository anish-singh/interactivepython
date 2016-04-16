'''
Created on Apr 16, 2016

@author: anishsingh1
'''

class MyHashtable:

    def __init__(self):
        self.table_size = 3
        self.size = 0
        self.keys = [None]*self.table_size
        self.values = [None]*self.table_size
        
    def add(self, k, v):
        
        if (self.size +1) > self.table_size:
            self.resize()
            
            
        index = self.hash(k)
        
        if not self.keys[index]:
            # nothing at the hash.
            self.keys[index] = k
            self.values[index] = v
            self.size += 1
        elif self.keys[index] == k :
            # same key, different value. replace
            self.values[index] = v
        else:
            # collision. 2 keys hash to same index. look for next index
            nextIndex = self.rehash(index)
            while self.keys[nextIndex] != None  and self.keys[nextIndex] != k :
                nextIndex = self.rehash(nextIndex)
            
            self.keys[nextIndex] = k
            self.values[nextIndex] = v
            self.size += 1

        
    
    def get(self, k):
        
        index = self.hash(k)
        
        if self.keys[index] == None: return None
        
        if self.keys[index] == k:  return self.values[index]
        
        # collision. 
        nextIndex = self.rehash(index)
        while self.keys[nextIndex] != None:
            if self.keys[nextIndex] == k:
                return self.values[nextIndex]
            else:
                nextIndex = self.rehash(nextIndex)
        return None
    
    
    def resize(self):
        
        primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43]
        
        next_size = self.table_size
        for next_size in primes:
            if next_size > self.table_size *2:
                break
        self.table_size = next_size
        
        print 'resizing to new_size =%d' %(next_size)

        
        old_keys = self.keys
        old_values = self.values
        
        self.keys = [None] * self.table_size
        self.values = [None] * self.table_size
        
        for k,v in zip(old_keys, old_values):
            if k:
                self.add(k,v)
        

        
    def hash(self, k):
        # assumes integer key
        return k % self.table_size
    
    def rehash(self, k):
        return (k +1) % self.table_size
    
    def delete(self, k):
        pass
  
class MyHashWithChaining:
    
    def __init__(self):
        self.table_size = 3
        self.size = 0
        self.buckets = [None] * self.table_size
        
    def add(self, k, v):
        index = self.hash(k)
        
        if self.buckets[index] == None:
            self.buckets[index] = []
            self.buckets[index].append([k,v])
            self.size +=1 
        elif self.buckets[index]:
            key_exists = False
            for t in self.buckets[index]:
                if (t[0] == k):
                    # replace
                    key_exists = True
                    t[1] = v
                    break
            if not key_exists:
                self.buckets[index].append([k,v])
                self.size += 1
    
    
    def get(self, k):
        index = self.hash(k)
        
        if self.buckets[index] == None: return None
        
        for t in self.buckets[index]:
            if t[0] == k:  return t[1]
        return None
            
    def hash(self, k):
        # assumes integer key
        return k % self.table_size
        

def main():
    t = MyHashWithChaining()
    t.add(3,'A')
    t.add(2,'B')
    t.add(1,'C')
    t.add(3,'D')
    t.add(4,'E')
    
    print t.get(4)
    print t.get(3)
    print t.get(2)
    print t.get(1)
    print t.get(0)
    
    
if __name__ == '__main__':
    main()    