import json
from math import inf

def load_journal(filename):
    file=open(filename, 'r')
    data=json.load(file)
    return data

def compute_phi(journal,event):
    if isinstance(journal,str):
        journal=load_journal(journal)
        
    n11=n00=n10=n01=n1_=n0_=n_1=n_0=0 
    #first no. after n corresponds to specific event; second no. corresponds to transforming into squirrel 
    for day in journal:
        if(event in day['events'] and day['squirrel']):
            n11+=1
            n1_+=1
            n_1+=1
        elif(event in day['events']):
            n10+=1
            n1_+=1
            n_0+=1
        elif(day['squirrel']):
            n01+=1
            n_1+=1
            n0_+=1
        else:
            n00+=1
            n_0+=1
            n0_+=1

    phi = (n11 * n00 - n10 * n01)
    phi = phi/((n1_*n0_*n_1*n_0)**0.5)
    return phi
        





def compute_correlations(filename):
    journal = load_journal(filename)
    computed = dict()
    for day in journal:
        for event in day['events']:
            if event not in computed.keys():
                phi=compute_phi(journal,event)
                computed[event] = phi

    return computed

def diagnose(filename):
    corrs = compute_correlations(filename).items()
    max = float('-inf')
    max_event = ""
    min = float('inf')
    min_event = ""
    for event,phi in corrs:
        if phi > max:
            max_event = event
            max = phi
        if phi < min:
            min_event = event
            min = phi

    return max_event,min_event