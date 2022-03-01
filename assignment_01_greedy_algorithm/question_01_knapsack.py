def knapsack(items, max_weight):
    items.sort(key=lambda x: x[0] / x[1],reverse=True)
    weight_gained = 0
    value_gained = 0
    for item in items:
        if weight_gained == max_weight:
            break
        if weight_gained + item[1] > max_weight:
            break
        else:
            value_gained += item[0]
            weight_gained += item[1]
    return value_gained


print(knapsack([(105, 70), (60, 60), (50, 50)], 110))
