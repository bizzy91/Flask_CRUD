"""
{ 
    "index": 0,
    0: {
        "name": "bizzy",
        "id": "bizzy",
        "password": 1234,
        "state": True
    }
    ...
}
"""
data = {
    "index": 0,
    0: {
        "name": "bizzy",
        "id": "bizzy",
        "password": 1234,
        "state": True
    }
}
def data_init(data):
    data = {
        "index": 0,
        0: {
            "name": "bizzy",
            "id": "bizzy",
            "password": 1234,
            "state": True
        }
    }


# Create
def add_data(data, name, id, password):
    index = data["index"]
    data[index] = {"name": name, "id": id, "password": password, "state": True}
    data["index"] += 1

# Read
def read_data_all(data):
    return data
def read_data(data, index):
    if data[index]["state"]=="True":
        return data[index]
    return 

# Update
def update_data(data, index, name, id, password):
    data[index] = {"name": name, "id": id, "password": password, "state": True}

# Delete
def delete_data(data, index):
    data[index]["state"] = False