**********************
Setting up environment
**********************

Python 3 Virtual Environment
----------------------------
`$ pyvenv-3.4 --without-pip venvdir`

`$ source venvdir/bin/activate`

`$ curl https://bootstrap.pypa.io/get-pip.py | venvdir/bin/python`

Python Dependencies
-------------------
`$ pip install -r requirements.txt`


*************
Running Tests
*************

`$ make tests`


*********
Traceback
*********

  File "/home/leandrotoledo/workspace/pony_and_nose_issue_144/venvdir/lib/python3.4/site-packages/pony/orm/core.py", line 4358, in __init__
  pickled_tree = pickle.dumps(tree, 2)
  _pickle.PicklingError: Can't pickle <class 'pony.thirdparty.compiler.ast.GenExprInner'>: it's not the same object as pony.thirdparty.compiler.ast.GenExprInner
