from utils.unpickle_scores import load_all_scores
from utils.plot_figures import *

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

