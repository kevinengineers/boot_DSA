def num_possible_orders(num_posts):
    if num_posts == 0:
        return 1
    
    
    return num_posts * num_possible_orders(num_posts - 1)
 
