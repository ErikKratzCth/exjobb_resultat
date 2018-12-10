from utils.unpickle_scores import load_all_scores
from utils.generate_outputs import *

results = load_all_scores()

# for key, value in results.items():
#     print(key)
#     for subkey, subvalue in value.items():
#         print("\t",subkey)
# Create histograms
save_all_histograms(results)

# Plot ROC
save_roc_curves(results)

# Plot PRC
save_prc_curves(results)

# Generate tables with metrics
save_metrics_tables(results)

# Generate source code for latex figures
save_histogram_figures_latex_code(["prosivic", "dreyeve"],["alocc","dsvdd", "gpnd"])
save_metrics_figures_latex_code(["prosivic","dreyeve"],["roc","prc"])