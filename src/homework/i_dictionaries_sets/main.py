import dictionary
list1 = ['T','T','T']
list2 = ['G','A','T']
list3 = ['T','T','T']
#dic1 = {"1":list1,"2":list2,"3":list3}
#dic2 = {}
#print(dic1)
list = [list1, list2, list3]
"""
results = [[],[],[]]
count = 0
for c in range(len(list)):
        for d in range(len(list[c])):
            if (list[c][d]=="T"):
                count += 1
            results[c].append(count)
        count = 0



print(results)
"""
 	
#list1 = ['T','T','T','C','C','A','T','T','T','A']
  	
#list2 = ['G','A','T','T','C','A','T','T','T','C']
  	
#list3 = ['T','T','T','C','C','A','T','T','T','T']
  	
#list4 = ['G','T','T','C','C','A','T','T','T','A']

#dict2 = {0:list1,1:list2,2:list3,3:list4}

#print(dictionary.get_p_distance_matrix(dict2))

def main():
    list1 = ['T','T','T','C','C','A','T','T','T','A']  	
    list2 = ['G','A','T','T','C','A','T','T','T','C']  	
    list3 = ['T','T','T','C','C','A','T','T','T','T']	
    list4 = ['G','T','T','C','C','A','T','T','T','A']

    list5 = [list1, list2, list3, list4]

    results = dictionary.get_p_distance_matrix(list5)
    print(results)

main()