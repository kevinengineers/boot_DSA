"""
Implement the last_work_experience function. It takes a list of our player's
work history (strings) and returns the last place they worked.

    Assume the list is ordered from oldest to most recent.
    If the list is empty, return None.

"""


def last_work_experience(work_experiences):
    if len(work_experiences) == 0:
        return None
    return work_experiences[-1]


print(last_work_experience(["target", "walmart", "costco"]))
