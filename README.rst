==========================
Tachyonic Template Project
==========================

This project provides a best-practices template Python project which integrates several different tools. It saves you work by setting up a number of things, including documentation, code checking, and unit test runners.

Project Setup
=============

This will be the ``README`` for your project. For now, follow these instructions to get this project template set up correctly. Then, come back and replace the contents of this ``README`` with contents specific to your project.

Instructions
------------

#. Clone the template project, replacing ``my-project`` with the name of the project you are creating::

        git clone https://github.com/TachyonicProject/template-project.git my-project
        cd my-project

#. Edit the metadata file ``package/metadata.py`` to correctly describe your project.

#. Generate files based upon the project metadata you just entered::

        python generate.py

   The generation script will remove all the template files and generate real files, then self-destruct upon completion.

#. Delete the old git history and optionally re-initialize the repository::

        rm -rf .git
        git init

#. Replace this ``README`` with your own text.
