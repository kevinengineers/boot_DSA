#original function, rewrite this from O(n) to O(1).
def find_last_name(names_dict, first_name):
    for current_first_name, last_name in names_dict.items():
        if current_first_name == first_name:
            return last_name

# O(1)
def updated_find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError as e:
        print(f"{e} not found")
        return None

# test dictionary.
d = {
    "kevin": "watke",
    "james": "mason"
}

# test case for a firstname that exists.
print(updated_find_last_name(d, "kevin"))

# test case for a firstname that doesn't exist.
print(updated_find_last_name(d, "walter"))
