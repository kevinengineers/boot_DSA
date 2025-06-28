def power_set(input_set):
    if len(input_set) == 0:
        return [[]]
    all_subsets = [[]]
    for element in input_set:
        subsets_with_element = []
        for subset in all_subsets:
            subsets_with_element.append(subset + [element])
        all_subsets.extend(subsets_with_element)
    return all_subsets
