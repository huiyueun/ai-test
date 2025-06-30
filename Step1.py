  Preparing metadata (setup.py) ... error
  error: subprocess-exited-with-error
  
  × python setup.py egg_info did not run successfully.
  │ exit code: 1
  ╰─> [16 lines of output]
      /tmp/pip-install-5rnil4m4/sympy_22b44ea237e345988cdd3f482138163a/sympy/mpmath/ctx_mp_python.py:873: SyntaxWarning: "is" with a literal. Did you mean "=="?
        if other is 0:
      /tmp/pip-install-5rnil4m4/sympy_22b44ea237e345988cdd3f482138163a/sympy/mpmath/ctx_mp_python.py:967: SyntaxWarning: "is" with a literal. Did you mean "=="?
        if other is 0:
      Traceback (most recent call last):
        File "<string>", line 2, in <module>
        File "<pip-setuptools-caller>", line 35, in <module>
        File "/tmp/pip-install-5rnil4m4/sympy_22b44ea237e345988cdd3f482138163a/setup.py", line 37, in <module>
          import sympy
        File "/tmp/pip-install-5rnil4m4/sympy_22b44ea237e345988cdd3f482138163a/sympy/__init__.py", line 54, in <module>
          from .plotting import plot, Plot, textplot, plot_backends, plot_implicit
        File "/tmp/pip-install-5rnil4m4/sympy_22b44ea237e345988cdd3f482138163a/sympy/plotting/__init__.py", line 1, in <module>
          from .plot import plot_backends
        File "/tmp/pip-install-5rnil4m4/sympy_22b44ea237e345988cdd3f482138163a/sympy/plotting/plot.py", line 29, in <module>
          from collections import Callable
      ImportError: cannot import name 'Callable' from 'collections' (/usr/lib/python3.10/collections/__init__.py)
      [end of output]
  
  note: This error originates from a subprocess, and is likely not a problem with pip.
error: metadata-generation-failed

× Encountered error while generating package metadata.
╰─> See above for output.

note: This is an issue with the package mentioned above, not pip.
hint: See above for details.


Requirement already satisfied: sympy in /home/huiyu/unsloth-env/lib/python3.10/site-packages (1.14.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /home/huiyu/unsloth-env/lib/python3.10/site-packages (from sympy) (1.3.0)
