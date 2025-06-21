def get_avg_brand_followers(all_handles, brand_name):
    brand_occr = 0
    for inner_list in all_handles:
        for handle in inner_list:
            if brand_name in handle:
                brand_occr += 1
    return brand_occr / len(all_handles)


