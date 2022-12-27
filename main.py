def main(S, d):
    '''create a babylonian function.
    
    Args:
        S (int): number
        d (int): numnber
        
    Returns:
        float: result
    '''
    
    a=(S-d**2)/(2*d)
    b=a+d
    x=b-((a**2)/(2*b))
    return float(x)
S=26
d=5

print(main(S,d))
