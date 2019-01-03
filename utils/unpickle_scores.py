import pickle
import os
import numpy as np

data_source = '/home/erik/Github/exjobb_resultat/data/'


def load_specific_score(dataset, algorithm):
    assert dataset in ("prosivic", "dreyeve")
    # assert algorithm in ("DSVDD", "GPND", "ALOCC")

    filepath = os.path.join(data_source,"%s_%s.pkl"%(dataset, algorithm))

    try:
        with open(filepath,'rb') as f:
            scores, labels = pickle.load(f)
    except:
        with open(filepath,'rb') as f:
            scores, labels = pickle.load(f, encoding='latin1')

    return scores, labels

def load_all_scores():
    print("Loading all results")
    results = {}
    key_it = 0
    common_results_dict = pickle.load(open('/home/erik/Github/exjobb_resultat/data/name_dict.pkl','rb'))
    for i_dataset, experiments in common_results_dict.items():
        for i_algorithm, experiment in experiments.items():
            key = "result%d"%key_it
            results[key] = {}
            results[key]["dataset"] = i_dataset
            results[key]["algorithm"] = i_algorithm

            scores, labels = load_specific_score(i_dataset, i_algorithm)
            labels = np.array([np.int(x) for x in labels])
            results[key]["scores"] = scores
            results[key]["labels"] = labels
            
            key_it += 1

            print("Successfully loaded results for {:<10} : {:<15}".format(i_dataset, i_algorithm))
    return results

def separate_in_and_out(scores, labels, outlier_label = 1):
    
    inlier_idx = np.where(labels != outlier_label)[0]
    outlier_idx = np.where(labels==outlier_label)[0]
    scores = (scores-np.amin(scores))
    # scores = scores / np.amax(scores)
    # print(labels)
    # print(scores)
    # print(inlier_idx)
    # Classwise scores
    inlier_scores = scores[inlier_idx]
    outlier_scores = scores[outlier_idx]

    return inlier_scores, outlier_scores, inlier_idx, outlier_idx

def show_all_stored_experiments():
    common_results_dict = pickle.load(open('/home/erik/Github/exjobb_resultat/data/name_dict.pkl','rb'))
    print("Experiments with stored results:\n")
    print("\t{:<10} {:<15} {:<30}".format("Dataset","Algorithm", "Experiment name"))
    datasets = []
    algorithms = []
    for dataset, experiments in common_results_dict.items():
        datasets.append(dataset)
        for algorithm, exp_name in experiments.items():
            algorithms.append(algorithm.lower())
            print("\t{:<10} {:<15} {:<30}".format(dataset, algorithm, exp_name))
    
    return datasets, algorithms