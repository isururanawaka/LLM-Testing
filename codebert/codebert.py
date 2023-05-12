import torch
from transformers import RobertaTokenizer, RobertaConfig, RobertaModel
from transformers import AutoTokenizer, AutoModel

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
tokenizer = RobertaTokenizer.from_pretrained("microsoft/codebert-base")
model = RobertaModel.from_pretrained("microsoft/codebert-base")
model.to(device)

tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")
nl_tokens = tokenizer.tokenize("return maximum value")
print("nl_tokens", nl_tokens)
code_tokens = tokenizer.tokenize("def max(a,b): if a>b: return a else return b")
print("code_tokens", code_tokens)
tokens = [tokenizer.cls_token] + nl_tokens + [tokenizer.sep_token] + code_tokens + [tokenizer.eos_token]
print("all tokens", tokens)
tokens_ids = tokenizer.convert_tokens_to_ids(tokens)
print("token_ids", tokens_ids)
context_embeddings = model(torch.tensor(tokens_ids)[None, :])[0]
print("context_embeddings", context_embeddings)
torch.Size([1, 23, 768])
