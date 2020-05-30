import json

class Vendor:

    def __init__(self, attr_list):
        self.name = attr_list[0]
        self.number = attr_list[1]
        self.mail = attr_list[2]
        self.phone = attr_list[3]
        self.country = attr_list[4]

    def __repr__(self):
        return self.name

class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = Node()

    def append(self,data):
        new_node = Node(data)
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def length(self):
        cur_node = self.head
        total = 0
        while cur_node.next != None:
            cur_node = cur_node.next
            total += 1
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx += 1

    def __getitem__(self, index):
        return self.get(index)

def get_vendors(file_name):

    with open(file_name) as json_f:
        db = json.load(json_f)

    vendors = []
    for dict in db['vendor-db']['vendors']:
        attr_list=[]
        for key in dict:
            attr_list.append(dict[key])
        else:
            v = Vendor(attr_list)
            vendors.append(v)

    vendor_linkedlist = Linked_list()

    for vendor in vendors:
        vendor_linkedlist.append(vendor)

    return vendor_linkedlist

def new_vendor(attrs_list):
    v = Vendor(attrs_list)
    vendors.append(v)

vendors = get_vendors('data.json')
new_vendor(['Brand-new Supplier','99999999','supplier_x@mail.com','+49 989 988 998', 'France'])

vendors.display()

print(vendors[0].mail)
print(vendors[1].mail)
print(vendors[3].phone)
