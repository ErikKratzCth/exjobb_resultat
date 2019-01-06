from utils.unpickle_scores import *
from utils.generate_outputs import *


# Print out which experiments are stored
#datasets, algorithms = show_all_stored_experiments()

results = load_all_scores()

# # Create histograms
# save_all_histograms(results)

# # Plot ROC
# save_roc_curves(results)

# # Plot PRC
# save_prc_curves(results)

# # Generate tables with metrics
# save_metrics_tables(results)

# # Generate source code for latex figures
# save_histogram_figures_latex_code(datasets,algorithms)
# save_metrics_figures_latex_code(datasets,["roc","prc"])