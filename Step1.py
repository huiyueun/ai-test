(unsloth-env) (base) huiyu@huiyu-linux2:~/Workspace/test-1$ python step1.py 
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
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth/models/_utils.py", line 110, in <module>
    from unsloth_zoo.vision_utils import (
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth_zoo/vision_utils.py", line 257, in <module>
    from .dataset_utils import train_on_responses_only as _train_on_responses_only
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/unsloth_zoo/dataset_utils.py", line 480, in <module>
    from trl.trainer.utils import ConstantLengthDataset
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/trl/trainer/utils.py", line 36, in <module>
    from transformers import (
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 2155, in __getattr__
    value = getattr(module, name)
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 2154, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 2184, in _get_module
    raise e
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/transformers/utils/import_utils.py", line 2182, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "/home/huiyu/unsloth-env/lib/python3.10/site-packages/transformers/integrations/integration_utils.py", line 37, in <module>
    from .. import PreTrainedModel, TFPreTrainedModel, TrainingArguments
ImportError: cannot import name 'PreTrainedModel' from 'transformers' (/home/huiyu/unsloth-env/lib/python3.10/site-packages/transformers/__init__.py)
