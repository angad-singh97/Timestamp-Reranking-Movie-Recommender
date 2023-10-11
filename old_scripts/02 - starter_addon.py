# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 23:07:01 2020

@author: Angad
"""



top_n_hybrid = {}

top_n_hybrid_sorted = {}



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
