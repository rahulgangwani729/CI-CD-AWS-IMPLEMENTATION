import json
import pandas as pd
import requests

def lambda_handler(event, context):
    
    print("Event Data -> ", event)
    response = requests.get("https://www.google.com/")
    print(response.text)
    
    d = {'col1': 1, 'col2': 3}
    df = pd.DataFrame(data=d)
    print(df)
    print("Demo completed !!!")
    