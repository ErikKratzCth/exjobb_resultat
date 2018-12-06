import pickle
import os
import numpy as np

data_source = '/home/erik/Github/exjobb_resultat/data/'


def load_specific_score(dataset, algorithm):
    assert dataset in ("prosivic", "dreyeve")
    assert algorithm in ("DSVDD", "GPND", "ALOCC")

    filepath = os.path.join(data_source,"%s_%s.pkl"%(dataset, algorithm))

    with open(filepath,'rb') as f:
        scores, labels = pickle.load(f)

    return scores, labels

def load_all_scores():
    results = {}
    key_it = 0
    for i_dataset in ("prosivic", "dreyeve"):
        for i_algorithm in ("DSVDD", "GPND", "ALOCC"):
            key = "result%d"%key_it
            results[key] = {}
            results[key]["dataset"] = i_dataset
            results[key]["algorithm"] = i_algorithm

            scores, labels = load_specific_score(i_dataset, i_algorithm)
            
            results[key]["scores"] = scores
            results[key]["labels"] = labels
            
            key_it += 1
    return results

def separate_in_and_out(scores, labels, outlier_label = 1):
    inlier_idx = np.where(labels != outlier_label)[0]
    outlier_idx = np.where(labels==outlier_label)[0]

    # Classwise scores
    inlier_scores = scores[inlier_idx]
    outlier_scores = scores[outlier_idx]

    return inlier_scores, outlier_scores, inlier_idx, outlier_idx