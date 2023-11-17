# Reframe anal

Contains tools to analyse json outputs. 

- load_performance_metrics( files)
    Creates a pandas Dataframe with all performance metrics from a list of json files emitted from reframe.
    
```python
import reframe_anal.reframe_anal as rfa

json_files=["benchio_work3.json","benchio_work4.json"]
rfa.load_performance_metrics(json_files)
```