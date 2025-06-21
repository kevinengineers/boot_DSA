def does_name_exist(first_names, last_names, full_name):
    for first_name in first_names:
        for last_name in last_names:
            full_name_nowhitespace = ('').join(full_name.split(' '))
            current_name = first_name + last_name

            if full_name_nowhitespace == current_name:
                return True

    return False

test1 = does_name_exist(
    ["kevin", "james", "bob", "kramer", "steve"],
    ["stevens", "adams", "staven", "nester", "watke"],
    "kevin watke")

print("test 1: ", {test1})
