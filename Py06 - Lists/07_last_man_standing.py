def last_man_standing(a_list, step):
    index = 0
    while len(a_list) > 1:
        index = (index + step-1) % len(a_list)
        a_list.remove(a_list[index])
        if index == len(a_list):
            index = 0

    return a_list[0]