import sys
import json
import pandas as pd
from tqdm import tqdm
import openai
import os
import sklearn
import io
import contextlib
import prompts as pr
from calling_gpt import client, resp
from my_funcs import classify_task, generate_code

my_set_df = pd.read_csv("C:\\Users\\Olga\\Downloads\\Mall_Customers.csv")

r = resp(pr.system_prompt1, pr.test_3)
req = r.choices[0].message.content.strip()
print("Classification result (req):", req)

model_to_use = classify_task(req)

# if 'my_set_df' in globals():
#     generate_code(pr.system_prompt21, pr.test_3, 'my_set_df')
# else:
#     generate_code (pr.system_prompt22, pr.test_3)

generate_code(pr.system_prompt21, pr.test_3, 'my_set_df')