import importlib

import recipy
subset = importlib.import_module('.data.01_subset-data-GBP', 'src')
plotwines = importlib.import_module('.visualization.02_visualize-wines', 'src')
country_sub = importlib.import_module('.data.03_country-subset', 'src')

country = 'Chile'
raw_data = f'data/raw/winemag-data-130k-v2.csv'
subset_file = subset.process_data_GBP(raw_data)
print(subset_file)
plotwines.create_plots(subset_file)
country_file = country_sub.get_country(subset_file, country)
print(country_file)