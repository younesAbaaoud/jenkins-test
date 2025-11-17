
# def delete_duplicate(list):
#     listfinal = []
#     for i in range(len(list)+1):
#         listfinal.append(list[i])
#         if list[i] == list[i+1]:
#             continue

#     return listfinal


def delete_duplicate(listin):
    listfinal = []
    listfinal.append(listin[0])
    for i in range(1,len(listin)):
        if listin[i] != listin[i-1]:
            listfinal.append(listin[i])
    
    return listfinal



            