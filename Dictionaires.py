my_dic1 = {"age": 20, "sex": "male", "name": "Marty"}
my_dict2 = dict(name="Marty", sex="Male", speed=100)
print(len(my_dict2))
print(type(my_dict2))
my_dict2["beautifulness"] = "100%"

a = my_dic1["age"]
# a = my_dic1.get("sex")
# b = my_dict2.keys()
# b = my_dict2.values()
b = my_dict2.items()

print(b)
