.. _contributing:

Contributing
============

Encouraging more people to help develop pvlib-python is essential to our
success. Therefore, we want to make it easy and rewarding for you to
contribute.

There is a lot of material in this section, aimed at a variety of
contributors from novice to expert. Don't worry if you don't (yet)
understand parts of it.


Easy ways to contribute
~~~~~~~~~~~~~~~~~~~~~~~

Here are a few ideas for how you can contribute, even if you are new to
pvlib-python, git, or Python:

* Ask and answer `pvlib questions on StackOverflow <http://stackoverflow.com/questions/tagged/pvlib>`_
  and participate in discussions in the `pvlib-python google group <https://groups.google.com/forum/#!forum/pvlib-python>`_.
* Make `GitHub issues <https://github.com/pvlib/pvlib-python/issues>`_
  and contribute to the conversations about how to resolve them.
* Read issues and pull requests that other people created and
  contribute to the conversation about how to resolve them.
  Look for issues tagged with
  `good first issue <https://github.com/pvlib/pvlib-python/labels/good%20first%20issue>`_,
  `easy <https://github.com/pvlib/pvlib-python/labels/easy>`_,
  or `help wanted <https://github.com/pvlib/pvlib-python/labels/help%20wanted>`_.
* Improve the documentation and the unit tests.
* Improve the IPython/Jupyter Notebook tutorials or write new ones that
  demonstrate how to use pvlib-python in your area of expertise.
* If you have MATLAB experience, you can help us keep pvlib-python
  up to date with PVLIB_MATLAB or help us develop common unit tests.
  For more, see `Issue #2 <https://github.com/pvlib/pvlib-python/issues/2>`_
  and `Issue #3 <https://github.com/pvlib/pvlib-python/issues/3>`_.
* Tell your friends and colleagues about pvlib-python.
* Add your project to our
  `Projects and publications that use pvlib-python wiki
  <https://github.com/pvlib/pvlib-python/wiki/Projects-and-publications-
  that-use-pvlib-python>`_.


How to contribute new code
~~~~~~~~~~~~~~~~~~~~~~~~~~

The basics
----------

Contributors to pvlib-python use GitHub's pull requests to add/modify
its source code. The GitHub pull request process can be intimidating for
new users, but you'll find that it becomes straightforward once you use
it a few times. Please let us know if you get stuck at any point in the
process. Here's an outline of the process:

#. Create a GitHub issue and get initial feedback from users and
   maintainers. If the issue is a bug report, please include the
   code needed to reproduce the problem.
#. Obtain the latest version of pvlib-python: Fork the pvlib-python
   project to your GitHub account, ``git clone`` your fork to your computer.
#. Make some or all of your changes/additions and ``git commit`` them to
   your local repository.
#. Share your changes with us via a pull request: ``git push`` your
   local changes to your GitHub fork, then go to GitHub make a pull
   request.

The Pandas project maintains an excellent `contributing page
<http://pandas.pydata.org/pandas-docs/stable/contributing.html>`_ that goes
into detail on each of these steps. Also see GitHub's `Set Up Git
<https://help.github.com/articles/set-up-git/>`_ and `Using Pull
Requests <https://help.github.com/articles/using-pull-requests/>`_.

We strongly recommend using virtual environments for development.
Virtual environments make it trivial to switch between different
versions of software. This `astropy guide
<http://astropy.readthedocs.org/en/latest/development/workflow/
virtual_pythons.html>`_ is a good reference for virtual environments. If
this is your first pull request, don't worry about using a virtual
environment.

You must include documentation and unit tests for any new or improved
code. We can provide help and advice on this after you start the pull
request. See the Testing section below.


.. _pull-request-scope:

Pull request scope
------------------

This section can be summed up as "less is more".

A pull request can quickly become unmanageable if too many lines are
added or changed. "Too many" is hard to define, but as a rule of thumb,
we encourage contributions that contain less than 50 lines of primary code.
50 lines of primary code will typically need at least 250 lines
of documentation and testing. This is about the limit of what the
maintainers can review on a regular basis.

A pull request can also quickly become unmanageable if it proposes
changes to the API in order to implement another feature. Consider
clearly and concisely documenting all proposed API changes before
implementing any code. Modifying
`api.rst <https://github.com/pvlib/pvlib-python/blob/master/docs/sphinx/source/api.rst>`_
and/or the latest `whatsnew file <https://github.com/pvlib/pvlib-python/tree/master/docs/sphinx/source/whatsnew>`_
can help formalize this process.

Questions about related issues frequently come up in the process of
addressing implementing code for a pull request. Please try to avoid
expanding the scope of your pull request (this also applies to
reviewers!). We'd rather see small, well-documented additions to the
project's technical debt than see a pull request languish because its
scope expanded beyond what the reviewer community is capable of
processing.

Of course, sometimes it is necessary to make a large pull request. We
only ask that you take a few minutes to consider how to break it into
smaller chunks before proceeding.

pvlib-python contains :ref:`3 "layers" of code <modeling-paradigms>`:
functions, PVSystem/Location, and ModelChain. We recommend that
contributors focus their work on only one or two of those layers in a
single pull request. New models are *not* required to be available to
the higher-level API!


When should I submit a pull request?
------------------------------------

The short answer: anytime.

The long answer: it depends. If in doubt, go ahead and submit. You do
not need to make all of your changes before creating a pull request.
Your pull requests will automatically be updated when you commit new
changes and push them to GitHub.

There are pros and cons to submitting incomplete pull-requests. On the
plus side, it gives everybody an easy way to comment on the code and can
make the process more efficient. On the minus side, it's easy for an
incomplete pull request to grow into a multi-month saga that leaves
everyone unhappy. If you submit an incomplete pull request, please be
very clear about what you would like feedback on and what we should
ignore. Alternatives to incomplete pull requests include creating a
`gist <https://gist.github.com>`_ or experimental branch and linking to
it in the corresponding issue.

The best way to ensure that a pull request will be reviewed and merged in
a timely manner is to:

#. Start by creating an issue. The issue should be well-defined and
   actionable.
#. Ask the maintainers to tag the issue with the appropriate milestone.
#. Make a limited-scope pull request. It can be a lot of work to check all of
   the boxes in `pull request guidelines
   <https://github.com/pvlib/pvlib-python/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_,
   especially for pull requests with a lot of new primary code.
   See :ref:`pull-request-scope`.
#. Tag pvlib community members or ``@pvlib/maintainer`` when the pull
   request is ready for review. (see :ref:`pull-request-reviews`)


.. _pull-request-reviews:

Pull request reviews
--------------------

The pvlib community and maintainers will review your pull request in a
timely fashion. Please "ping" ``@pvlib/maintainer`` if it seems that
your pull request has been forgotten at any point in the pull request
process.

Keep in mind that the PV modeling community is diverse and each pvlib
community member brings a different perspective when reviewing code.
Some reviewers bring years of expertise in the sub-field that your code
contributes to and will focus on the details of the algorithm. Other
reviewers will be more focused on integrating your code with the rest of
pvlib, ensuring that it is feasible to maintain, that it meets the
:ref:`code style <code-style>` guidelines, and that it is
:ref:`comprehensively tested <testing>`. Limiting the scope of the pull
request makes it much more likely that all of these reviews can be
conducted and any issues can be resolved in a timely fashion.

Sometimes it's hard for reviewers to be immediately available, so the
right amount of patience is to be expected. That said, interested
reviewers should do their best to not wait until the last minute to put
in their two cents.


.. _code-style:

Code style
~~~~~~~~~~

pvlib python generally follows the `PEP 8 -- Style Guide for Python Code
<https://www.python.org/dev/peps/pep-0008/>`_. Maximum line length for code
is 79 characters.

Code must be compatible with python 2.7 and 3.4+.

pvlib python uses a mix of full and abbreviated variable names. See
:ref:`variables_style_rules`. We could be better about consistency.
Prefer full names for new contributions. This is especially important
for the API. Abbreviations can be used within a function to improve the
readability of formulae.

Set your editor to strip extra whitespace from line endings. This
prevents the git commit history from becoming cluttered with whitespace
changes.

Please see :ref:`Documentation` for information specific to documentation
style.

Remove any ``logging`` calls and ``print`` statements that you added
during development. ``warning`` is ok.

We typically use GitHub's
"`squash and merge` <https://help.github.com/articles/about-pull-request-merges/#squash-and-merge-your-pull-request-commits>_"
feature to merge your pull request into pvlib. GitHub will condense the
commit history of your branch into a single commit when merging into
pvlib-python/master (the commit history on your branch remains
unchanged). Therefore, you are free to make commits that are as big or
small as you'd like while developing your pull request.


.. _documentation:

Documentation
~~~~~~~~~~~~~

Documentation must be written in
`numpydoc format <https://numpydoc.readthedocs.io/>`_.

The numpydoc format includes a specification for the allowable input
types. Python's `duck typing <https://en.wikipedia.org/wiki/Duck_typing>`_
allows for multiple input types to work for many parameters. pvlib uses
the following generic descriptors as short-hand to indicate which
specific types may be used:

* dict-like : dict, OrderedDict, pd.Series
* numeric : scalar, np.array, pd.Series. Typically int or float dtype.
* array-like : np.array, pd.Series. Typically int or float dtype.

Parameters that specify a specific type require that specific input type.

A relatively easy way to test your documentation is to build it on
`readthedocs.org <https://readthedocs.org>` by following their
`Import Your Docs <http://docs.readthedocs.io/en/stable/getting_started.html#import-your-docs>`_
instructions and enabling your branch on the readthedocs
`versions admin page <http://docs.readthedocs.io/en/stable/features.html#versions>`_.

Another option is to install the required dependencies in your virtual/conda
environment. See
`docs/environment.yml <https://github.com/pvlib/pvlib-python/blob/master/docs/environment.yml>`_
for the latest dependences for building the complete documentation. Some
doc files can be compiled with fewer dependencies, but this is beyond
the scope of this guide.

.. _testing:

Testing
~~~~~~~

pvlib's unit tests can easily be run by executing ``pytest`` on the
pvlib directory:

``pytest pvlib``

or, for a single module:

``pytest pvlib/test/test_clearsky.py``

or, for a single test:

``pytest pvlib/test/test_clearsky.py::test_ineichen_nans``

We suggest using pytest's ``--pdb`` flag to debug test failures rather
than using ``print`` or ``logging`` calls. For example:

``pytest pvlib --pdb``

will drop you into the
`pdb debugger <https://docs.python.org/3/library/pdb.html>`_ at the
location of a test failure. As described in :ref:`code-style`, pvlib
code does not use ``print`` or ``logging`` calls, and this also applies
to the test suite (with rare exceptions).

New unit test code should be placed in the corresponding test module in
the pvlib/test directory.

Developers **must** include comprehensive tests for any additions or
modifications to pvlib.

pvlib-python contains 3 "layers" of code: functions, PVSystem/Location,
and ModelChain. Contributors will need to add tests that correspond to
the layers that they modify.

Functions
---------
Tests of core pvlib functions should ensure that the function returns
the desired output for a variety of function inputs. The tests should be
independent of other pvlib functions (see :issue:`394`). The tests
should ensure that all reasonable combinations of input types (floats,
nans, arrays, series, scalars, etc) work as expected. Remember that your
use case is likely not the only way that this function will be used, and
your input data may not be generic enough to fully test the function.
Write tests that cover the full range of validity of the algorithm.
It is also important to write tests that assert the return value of the
function or that the function throws an exception when input data is
beyond the range of algorithm validity.

PVSystem/Location
-----------------
The PVSystem and Location classes provide convenience wrappers around
the core pvlib functions. The tests in test_pvsystem.py and
test_location.py should ensure that the method calls correctly wrap the
function calls. Many PVSystem/Location methods pass one or more of their
object's attributes (e.g. PVSystem.module_parameters, Location.latitude)
to a function. Tests should ensure that attributes are passed correctly.
These tests should also ensure that the method returns some reasonable
data, though the precise values of the data should be covered by
function-specific tests discussed above.

We prefer to use the ``pytest-mock`` framework to write these tests. The
test below shows an example of testing the ``PVSystem.ashraeiam``
method. ``mocker`` is a ``pytest-mock`` object. ``mocker.spy`` adds
features to the ``pvsystem.ashraeiam`` *function* that keep track of how
it was called. Then a ``PVSystem`` object is created and the
``PVSystem.ashraeiam`` *method* is called in the usual way. The
``PVSystem.ashraeiam`` method is supposed to call the
``pvsystem.ashraeiam`` function with the angles supplied to the method
call and the value of ``b`` that we defined in ``module_parameters``.
The ``pvsystem.ashraeiam.assert_called_once_with`` tests that this does,
in fact, happen. Finally, we check that the output of the method call is
reasonable.

.. code-block:: python

    def test_PVSystem_ashraeiam(mocker):
        # mocker is a pytest-mock object.
        # mocker.spy adds code to a function to keep track of how it is called
        mocker.spy(pvsystem, 'ashraeiam')

        # set up inputs
        module_parameters = {'b': 0.05}
        system = pvsystem.PVSystem(module_parameters=module_parameters)
        thetas = 1

        # call the method
        iam = system.ashraeiam(thetas)

        # did the method call the function as we expected?
        # mocker.spy added assert_called_once_with to the function
        pvsystem.ashraeiam.assert_called_once_with(thetas, b=module_parameters['b'])

        # check that the output is reasonable, but no need to duplicate
        # the rigorous tests of the function
        assert iam < 1.

Avoid writing PVSystem/Location tests that depend sensitively on the
return value of a statement as a substitute for using mock. These tests
are sensitive to changes in the functions, which is *not* what we want
to test here, and are difficult to maintain.

ModelChain
----------
The tests in test_modelchain.py should ensure that
``ModelChain.__init__`` correctly configures the ModelChain object to
eventually run the selected models. A test should ensure that the
appropriate method is actually called in the course of
``ModelChain.run_model``. A test should ensure that the model selection
does have a reasonable effect on the subsequent calculations, though the
precise values of the data should be covered by the function tests
discussed above. ``pytest-mock`` can also be used for testing ``ModelChain``.

The example below shows how mock can be used to assert that the correct
PVSystem method is called through ``ModelChain.run_model``.

.. code-block:: python

    def test_modelchain_dc_model(mocker):
        # set up location and system for model chain
        location = location.Location(32, -111)
        system = pvsystem.PVSystem(module_parameters=some_sandia_mod_params,
                                   inverter_parameters=some_cecinverter_params)

        # mocker.spy adds code to the system.sapm method to keep track of how
        # it is called. use returned mock object m to make assertion later,
        # but see example above for alternative
        m = mocker.spy(system, 'sapm')

        # make and run the model chain
        mc = ModelChain(system, location,
                        aoi_model='no_loss', spectral_model='no_loss')
        times = pd.date_range('20160101 1200-0700', periods=2, freq='6H')
        mc.run_model(times)

        # assertion fails if PVSystem.sapm is not called once
        # if using returned m, prefer this over m.assert_called_once()
        # for compatibility with python < 3.6
        assert m.call_count == 1

        # ensure that dc attribute now exists and is correct type
        assert isinstance(mc.dc, (pd.Series, pd.DataFrame))


This documentation
~~~~~~~~~~~~~~~~~~

If this documentation is unclear, help us improve it! Consider looking
at the `pandas
documentation <http://pandas.pydata.org/pandas-docs/stable/
contributing.html>`_ for inspiration.
