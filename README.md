Need to install venv vai command.
for Macbook
# python3 -m venv .venv
for window
# py -m venv .venv
Need to install resuests via this command
# pip install requests
Need to install tabulate via thi command
# pip install tabulate
Don't forget to change table style here's the link to change table style
LINK: https://pypi.org/project/tabulate/
In line 90 - print (tabulate(filter_result_row,["ID", "Title", "Price","Category", "Description"], tablefmt="grid"))
change grid to what ever in link like = 
"plain"
"simple"
"github"
"grid"
"simple_grid"
"rounded_grid"
"heavy_grid"
"mixed_grid"
"double_grid"
"fancy_grid"
"outline"
"simple_outline"
"rounded_outline"
"heavy_outline"
"mixed_outline"
"double_outline"
"fancy_outline"
"pipe"
"orgtbl"
"asciidoc"
"jira"
"presto"
"pretty"
"psql"
"rst"
"mediawiki"
"moinmoin"
"youtrack"
"html"
"unsafehtml"
"latex"
"latex_raw"
"latex_booktabs"
"latex_longtable"
"textile"
"tsv"
