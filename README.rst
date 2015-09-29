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