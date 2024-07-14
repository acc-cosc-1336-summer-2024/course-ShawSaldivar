#

def get_p_distance(list1, list2):
    count = 0

    for c in range(len(list1)):
        if list1[c]!=list2[c]:
            count = count + 1
    
    return count / len(list1)

def get_p_distance_matrix(list1):
    results = []
    
    for r in range(len(list1)):
        list=[]
        for c in range(len(list1)):   
            list.append(get_p_distance(list1[r],list1[c]))         
        results.append(list)
    return results
            