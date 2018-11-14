# Exclude any compile Python files (most likely grafted by tests/ directory).
global-exclude *.pyc

# Informational files
include *.txt
include LICENSE

# Including docs and tests. It's unclear whether convention dictates
# including built docs. However, Sphinx doesn't include built docs, so
# we are following their lead.
graft docs
prune docs/build
graft tests

# Setup-related things
include setup.py

# Templates
graft $package/ui/templates
graft $package/templates

# Static
graft $package/ui/static
graft $package/static

# Other
recursive-include $package *.json
recursive-include $package *.ini

# NO-CYTHON PACKAGES
recursive-exclude $package *.c
recursive-exclude $package *.so
