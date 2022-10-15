import os
import torch
import transformers
from transformers import GPT2Tokenizer, GPT2LMHeadModel

import logging
logging.disable(logging.CRITICAL)
logger = logging.getLogger(transformers.__name__)
# logger.setLevel(logging.WARNING)
# logger.propagate = False
logger.disabled = True

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

tokenizer = GPT2Tokenizer.from_pretrained(
    "shibing624/code-autocomplete-gpt2-base")
model = GPT2LMHeadModel.from_pretrained(
    "shibing624/code-autocomplete-gpt2-base")
model.to(device)
prompts = [
    """from torch import nn
    class LSTM(Module):
        def __init__(self, *,
                     n_tokens: int,
                     embedding_size: int,
                     hidden_size: int,
                     n_layers: int):""",
    """import numpy as np
    import torch
    import torch.nn as""",
    "import java.util.ArrayList",
    "def factorial(n):",
]
for prompt in prompts:
    input_ids = tokenizer.encode(
        prompt, add_special_tokens=False, return_tensors='pt').to(device)
    outputs = model.generate(input_ids=input_ids,
                             max_length=64 + len(prompt),
                             temperature=1.0,
                             top_k=50,
                             top_p=0.95,
                             repetition_penalty=1.0,
                             do_sample=True,
                             num_return_sequences=1,
                             length_penalty=2.0,
                             early_stopping=True)
    decoded = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
    )
    print(decoded)
    # print("=" * 20)
