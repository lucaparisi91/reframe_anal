import json
import pandas as pd
import numpy as np

def get_test_description(test_case):
    row={}
    args=test_case["name"].split("%")
    args[0]=f"name={args[0]}"
    for (key,value) in [ arg.split("=") for arg in args ]:
        row[key]=value
    return row

def get_test_performance_metrics(test_case):
    rows=[]
    
    if test_case["perfvars"] is not None:
        
        for perf_var in test_case["perfvars"]:
            row={}
            row["metric"]=perf_var["name"]
            row["value"]=perf_var["value"]
            rows.append(row)
    return rows


def get_performance_metrics(j):
    rows=[]
    for run in j["runs"]:
        if "testcases" in run.keys():
            for test_case in run["testcases"]:
                metrics=get_test_performance_metrics(test_case)
                description=get_test_description(test_case)
                rows=rows + [ { **description , **metric } for metric in metrics ]
                
    return pd.DataFrame(rows)


def load_performance_metrics(json_files):
    js=[]
    for json_file in json_files:
        with open(json_file) as f:
            j=json.load(f)
            js.append(j)
    data=pd.concat([get_performance_metrics(j) for j in js])
    
    return data