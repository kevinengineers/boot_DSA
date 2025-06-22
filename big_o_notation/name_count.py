def count_names(list_of_lists, target_name):
    target_count = 0

    for list in list_of_lists:
        target_count += list.count(target_name)

    return target_count

