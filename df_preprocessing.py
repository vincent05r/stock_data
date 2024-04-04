import pandas as pd

def convert_to_pct(df:pd.DataFrame, list_axis=["open", "high", "low"], drop_inplace=False, drop_NA=False):
    
    for item in list_axis:
        
        output = df[item].pct_change() * 100
        new_str = item + "_pct_change"
        df[new_str] = output
    

    if drop_NA:
        df.dropna(inplace=True)


    if drop_inplace:
        df.drop(list_axis, axis=1, inplace=True)





def drop_zeros_filter(row, list):

    ct = 0

    for i in list:
        if row[i] == 0:
            ct += 1
    
    if ct >= int(len(license) * 0.6):
        return False
    else:
        return True
