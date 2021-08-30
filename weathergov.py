def get_properties(dict:dict):
    return(dict['properties'])

#feed this properties
def get_number(number:int,dict:dict):
    for i in dict["periods"]:
        if i["number"] == number:
            return i

#give this properties
def get_param(number:int,dict:dict,name:str):
    for i in dict["periods"]:
        if i ["number"] == number:
            return i[name]


#also feed this the properties
def get_largest_number(dict:dict):
    for i in dict["periods"]:
        prev_num = 0
        if int(i["number"])>prev_num:
            prev_num = int(i["number"])
    return prev_num

def get_all_params(dict:dict,searchterm:str):
    lst = []
    for i in dict["periods"]:
        for x in i:
            if x == searchterm:
                lst.append(i[searchterm])
                
                #lst.append(i[searchterm])
    return lst