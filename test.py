import einops
import pickle
import json
from unseal import hooks
from unseal.transformers_util import load_from_pretrained # TODO fix that it doesnt work to directly call unseal.transformes_util

import pysvelte


# model, tokenizer, config = load_from_pretrained('gpt2')

text = "Mr and Mrs Dursley, of number four, Privet Drive, were proud to say that they were perfectly normal, thank you very much. They were the last people you'd expect to be involved in anything strange or mysterious, because they just didn't hold with such nonsense. Mr Dursley was the director of a firm called Grunnings, which made drills. He was a big, beefy man with hardly any neck, although he did have a very large moustache. Mrs Dursley was thin and blonde and had nearly twice the usual amount of neck, which came in very useful as she spent so much of her time craning over garden fences, spying on the neighbours. The Dursleys had a small son called Dudley and in their opinion there was no finer boy anywhere. The Dursleys had everything they wanted, but they also had a secret, and their greatest fear was that somebody would discover it. They didn't think they could bear it if anyone found out about the Potters. Mrs Potter was Mrs Dursley's sister, but they hadn't met for several years; in fact, Mrs Dursley pretended she didn't have a sister, because her sister and her good- for-nothing husband were as unDursleyish as it was possible to be. The Dursleys shuddered to think what the neighbours would say if the Potters arrived in the street. The Dursleys knew that the Potters had a small son, too, but they had never even seen him. This boy was another good reason for keeping the Potters away; they didn't want Dudley mixing with a child like that."
# tokenized_text = tokenizer.tokenize(text)
# # print(tokenized_text)
# tokenized_text = [token.replace("Ġ", " ") for token in tokenized_text]
# # print(f'{tokenized_text=}')
# model_input = tokenizer.encode(text, return_tensors='pt')

# model = hooks.HookedModel(model)
# hook = hooks.common_hooks.gpt_get_attention_hook(0, 'my_hook')

# model.forward(model_input, hooks=[hook], output_attentions=True)
# attn = model.save_ctx['my_hook']['attn']
# attn = einops.rearrange(attn[0], 'h n1 n2 -> n1 n2 h')
# print(attn.shape)
# pysvelte.Hello(name="World").publish('./test.html')

# pysvelte.AttentionMulti(tokens=tokenized_text, attention=attn, head_labels=[f'0:{i}' for i in range(attn.shape[-1])]).publish('./test.html', suppress_title=True)
tokens =['The', ' D', 'urs', 'leys', ' had', ' a', ' small', ' son', ' called', ' Dudley', ' and', ' ', ' in', ' their', ' opinion', ' there', ' was', ' no', ' finer', ' boy', ' anywhere', '.', ' The', ' D', 'urs', 'leys']

with open('token_data.json', 'r') as f:
    neuron_result = json.load(f)
html_object = pysvelte.Clusters(tokens=tokens, model_map=neuron_result)
html_object.update_meta(suppress_title=True).publish('./test.html')