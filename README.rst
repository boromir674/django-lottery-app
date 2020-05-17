==========
DD LOTTERY
==========


-----------------------------------------
A Django lottery app with multiple prizes
-----------------------------------------


Development
===========

To run all automated tasks, including unittests:

.. code-block::

    pip install tox
    tox

No need to be in a virtual environment!

Deployment
----------

To deploy in localhost at port 8000, with an *sqlite* in-memory database:

.. code-block::

    virtualenv env --python=python3
    source env/bin/activate
    pip install -r requirements/base.txt

    cd src/dd_lottery_project
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000
