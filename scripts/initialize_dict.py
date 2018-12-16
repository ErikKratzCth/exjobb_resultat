import pickle

common_results_dict = {}

for dataset in ['prosivic', 'dreyeve']:
    common_results_dict[dataset] = {}
    for algorithm in ['ALOCC','DSVDD','GPND']:
        common_results_dict[dataset][algorithm] = "Fake"
print(common_results_dict)
pickle.dump(common_results_dict,open('/home/erik/Github/exjobb_resultat/data/name_dict.pkl','wb'),protocol=2)
