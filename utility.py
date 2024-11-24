
# utilities 

def replaceLine(strList, str_pattern, newstr)->bool:
    index = _findLineIndex(strList, str_pattern)
    #index check
    if index >len(strList):
        return False
    else : #replace 
        strList = _replace(strList, str_pattern, newstr, index)
        return True


def _findLineIndex(strList, str_pattern)->int:

    #find which line the string is in 
    index = 0
    for line in strList:
        if str_pattern in line:
            print(f"found line \"{line}\" at index : {index}")
            return index
        
        index += 1
    return -1

def _replace(strList, str_pattern, newstr, index)->list:

    if str_pattern in strList[index]:
        #replace 
        strList[index] = newstr
        if newstr == strList[index] :
            return strList

    return []
