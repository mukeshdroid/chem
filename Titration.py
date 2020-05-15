import matplotlib.pyplot as plt
import math

di = dict(zip([1,100,10**6,10**10],[1000,100000,100,25]))
for step in di:
    lim = step * di[step]
    y = []
    for a in range(-lim,lim,step):
        B = a + 2 * 10 ** 7
        C = a * 10 ** 7
        x2 = (B - math.sqrt(B*B - 4 * C)) / 2   
        hconc = 10**7 + a - x2
        pH = math.log10(hconc)
        y.append(hconc)
    graph, ax = plt.subplots()
    txt = "Note : Each drop contains " + str(step)+  " disassociated molecules"
    graph.text(.5, -0.05, txt, ha='center')
    xaxis = range( - di[step] , di[step])
    ax.plot(xaxis,y)
    #graph.set_size_inches(7, 4, forward=True)
    graph.suptitle('Hypothetical titration Curves')
    ax.set_xlabel('Drops added')
    ax.set_ylabel('pH value')
