def generate_ref_list(orig_list):
    
    ref_list = []
    
    for i in range(0, len(orig_list)):
        ref_list.append(i)
        
    return ref_list

def find_missing(orig_list, ref_list):
    
    for i in ref_list:
        if i not in orig_list:
            return i
        else:
            pass
        
def final_func(orig_list):
    
    ref_list = generate_ref_list(orig_list)
    
    missing_num = find_missing(orig_list, ref_list)
    
    return missing_num
