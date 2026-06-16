# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

dic={"name":"sravya","course":"python"}
dic=dict(name="sravya",course="python")
dic=dict([("name","sravya"),("course","python")])
print(dic)
print(dic["name"])
print(dic["course"])
#updating a value
dic["name"]="Deepak"
print(dic["name"])
print(dic)

#iterations
for keys in dic:
    print(keys)
for value in dic.values():
    print(value)
for key, value in dic.items():
    print(key,value)

# without iterations

print(dic.keys())
print(dic.values())
print(dic.items())

# pop a value  or remove a value
dic.pop("course")
print(dic)
#update a dictionary by adding new dictionary to old dictionary
dic2={"city":"Austin","state":"Texas","County":"Williamson","country":"United states"}

dic.update(dic2)
print(dic)
dic.popitem()
print(dic)

