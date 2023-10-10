

#splits top_n_hybrid into 4 separate lists 

#these lists are then offered over 4 weeks


def splitList(lst):
    list_len = len(lst)
    
    #print(list_len)
    
    list_fin = []
    
    twty_perc_len = int(.25*list_len)
    init_pos = 0
    fin_pos = twty_perc_len
    
    
    
    for k in range(4):
        list_temp = lst[init_pos:fin_pos]
        list_fin.append(list_temp)
        init_pos+=twty_perc_len
        fin_pos+=twty_perc_len

    
    return list_fin
        

top_n_a = {}
top_n_b = {}
top_n_c = {}
top_n_d = {}

#first we need to sort this list by last rated date first


        
    



for i in range(1,611):
    curr_user = str(i)
    curr_list = top_n_hybrid[curr_user]
    #I need to sort this by date before the split up
        
    curr_list_split = splitList(curr_list)
        
    top_n_a[curr_user] = curr_list_split[0]
    top_n_b[curr_user] = curr_list_split[1]
    top_n_c[curr_user] = curr_list_split[2]
    top_n_d[curr_user] = curr_list_split[3]
        


