class Test:

    def __init__(self, data_list):
        self.data_list = data_list

    def list_as_string(self):
        return [str(ele) for ele in self.data_list]

    def list_as_int(self):
        return [int(ele) for ele in self.data_list]


obj = Test([1, 5, 6, 7, 8])
print(obj)
print(obj.data_list)
new_obj = obj.list_as_string()
print(new_obj)
new_obj = obj.list_as_int()
print(new_obj)
