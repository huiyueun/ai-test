🦥 Unsloth: Will patch your computer to enable 2x faster free finetuning.
Traceback (most recent call last):
  File "/home/huiyu/Workspace/test-1/step1.py", line 1, in <module>
    from unsloth import FastModel
  File "/home/huiyu/.local/lib/python3.10/site-packages/unsloth/__init__.py", line 251, in <module>
    from .models import *
  File "/home/huiyu/.local/lib/python3.10/site-packages/unsloth/models/__init__.py", line 15, in <module>
    from .llama     import FastLlamaModel
  File "/home/huiyu/.local/lib/python3.10/site-packages/unsloth/models/llama.py", line 20, in <module>
    from ._utils import *
  File "/home/huiyu/.local/lib/python3.10/site-packages/unsloth/models/_utils.py", line 110, in <module>
    from unsloth_zoo.vision_utils import (
  File "/home/huiyu/.local/lib/python3.10/site-packages/unsloth_zoo/vision_utils.py", line 256, in <module>
    LANCZOS = PIL.Image.Resampling.LANCZOS
  File "/usr/lib/python3/dist-packages/PIL/Image.py", line 65, in __getattr__
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
AttributeError: module 'PIL.Image' has no attribute 'Resampling'
