from sklearn.metrics import roc_curve, precision_recall_curve, auc
from matplotlib import pyplot as plt
plt.rcParams["font.family"] = "Times"
from utils.unpickle_scores import separate_in_and_out
import os

export_dir = '/home/erik/Github/exjobb_resultat/outputs/'


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
    plt.xlabel("score")
    plt.ylabel("frequency")
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
        plt.xlabel('false positive rate')
        plt.ylabel('true positive rate')
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
        plt.xlabel('recall')
        plt.ylabel('precision')
        plt.legend(loc=legend_loc)
        # Set correct font (Times)
        
        export_path = os.path.join(export_dir, title_prefix+dataset+".svg")
        plt.savefig(export_path)
        print("Saving PRC diagrim to %s"%export_path)

def save_metrics_tables(results):
    for dataset in ("prosivic", "dreyeve"):

        if dataset == "dreyeve":
            dataset_str = "Dr(eye)ve"
        elif dataset == "prosivic":
            dataset_str = "Pro-SiVIC"

        # Begin writing file
        filename = "metric_table_%s.tex"%dataset
        filepath = export_dir+filename
        
        with open(filepath,'w') as f:
            f.write('\\begin{table}\n')
            f.write('\\begin{tabular}{|l|l|l|}\n')
            f.write('\\hline\n')
            f.write('      & AUROC & AUPRC \\\\ \\hline\n')
        
        for key, item in results.items():
                if item["dataset"] == dataset:
                    pr, rc, _ = precision_recall_curve(item["labels"],item["scores"], 1)
                    fpr, tpr, _ = roc_curve(item["labels"],item["scores"], 1)
                    auprc = auc(rc,pr)
                    auroc = auc(fpr,tpr)
                    algorithm_str = item["algorithm"].upper()
                    with open(filepath,'a') as f:
                        f.write('%s & %.4f  & %.4f  \\\\ \\hline\n'%(algorithm_str,auroc,auprc))
        
        caption_str = '\\gls{nd} performance metrics for the evaluated algorithms on the %s dataset'%dataset_str
        label_str = 'tab:results %s'%dataset

        with open(filepath,'a') as f:
            f.write('\\end{tabular}\n')
            f.write('\\caption{%s}\n'%caption_str)
            f.write('\\label{%s}\n'%label_str)
            f.write('\\end{table}\n')

        print("Exported metrics table source code to %s"%filepath)

