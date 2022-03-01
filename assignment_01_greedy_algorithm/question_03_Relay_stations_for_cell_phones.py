def number_stations(distances, x):
    amount_stations = 1
    updated_distance = 0
    for distance in distances:
        if distance + updated_distance > 2*x:
            updated_distance = distance
            amount_stations += 1
        else:
            updated_distance += distance
    return amount_stations




print(number_stations([5, 2, 8, 7], 10))
