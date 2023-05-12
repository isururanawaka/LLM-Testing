import openai
import json
import requests
import time

openai.api_key = "None"
model_engine = "gpt-3.5-turbo"


def download_github_file(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as f:
        f.write(response.content)


def process(file_path):
    with open(file_path, 'r') as file:
        accuracy = 0;
        for line in file:
            if line.strip() and line.startswith("https"):
              values = line.strip().split()
              if len(values) >= 2:
               first = values[0]
               second = values[1]
               download_github_file(first, 'temp.txt')  # or do whatever operation you need to do with each line
               content = read_file('temp.txt')
               response = get_chat_gpt_result("list  set of method parameters in  the code " + content)
               print(response)
               data = json.loads(json_string)
               count = data['total_parameter_count']
               accuracy =  calculate_accuracy(accuracy,second,count)
              elif len(values) == 1:
               download_github_file(line.strip(), 'temp.txt')  # or do whatever operation you need to do with each line
               content = read_file('temp.txt')
               response = get_chat_gpt_result("list  set of method parameters in  the code " + content)
               print(response)
            time.sleep(35)
        return accuracy

def read_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content


def get_chat_gpt_result(promt):
    response = openai.ChatCompletion.create(
        model=model_engine, messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "exactly list all method parameters in this python code in pure  json format without special characters as {results: [{name:'methodname',parameters:['a','b','c'],count:3}], total_parameter_count:3} " + promt},
          ],
        n=1, stop=None, temperature=0)

    return response.choices[0]['message']['content']

def calculate_accuracy(accuracy,second, count):
    if second >= count:
       if accuracy > 0 :
          accuracy  =  accuracy  + (count/second)*100
       else :
          accuracy = (count/second)*100
    else:
       if accuracy > 0 :
          accuracy  =  accuracy  + (second/count)*100
       else :
          accuracy = (second/count)*100

acc = process('../resources/urls.txt')
print("accuracy:",acc)
