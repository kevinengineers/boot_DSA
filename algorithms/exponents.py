def get_estimated_spread(audiences_followers):
    average_audience_followers = avg_aud_followers(audiences_followers)
    num_followers = len(audiences_followers)

    return average_audience_followers * (num_followers ** 1.2)
    

def avg_aud_followers(audiences_followers):
    if len(audiences_followers) == 0:
        return 0
    sum = 0
    for follower in audiences_followers:
        sum += follower

    return sum / len(audiences_followers) 
