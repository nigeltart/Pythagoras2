import math

def compute_hcf (x,y):
    while (y>0):
        x, y = y, x%y
    return x

def triangle_match (triangle_a, triangle_b):
    for i in range(3):
        hcf = compute_hcf(triangle_a[i],triangle_b[i])
        if hcf==1:
            return False
    return True

def triples_match(triangle_a, triangles):
    for triangle in triangles:
        if triangle_match(triangle_a, triangle):
            return True
    return False


triples=[]
candidate_count=0

for base in range (1,1000):
    for height in range (base+1,1000):
        hyp = math.sqrt(base**2 + height**2)
        if int(hyp)==hyp:
            candidate_count+=1
            triangle=[base, height, int(hyp)]
            if not triples_match(triangle, triples):
                triples.append(triangle)


for triple in triples:
    print (triple)
print ("candidates: %d found: %d" % (candidate_count, len(triples)))