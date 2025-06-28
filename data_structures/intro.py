def count_marketers(job_titles):
    num_users = 0
    for title in job_titles:
        if title.lower() == "marketer":
            num_users += 1
    return num_users


"""
Implement the count_marketers function. It should accept a list of strings
(job titles) and return the number of users who've set their title to "marketer
. LockedIn users sometimes use different casing in their titles, so make sure
to account for that.
"""


# should return 2
print(count_marketers(["eng", "something", "marketer", "marketer"]))
print(count_marketers([]))  # Should return 0
