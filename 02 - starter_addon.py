# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:07:01 2020

@author: Angad
"""

def single_prec(recom_list,threshold):
    count = 0
    short_list = recom_list[0:12]
 
    for rl in short_list:
        #print(rl[1])
        if rl[1]>=threshold:
            count = count + 1

    recom_list_size = len(short_list)

    return count/recom_list_size

def single_prec_hybrid(recom_list,threshold):
    count = 0
    short_list = recom_list[0:25]
 
    for rl in short_list:
        #print(rl[1])
        if rl[1]>=threshold:
            count = count + 1

    recom_list_size = len(short_list)

    return count/recom_list_size


def global_prec(user_count,func):
    
    global_res = 0
    for i in range(1,user_count+1):
        i2 = str(i)
        curr = top_n[i2]
        curr_prec = func(curr,3.5)
        #print(curr_prec)
        global_res = global_res + curr_prec*100
    
    return global_res/user_count

def global_prec2(user_count,func):
    
    global_res = 0
    for i in range(1,user_count+1):
        i2 = str(i)
        curr = top_n2[i2]
        curr_prec = func(curr,4)
        #print(curr_prec)
        global_res = global_res + curr_prec*100
    
    return global_res/user_count
#
def global_prec_hybrid(user_count,func):
    
    global_res = 0
    for i in range(1,user_count+1):
        i2 = str(i)
        curr = top_n_hybrid[i2]
        curr_prec = func(curr,3.5)
        #print(curr_prec)
        global_res = global_res + curr_prec*100
    
    return global_res/user_count

def diversity_in_top_n(user_count):
	global_res = set()
	for i in range(1,user_count+1):
		i2 = str(i)
		curr = top_n[i2]
		for mv in curr[0:5]:
			global_res.add(mv[0])
	return len(global_res)

def diversity_in_top_n2(user_count):
	global_res = set()
	for i in range(1,user_count+1):
		i2 = str(i)
		curr = top_n2[i2]
		for mv in curr[0:5]:
			global_res.add(mv[0])
	return len(global_res)
    
#
def diversity_in_top_n_hybrid(user_count):
	global_res = set()
	for i in range(1,user_count+1):
		i2 = str(i)
		curr = top_n_hybrid[i2]
		for mv in curr[0:5]:
			global_res.add(mv[0])
	return len(global_res)



def spliceLists(lst1, lst2): 
    return [sub[item] for item in range(len(lst2)) 
                      for sub in [lst1, lst2]] 

top_n_hybrid = {}



for i in range(1,len(top_n)+1):
    temp_list = spliceLists(top_n[str(i)],top_n2[str(i)])
    top_n_hybrid[str(i)] = temp_list


    
for i in range(1,len(top_n_hybrid)+1):
    
    list_of_lists = [list(elem) for elem in top_n_hybrid[str(i)]]
    top_n_hybrid[str(i)] = list_of_lists
    
    
#MODEL 1 IS SVD
#    MODEL 2 IS KNN

for i in range(1,len(top_n_hybrid)+1):
    
    for j in range(len(top_n_hybrid['1'])):
        if j%2 == 0:
            top_n_hybrid[str(i)][j].append(1)
        else:
            top_n_hybrid[str(i)][j].append(2)
            
for i in range(1,len(top_n_hybrid)+1):
    i2 = str(i)
    curr_list = top_n_hybrid[i2]
    for mv in curr_list:
        if mv[2] == 2:
            #print("oh no")
            new_pred_val = algo.predict(i2,mv[0],3.4)
            mv[1] = new_pred_val[3]
            mv[2] = 1

Movies_fixed=pd.read_csv("ml-latest-small/movies_fixed.csv",encoding="ISO-8859-1")
Ratings_fixed=pd.read_csv("ml-latest-small/ratings_fixed.csv",encoding="ISO-8859-1")

print("Precision of Early SVD Model:", global_prec(len(top_n),single_prec))
print("Diversity in Early SVD Top N:",diversity_in_top_n(len(top_n)),"unique items found.")

print("Precision of Early KNN Model:", global_prec2(len(top_n2),single_prec))
print("Diversity in Early KNN Top N:",diversity_in_top_n2(len(top_n2)),"unique items found.")


print("Precision of Early Hybrid Model:", global_prec_hybrid(len(top_n_hybrid),single_prec_hybrid))
print("Diversity in Early Hybrid Top N:",diversity_in_top_n_hybrid(len(top_n_hybrid)),"unique items found.")
    
def sort_list(list1, list2): 
  
    zipped_pairs = zip(list2, list1) 
  
    z = [x for _, x in sorted(zipped_pairs)] 
      
    return z 

top_n_hybrid_sorted = {}

def sortByLastRatedDate(recom_list):
    
    for i in range(1,611):
        curr_user = str(i)
        
        
        curr_list = recom_list[curr_user]
        
        datesList = []
        for movie in curr_list:
            curr_mv_id = int(movie[0])
         
            curr_mv_date = Movies_fixed.at[curr_mv_id-1,'LastRated']
            datesList.append(curr_mv_date)
        
        z_list = sort_list(curr_list,datesList)
        
        recom_list[curr_user] = z_list
    
sortByLastRatedDate(top_n)
sortByLastRatedDate(top_n2)
sortByLastRatedDate(top_n_hybrid)
 


#print("Precision of SVD Model:", global_prec(len(top_n),single_prec))
#print("Diversity in SVD Top N:",diversity_in_top_n(len(top_n)),"unique items found.")
#
#print("Precision of KNN Model:", global_prec2(len(top_n2),single_prec))
#print("Diversity in KNN Top N:",diversity_in_top_n2(len(top_n2)),"unique items found.")
#
#print("Precision of Hybrid Model:", global_prec_hybrid(len(top_n_hybrid),single_prec_hybrid))
#print("Diversity in Hybrid Top N:",diversity_in_top_n_hybrid(len(top_n_hybrid)),"unique items found.")
#
#
#final_sum = 0
#final_count= 0
#for pt0 in range(1,611):
#    curr_recoms = top_n[str(pt0)]
#
#    for x in curr_recoms:
#        final_sum = final_sum + x[1]
#        final_count = final_count + 1
#
#
#
#print(final_sum/final_count)
#final_sum = 0
#final_count= 0
#for pt0 in range(1,611):
#    curr_recoms = top_n2[str(pt0)]
#
#    for x in curr_recoms:
#        final_sum = final_sum + x[1]
#        final_count = final_count + 1
#
#print(final_sum/final_count)
#final_sum = 0
#final_count= 0
#for pt0 in range(1,611):
#    curr_recoms = top_n_hybrid[str(pt0)]
#
#    for x in curr_recoms:
#        final_sum = final_sum + x[1]
#        final_count = final_count + 1
#
#print(final_sum/final_count)





#this code might be removed, it used the last recommended date instead
#however a later model could use that data as well
#hmmm


#for i in range(1,len(top_n_hybrid)+1):
#    i2 = str(i)
#    #print("User",i2)
#    curr_recoms = top_n_hybrid[i2]
#    curr_date = mymetadata['last_date']
#    y2,m2,d2 = [int(x) for x in curr_date.split('-')]
#    date2 = date(y2,m2,d2)
#    for mv in curr_recoms:
#        
#        mvid = mv[0]
#        movies2rowid = int(mvid)-1
#        prev_date = Movies_fixed.iloc[movies2rowid,4]
#        
#        
#        y1,m1,d1 = [int(x) for x in prev_date.split('-')]
#        date1 = date(y1,m1,d1)
#        
#                
#        if(date2>date1):
#            Movies_fixed.at[movies2rowid,4] = curr_date
