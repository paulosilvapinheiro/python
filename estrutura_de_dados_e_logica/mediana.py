def mediana(list_num):
    len_list = len(list_num)
    is_par = len_list % 2 == 0
    result = None
    if not is_par:
        med = int(len_list / 2 + 0.5)
        result = list_num[med-1]
    else:
        med = int(len_list / 2)
        result = (list_num[med-1] + list_num[med])/2
    return result