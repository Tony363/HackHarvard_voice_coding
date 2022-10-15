import os
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

import logging
logging.disable(logging.CRITICAL)


def get_model(device: torch.device) -> tuple:
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    tokenizer = GPT2Tokenizer.from_pretrained(
        "shibing624/code-autocomplete-gpt2-base")
    model = GPT2LMHeadModel.from_pretrained(
        "shibing624/code-autocomplete-gpt2-base")
    model.to(device)
    return model, tokenizer


def main(
    prompts: list,
    model: GPT2LMHeadModel,
    tokenizer: GPT2Tokenizer,
    device: torch.device,
) -> None:
    file = open("txt/autocomplete_code.txt", "w")
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
        file.write(decoded)
        print(decoded)
    file.close()
    # print("=" * 20)


if __name__ == "__main__":
    # prompts = [
    #     """
    #     from torch import nn
    #     class LSTM(Module):
    #         def __init__(self, *,
    #                     n_tokens: int,
    #                     embedding_size: int,
    #                     hidden_size: int,
    #                     n_layers: int):
    #                     """,
    #     """
    #     import numpy as np
    #     import torch
    #     import torch.nn as
    #     """,
    #     "import java.util.ArrayList",
    #     "def factorial(n):",
    # ]
    prompts = [
        """
class Vehicle:
        """,
        """
class Vehicle:
    def __init__(self):
""",
        """
class Vehicle:
    def __init__(self):
        self.wheels=
"""
    ]
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model, tokenizer = get_model(device)
    main(prompts, model, tokenizer, device)
