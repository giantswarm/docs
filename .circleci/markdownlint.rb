# This is a markdownlint styles file for giantswarm/docs.
# See https://github.com/markdownlint/markdownlint/blob/master/docs/creating_styles.md
# for details.

# First add all rules.
# Note: This MUST happen at the very top.
all

rule 'MD004', :style => 'consistent'

# Allow for intuitive numbered lists
rule 'MD029', :style => 'ordered'

# Ignore inline HTML. We need this in certain places.
exclude_rule 'MD033'

# Enforcing the rules below will require big changes in the entire repo.
# So we exclude them for now.

# Line length.
exclude_rule 'MD013'

# Trailing spaces. 
exclude_rule 'MD012'
