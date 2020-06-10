
def rob(hval, n): 
    if n == 0: 
        return 0
  
    value1 = hval[0] 
    if n == 1: 
        return value1 
  
    value2 = max(hval[0], hval[1]) 
    if n == 2: 
        return value2 

    max_val = None

    for i in range(2, n): 
        max_val = max(hval[i]+value1, value2) 
        value1 = value2 
        value2 = max_val 
  
    return max_val 
   
def main(): 
  
    hval = [1,2,3,1]  
    n = len(hval) 
    print("rob : {}".format(rob(hval, n))) 
  
if __name__ == '__main__': 
    main() 

