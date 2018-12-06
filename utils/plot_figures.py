from sklearn.metrics import roc_curve, precision_recall_curve, auc
from matplotlib import pyplot as plt
from utils.unpickle_scores import separate_in_and_out
import os

export_dir = '/home/erik/Github/exjobb_resultat/figures/'


def save_score_histogram(scores, labels, title_prefix, legend_loc = 'upper right', dataset = "", algorithm = ""):

    inlier_scores, outlier_scores, _, _ = separate_in_and_out(scores,labels)

    if dataset == "dreyeve":
        dataset_str = "Dr(eye)ve"
    elif dataset == "prosivic":
        dataset_str = "Pro-SiVIC"

    plt.clf()
    plt.hist(inlier_scores, alpha=0.5, label='Inliers')
    plt.hist(outlier_scores, alpha=0.5, label='Outliers')
    plt.legend(loc=legend_loc)
    plt.title("Scores for %s on %s"%(algorithm, dataset_str))
    plt.xlabel("Score")
    export_path = os.path.join(export_dir, title_prefix+'_scores_hist.svg')
    print('Saving score histogram to "%s"'%export_path)
    plt.savefig(export_path)

def save_all_histograms(results):
    for key, item in results.items():
        title_prefix = "%s_%s"%(item["dataset"], item["algorithm"])
        save_score_histogram(item["scores"], item["labels"], title_prefix, dataset = item["dataset"], algorithm = item["algorithm"])

def save_roc_curves(results, title_prefix = "all_roc_", legend_loc = 'upper right'):

    # For each set of results (scores+labels), compute fpr, tpr and add to plot
    for dataset in ("prosivic", "dreyeve"):
        if dataset == "dreyeve":
            dataset_str = "Dr(eye)ve"
        elif dataset == "prosivic":
            dataset_str = "Pro-SiVIC"

        plt.clf()
        for key, item in results.items():
            if item["dataset"] == dataset:
                fpr, tpr, _ = roc_curve(item["labels"],item["scores"], 1)
                plt.plot(fpr,tpr,label=item["algorithm"])
        plt.title("Receiver operating characteristic for %s experiment"%dataset_str)
        plt.xlabel('False positive rate')
        plt.ylabel('True positive rate')
        plt.legend(loc=legend_loc)
        export_path = os.path.join(export_dir, title_prefix+dataset+".svg")
        plt.savefig(export_path)
        print("Saving ROC diagrim to %s"%export_path)

def save_prc_curves(results, title_prefix = "all_prc_", legend_loc = 'upper right'):

    # For each set of results (scores+labels), compute fpr, tpr and add to plot
    for dataset in ("prosivic", "dreyeve"):

        if dataset == "dreyeve":
            dataset_str = "Dr(eye)ve"
        elif dataset == "prosivic":
            dataset_str = "Pro-SiVIC"

        plt.clf()
        for key, item in results.items():
            if item["dataset"] == dataset:
                pr, rc, _ = precision_recall_curve(item["labels"],item["scores"], 1)
                plt.plot(rc,pr,label=item["algorithm"])
        plt.title("Precicion-recall for %s experiment"%dataset_str)
        plt.xlabel('Recall')
        plt.ylabel('Precision')
        plt.legend(loc=legend_loc)
        export_path = os.path.join(export_dir, title_prefix+dataset+".svg")
        plt.savefig(export_path)
        print("Saving PRC diagrim to %s"%export_path)