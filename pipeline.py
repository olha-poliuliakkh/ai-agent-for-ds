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

r = resp(pr.query_type_classifier_prompt, pr.test_3)
req = int(r.choices[0].message.content.strip())
print("Classification result (req):", req)

model_to_use = classify_task(req)

code, result = generate_code(pr.code_generation_prompt.format(df = my_set_df, model_to_use = model_to_use), pr.test_3, "my_set_df", my_set_df)
print("Final code: ", code)
print("Result: ", result)