def fastest_path(e1, x1, a_list_1, t_list_1, e2, x2, a_list_2, t_list_2):
    f1_list = [e1 + a_list_1[0]]
    pred_1_list = []
    f2_list = [e2 + a_list_2[0]]
    pred_2_list = []
    for j in range(2, len(a_list_2)):
        same_line_1 = f1_list[j - 1] + a_list_1[j]
        change_line_1 = f2_list[j - 1] + t_list_2[j - 1] + a_list_1[j]
        if same_line_1 < change_line_1:
            f1_list[j] = same_line_1
            pred_1_list[j] = 1
        else:
            f1_list[j] = change_line_1
            pred_1_list[j] = 2

        same_line_2 = f2_list[j - 1] + a_list_2[j]
        change_line_2 = f1_list[j - 1] + t_list_1[j - 1] + a_list_2[j]
        if same_line_2 < change_line_2:
            f2_list[j] = same_line_2
            pred_2_list[j] = 2
        else:
            f2_list[j] = change_line_2
            pred_2_list[j] = 1

    if f1_list[-1] + x1 < f2_list[-1] + x2:
        F = f1_list[-1] + x1
        last = 1
        pred = pred_1_list
    else:
        F = f2_list[-1] + x2
        last = 2
        pred = pred_2_list

    return F, last, pred
