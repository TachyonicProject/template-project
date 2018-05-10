#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This script replaces all template files with a real file with contents
# properly substituted.

import os
import os.path
import shutil
import stat
from string import Template
import sys
import subprocess


def main():
    # If not in the project root directory, go to it.
    project_root = os.path.dirname(os.path.realpath(__file__))
    os.chdir(project_root)

    # Can't use `from my_module import metadata' since `__init__.py.tpl' is
    # templated.
    sys.path.insert(0, os.path.realpath('package'))
    import metadata

    # The title of the main documentation should match the project name in the
    # metadata. Under it should be a matching underline of equal signs. Produce
    # it for the template.
    project_underline = len(metadata.project) * '='


    # Substitute values into template files and produce their real
    # counterparts.
    for dirpath, dirnames, filenames in os.walk(project_root):
        # Don't recurse into git directory.
        if '.git' in dirnames:
            dirnames.remove('.git')

        for filename in filenames:
            # Ignore all non-template files.
            # Using splitext cuts off the last extension.
            root, extension = os.path.splitext(filename)
            if extension != '.tpl':
                continue

            # Substitute values and write the new file.
            tpl_path = os.path.join(dirpath, filename)
            real_path = os.path.join(dirpath, root)

            with open(tpl_path) as tpl_file:
                template = Template(tpl_file.read())
            print('Substituting', tpl_path, '->', real_path)
            with open(real_path, 'w') as real_file:
                real_file.write(template.safe_substitute(
                    project_underline=project_underline,
                    **metadata.__dict__))

            # Remove the template file.
            os.remove(tpl_path)
    print('Renaming the package module: package ->', metadata.package)
    os.rename('package', '%s' % metadata.package)

    os.mkdir(project_root + '/' + metadata.package + '/ui/static/' +
             metadata.package)
    open(project_root + '/' + metadata.package + '/ui/static/' +
         metadata.package + '/empty', 'a').close()

    os.remove('generate.py')


if __name__ == '__main__':
    main()
