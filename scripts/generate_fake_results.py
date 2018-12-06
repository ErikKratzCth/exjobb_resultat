import numpy as np
import pickle

# Generate fake scores and labels and save
export_dir = '/home/erik/Github/exjobb_resultat/data/'

for dataset in ("prosivic", "dreyeve"):
    for algorithm in ("GPND", "DSVDD", "ALOCC"):
        n_samples = np.random.randint(50,100)
        labels = np.concatenate([np.zeros(n_samples//2), np.ones(n_samples//2)])
        std = 1
        c_in = -1
        c_out = 1
        scores_in = np.random.normal(c_in,std, n_samples//2)
        scores_out = np.random.normal(c_out,std, n_samples//2)
        scores = np.concatenate([scores_in, scores_out])

        filepath = export_dir + "%s_%s.pkl"%(dataset, algorithm)
        with open(filepath,'wb') as f:
            pickle.dump([scores,labels],f)

        print("Saved results to %s"%filepath)
        
        