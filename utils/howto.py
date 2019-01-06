# I will have loads of results named e.g.
dataset_algorithm_somestring_outliername

First do separation of datasets: Prosivic or dreyeve:
then do separation of algorithm: ALOCC; DSVDD or GPND
then do separation of outliername: foggy or urban
store these and the remaining string in [dataset, alg, outliername, somestring]

for each dataset and outlier name, handle each alg differently (hard coded)
    for ALOCC: D(R(x)), |R(x)-x|, maybe also D(x)
    for DSVDD: soft, hard, ae
    for GPND: pX, ae