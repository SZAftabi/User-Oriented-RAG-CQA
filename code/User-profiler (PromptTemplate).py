# -*- coding: utf-8 -*-
"""Llama-2 (Tag generation).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VM2X2Z-ft0xw8M2-NUGVbwy6wH-cFza6
"""

B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
B_INST, E_INST = "[INST]", "[/INST]"

def get_tg_prompt(_question, _tags = None):
  system_prompt = 'You are a Tag Generator. Respond only with a list of tags; do not include any additional text or explanations.'
  user_prompt = f'''Please generate at least 5 tags for the provided question. Tags can include multi-word phrases if appropriate and should help hierarchically categorize the question's topics.
### Question:
{_question}
### Tags:
'''
  prompt = f"{B_INST} {B_SYS}{system_prompt}{E_SYS}{user_prompt} {E_INST}\n\n"
  if _tags: prompt += f'{_tags}</s>'
  return prompt

def get_response_index(_input_ids, _task):
  _index = None
  _skip_tokens = None
  if _task == 'RQE':
    _index = 2
    _skip_tokens = 10
  if _task == 'SUM':
    _index = 1
    _skip_tokens = 11
  if _task == 'TG':
    _index = 1
    _skip_tokens = 10
  hashtags_indexes = [i for i, n in enumerate(_input_ids) if n == 29937]
  if len(hashtags_indexes) > _index:
    return [i for i, n in enumerate(_input_ids) if n == 29937][_index] + _skip_tokens
  elif _task == 'RQE':
    return 0
  else:
    return -1

def generate_prompt(data, is_eval):
  promp = None
  if is_eval: prompt = get_tg_prompt(data['text'])
  else: prompt = get_tg_prompt(data['text'], data['tags'])
  return prompt