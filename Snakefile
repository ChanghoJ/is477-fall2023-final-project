# prepare data
rule prepare:
  output:
    "data/wine.zip",
    "data/Index",
    "data/wine.data",
    "data/wine.names"
  shell:
    "python scripts/prepare_data.py"

# profile dataframe from data
rule profile:
  input:
    "data/wine.data"
  output:
    "profiling/report.html"
  shell:
    "python scripts/profile.py"

# analyze from given data from previous step
rule analyze:
  input:
    "data/wine.data"
  output:
    "results/uci_wine_results.txt"
  shell:
    "python scripts/analysis.py"

