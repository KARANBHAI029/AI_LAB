import math
data = [
    [0.046, 4.006], [-0.454, -0.706], [0.181, 5.769], [0.739, 4.741], [-0.11, 5.179],
    [-0.235, 0.271], [-0.265, 5.257], [0.148, 5.131], [0.458, 5.164], [5.104, 4.02],
    [-0.117, -0.117], [0.034, -0.712], [-0.351, 4.836], [5.515, 5.466], [-0.301, 0.926],
    [5.411, 4.39], [-0.196, 4.268], [5.166, 5.488], [0.181, 4.677], [4.58, 4.845],
    [0.121, -0.957], [-0.272, 0.055], [0.79, 0.384], [-0.506, 0.157], [0.049, 5.484],
    [0.003, 4.883], [-0.232, -0.233], [-0.3, -0.146], [-0.862, -0.281], [4.76, 4.907],
    [5.406, 5.678], [4.964, 5.502], [5.172, 4.118], [-0.018, 5.782], [-1.31, 5.411],
    [4.942, 4.849], [-0.007, -0.529], [5.369, 5.086], [4.261, 4.64], [-0.404, 4.749],
    [4.447, 4.402], [0.733, -0.113], [4.336, 5.098], [5.162, 4.807], [4.662, 5.306],
    [0.044, 4.85], [4.77, 5.529], [-0.575, 0.188], [0.248, -0.069], [0.324, 0.762]
]
def dist(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

def gradient_descent_update(centroids,clusters,lr=0.1):
    new_centroids=[]
    for i in range(len(centroids)):
        if not clusters[i]:continue
        grad_x,grad_y=0,0
        for p in clusters[i]:
            grad_x+=-2*(p[0]-centroids[i][0])
            grad_y+=-2*(p[1]-centroids[i][1])
        new_x=centroids[i][0]-(lr*grad_x/len(clusters[i]))
        new_y=centroids[i][1]-(lr*grad_y/len(clusters[i]))
        new_centroids.append([new_x,new_y])
    return new_centroids

def newton_update(clusters):
    new_centroids=[]
    for cluster in clusters:
        if not cluster: continue
        avg_x=sum(p[0] for p in cluster)/len(cluster)
        avg_y=sum(p[1] for p in cluster)/len(cluster)
        new_centroids.append([avg_x,avg_y])
    return new_centroids

def get_sse(data, centroids):
    total = 0
    for p in data:
        total += min([(p[0]-c[0])**2 + (p[1]-c[1])**2 for c in centroids])
    return total

centroids_newton=[data[0],data[10],data[20]]
for iterations in range(10):
    clusters=[[],[],[]]
    for p in data:
        distances=[dist(p,c) for c in centroids_newton]
        closest=distances.index(min(distances))
        clusters[closest].append(p)

    centroids_newton=newton_update(clusters)

centroids_gd = [data[0],data[10],data[20]]
for i in range(10): 
    clusters = [[],[],[]]
    for p in data:
        distances = [dist(p,c) for c in centroids_gd]
        closest = distances.index(min(distances))
        clusters[closest].append(p)
    centroids_gd = gradient_descent_update(centroids_gd, clusters)
    
    
print("Newton Results:", centroids_newton)
print("Newton SSE:", get_sse(data, centroids_newton))
print("-" * 30)
print("Gradient Descent Results:", centroids_gd)
print("Gradient Descent SSE:", get_sse(data, centroids_gd))