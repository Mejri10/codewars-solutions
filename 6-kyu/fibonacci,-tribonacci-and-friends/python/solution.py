def Xbonacci(signature,n):
    k = len(signature)
    while len(signature) < n:
        signature.append(sum(signature[-k:]))
    return signature[:n]