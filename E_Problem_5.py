n, l = list(map(int, input().split()))
pts = list(map(int, input().split()))
pts.sort()


lc = l - pts[-1] 
diff = abs(pts[0]) if abs(pts[0]) > lc else lc
for i in range(len(pts)-1):
    if abs(pts[i] - pts[i+1])/2 > diff:
        diff =  abs(pts[i] - pts[i+1])/2
print("{0:.10f}".format(diff))