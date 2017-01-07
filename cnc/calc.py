import math as _M

def cnc_calc(i_data={}):
    """
    The function needs the following data, which of one parameter
    should be left out.
        "rpm": 0, #ex. 15000 - 18000
        "cl_mm": 0.0, #chip load mm, ex. 0.38
        "fr_mmin": 0.0, #feed rate meter/min, ex. 5
        "n_teeth": 0, #no of teeth, ex. 1 for single flute
        "cut_depth": (optional, default 1.0 diameter of bit) 
    """    
    data = {
        "rpm": 0, #ex. 15000 - 18000
        "cl_mm": 0.0, #cut load mm, ex. 0.38
        "fr_mmin": 0.0, #feed rate mm/min, ex. 80
        "n_teeth": 0, #no of teeth, ex. 1 for single flute
        "cut_depth": 1.0    #cut-depth in times of bit diameter
                            #reduces chip if bigger than 1.0
        }
    data.update(i_data)
    RPM = data["rpm"]
    T = data["n_teeth"]
    reduce_r = 1.0 - (data["cut_depth"] - 1) * 0.25
    CL = data["cl_mm"] * reduce_r
    FR = data["fr_mmin"]

    one_unknown = False
    ret_str = ""
    for k in data:
        if data[k] == 0:
            if one_unknown:
                one_unknown = False
                raise ValueError("More than one unknown provided!")
                break
            else:
                ret_str += k
                one_unknown = True

    if ret_str == "rpm":
        ret_val = 1000 * FR / (T * CL)
    elif ret_str == "cl_mm":
        ret_val = reduce_r * 1000 * FR / (RPM * T)
    elif ret_str == "fr_mmin":
        ret_val = RPM * T * CL / 1000
    elif ret_str == "n_teeth":
        ret_val = 1000 * FR / (RPM * CL)
    else:
        raise Exception("Some error!")

    return ret_str, ret_val
        
                
