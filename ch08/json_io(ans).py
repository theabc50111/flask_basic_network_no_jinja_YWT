# --------------Practice start--------------
import json
# --------------Practice end--------------

# --------------Practice start--------------
# json format string to python data
json_array_str = '[10, "a"]'
json_obj_str = '{"A":1, "B":true}'  # true, not True
print(f"json.loads(json_array_str): {json.loads(json_array_str)}")
print(f"json.loads(json_obj_str): {json.loads(json_obj_str)}")

# python data to json format string
l1 = [20, "b"]
d1 = {"C":1, "D":False, "E":l1, "F":{"f1":3, "f2":4}}
print(f"json.dumps(l1): {json.dumps(l1)}")
print(f"json.dumps(d1): {json.dumps(d1)}")

# load json file
with open("./example.json", "r") as f:
    load_json = json.load(f)
    print(f"type(load_json):{type(load_json)}\nload_json:{load_json}")

# dump to json file
with open("./l1.json", "w") as f:
    json.dump(l1, f)
with open("./d1.json", "w") as f:
    json.dump(d1, f)  # check boolean value of result
# --------------Practice end--------------

print("-"*50)
wrong_json_obj_str = "{'A':1, 'B'=True}"  # json's key must be enclosed in double quotes
print(json.loads(wrong_json_obj_str))