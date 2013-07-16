Subtickettypes in Trac
======================

The current version is ready for Trac 1.0. There are older, unmaintained,
versions for Trac 0.12 and Trac 0.11.

What is it?
-----------

This plugin alters Trac's behavior so that the interface supports multiple
layers of types. In project with lots of types, rearranging these
types into several layers can clear up the list of tickets and subtickets.

This plugin was based heavily on subcomponents plugin by
"Niels Sascha Reedijk" located here:
http://hg.haiku-os.org/trac-subcomponent,
http://trac-hacks.org/wiki/SubcomponentsPlugin

What is it not?
---------------

The plugin does not change the data model of the ticket; it merely
manipulates the user interface. So a typo ``task`` with the subtickettype
``development`` and ``release`` will be stored in the database as ``task/development``
and ``task/release``.

Installation
------------

To install the module see the TracPlugins page on
http://trac.edgewall.org/wiki/TracPlugins. After activating the plugin in
the configuration file or through the plugins page, it will be activated
without any further configuration.

Using subtickettypes
--------------------

To create types with subtickettypes, then you have to add these using the
standard type admin page. If you enter the following ticket types:

* ``task``
* ``task/development``
* ``task/release``

Then the user interface will show the ``development`` and ``release`` as a
subtickettypes of the ``task`` type.
