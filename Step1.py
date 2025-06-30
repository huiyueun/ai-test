from unsloth import FastModel
import torch

# ✅ Unsloth 모델 불러오기
model, tokenizer = FastModel.from_pretrained(
    model_name = "unsloth/Meta-Llama-3-8B-Instruct-bnb-4bit",
    max_seq_length = 2048,
    load_in_4bit = True,
)

# ✅ 한글 질문 입력
prompt = "한국의 수도는 어디인가요?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# ✅ 모델 추론
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=50)

# ✅ 결과 출력
print("🦥 모델 응답:")
print(tokenizer.decode(outputs[0], skip_special_tokens=True))



/home/huiyu/unsloth-env/lib/python3.10/site-packages/transformers/utils/generic.py:441: UserWarning: torch.utils._pytree._register_pytree_node is deprecated. Please use torch.utils._pytree.register_pytree_node instead.
  _torch_pytree._register_pytree_node(
🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
Traceback (most recent call last):
  File "/home/huiyu/Workspace/test-1/step1.py", line 1, in <module>
    from unsloth import FastModel
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth/__init__.py", line 251, in <module>
    from .models import *
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth/models/__init__.py", line 15, in <module>
    from .llama     import FastLlamaModel
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth/models/llama.py", line 20, in <module>
    from ._utils import *
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth/models/_utils.py", line 84, in <module>
    from unsloth_zoo.patching_utils import (
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth_zoo/patching_utils.py", line 565, in <module>
    raise RuntimeError("Unsloth: Patch for dynamic quantization failed since current_key_name_str does not exist.")
RuntimeError: Unsloth: Patch for dynamic quantization failed since current_key_name_str does not exist.

pip install torch==2.3.0 --index-url https://download.pytorch.org/whl/cu121
pip install transformers==4.36.2
pip install sentencepiece==0.1.99
pip install bitsandbytes==0.41.3.post2
pip install "unsloth[cu121-torch230] @ git+https://github.com/unslothai/unsloth.git"
