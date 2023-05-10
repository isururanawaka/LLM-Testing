import openai
from dill.source import getsource
import time
from codegen import *
import random
import string

openai.api_key = "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"
model_engine = "gpt-3.5-turbo"

def make_fun(parameters):
    return "def f_make_fun({}): pass\n".format(', '.join(parameters))


def cpp_fun(parameters):
    return "int cpp_fun({});".format(', '.join(parameters))

ar = "args_"

num_of_methods = [8]
array_params_no = [32]

#array = [1, 2, 4, 8, 16, 32, 64, 128, 512, 1024]
func =""
for k in range(num_of_methods[0]):
   for i in array_params_no:
        params = []
        for j in range(i):
           params.append(ar+''.join(random.choices(string.ascii_lowercase,k=5)) + str(j))
        func += make_fun(params)
        #func =  cpp_fun(params)
start = time.perf_counter()
response = openai.ChatCompletion.create(
           model='gpt-3.5-turbo',
           messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "exactly list all parameters in this python code " + str(func)},
          ])
end = time.perf_counter() - start
message = response.choices[0]['message']

print("origin {}: time {}: {}".format(i, end, message['content']))

