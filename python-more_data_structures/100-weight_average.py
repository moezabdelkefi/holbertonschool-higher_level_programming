#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == "":
        return 0
    total_weight = sum(weight for score, weight in my_list)
    weighted_sum = sum(score * weight for score, weight in my_list)
    return weighted_sum / total_weight
