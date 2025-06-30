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





===================================BUG REPORT===================================
/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:166: UserWarning: Welcome to bitsandbytes. For bug reports, please run

python -m bitsandbytes


  warn(msg)
================================================================================
/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/cuda_setup/main.py:166: UserWarning: /home/huiyu/miniconda3 did not contain ['libcudart.so', 'libcudart.so.11.0', 'libcudart.so.12.0'] as expected! Searching further paths...
  warn(msg)
The following directories listed in your path were found to be non-existent: {PosixPath('@/tmp/.ICE-unix/1852,unix/huiyu-linux2'), PosixPath('local/huiyu-linux2')}
The following directories listed in your path were found to be non-existent: {PosixPath('/etc/xdg/xdg-ubuntu')}
The following directories listed in your path were found to be non-existent: {PosixPath('/net/tenshu/Terminator2')}
The following directories listed in your path were found to be non-existent: {PosixPath('1'), PosixPath('0')}
CUDA_SETUP: WARNING! libcudart.so not found in any environmental path. Searching in backup paths...
The following directories listed in your path were found to be non-existent: {PosixPath('/usr/local/cuda/lib64')}
DEBUG: Possible options found for libcudart.so: set()
CUDA SETUP: PyTorch settings found: CUDA_VERSION=126, Highest Compute Capability: 8.6.
CUDA SETUP: To manually override the PyTorch CUDA version please see:https://github.com/TimDettmers/bitsandbytes/blob/main/how_to_use_nonpytorch_cuda.md
CUDA SETUP: Required library version not found: libbitsandbytes_cuda126.so. Maybe you need to compile it from source?
CUDA SETUP: Defaulting to libbitsandbytes_cpu.so...

================================================ERROR=====================================
CUDA SETUP: CUDA detection failed! Possible reasons:
1. You need to manually override the PyTorch CUDA version. Please see: "https://github.com/TimDettmers/bitsandbytes/blob/main/how_to_use_nonpytorch_cuda.md
2. CUDA driver not installed
3. CUDA not installed
4. You have multiple conflicting CUDA libraries
5. Required library not pre-compiled for this bitsandbytes release!
CUDA SETUP: If you compiled from source, try again with `make CUDA_VERSION=DETECTED_CUDA_VERSION` for example, `make CUDA_VERSION=113`.
CUDA SETUP: The CUDA version for the compile might depend on your conda install. Inspect CUDA version via `conda list | grep cuda`.
================================================================================

CUDA SETUP: Problem: The main issue seems to be that the main CUDA runtime library was not detected.
CUDA SETUP: Solution 1: To solve the issue the libcudart.so location needs to be added to the LD_LIBRARY_PATH variable
CUDA SETUP: Solution 1a): Find the cuda runtime library via: find / -name libcudart.so 2>/dev/null
CUDA SETUP: Solution 1b): Once the library is found add it to the LD_LIBRARY_PATH: export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:FOUND_PATH_FROM_1a
CUDA SETUP: Solution 1c): For a permanent solution add the export from 1b into your .bashrc file, located at ~/.bashrc
CUDA SETUP: Solution 2: If no library was found in step 1a) you need to install CUDA.
CUDA SETUP: Solution 2a): Download CUDA install script: wget https://github.com/TimDettmers/bitsandbytes/blob/main/cuda_install.sh
CUDA SETUP: Solution 2b): Install desired CUDA version to desired location. The syntax is bash cuda_install.sh CUDA_VERSION PATH_TO_INSTALL_INTO.
CUDA SETUP: Solution 2b): For example, "bash cuda_install.sh 113 ~/local/" will download CUDA 11.3 and install into the folder ~/local
CUDA SETUP: Setup Failed!
Traceback (most recent call last):
  File "/home/huiyu/Workspace/test-1/step1.py", line 1, in <module>
    from unsloth import FastModel
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth/__init__.py", line 176, in <module>
    import bitsandbytes as bnb
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/__init__.py", line 6, in <module>
    from . import cuda_setup, utils, research
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/research/__init__.py", line 1, in <module>
    from . import nn
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/research/nn/__init__.py", line 1, in <module>
    from .modules import LinearFP8Mixed, LinearFP8Global
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/research/nn/modules.py", line 8, in <module>
    from bitsandbytes.optim import GlobalOptimManager
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/optim/__init__.py", line 6, in <module>
    from bitsandbytes.cextension import COMPILED_WITH_CUDA
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/bitsandbytes/cextension.py", line 20, in <module>
    raise RuntimeError('''
RuntimeError: 
        CUDA Setup failed despite GPU being available. Please run the following command to get more information:

        python -m bitsandbytes

        Inspect the output of the command and see if you can locate CUDA libraries. You might need to add them
        to your LD_LIBRARY_PATH. If you suspect a bug, please take the information from python -m bitsandbytes
        and open an issue at: https://github.com/TimDettmers/bitsandbytes/issues
