#Normalizacion Min Max
def MinMax(A,Lista):
    valor = (A-min(Lista))/(max(Lista)-min(Lista))
    return valor
