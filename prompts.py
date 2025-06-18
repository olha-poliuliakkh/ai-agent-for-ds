system_prompt1 = f''' 
Your task is to classify user queries. There are two categories of queries:
1. Classification (selecting a category for a value)
2. Predicting a dependent value (linear regression)
Return the category using it's number (1 or 2).
''' 

test_1 = f'''
I need to predict a house price in 2027 year.'''


test_2 = f''' 
I need to define is this book a fiction or non-fiction.
'''

test_3 = f''' 
Is this customer a man or a women if their age is 23, annual income is 55 and spending score equals 6? Try to predict it 
using ML methods.
'''



system_prompt21 = ''' 
Use {my_set_df} as dataset, it is saved in variable "df". Generate the code for user's task using {model_to_use}. 
The code need to be in python and ready to be run, 
so there souldn't be any quotes etc, especially "```python". 
Mark all your comments and other non-code words with #.
'''

#system_prompt21.format(my_set_df=123)

system_prompt22 = ''' 
Generate the code for user's task using {model_to_use}. The code need to be in python and ready to be run, 
so there souldn't be any quotes etc, especially "```python". 
Mark all your comments and other non-code words with #.
'''
