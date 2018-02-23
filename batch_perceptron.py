def batch_perceptron(d, x, w, n):
    s_misclassify = []
    time = 0
    for i in range(len(x)):
        sum = 0
        for j in range(len(x[i])):
            sum += d[i] * w[j] * x[i][j]
        if sum <= 0:
            s_misclassify.append(i)
    while len(s_misclassify) > 0:
        for i in s_misclassify:
            for j in range(len(x[i])):
                w[j] += n * d[i] * x[i][j]
        s_misclassify = []
        for i in range(len(x)):
            sum = 0
            for j in range(len(x[i])):
                sum += d[i] * w[j] * x[i][j]
            if sum <= 0:
                s_misclassify.append(i)
        time += 1
        ##############
        print("iteration : %d, weight : %s" %(time, str(w)))
        ##############
    print("completet weight : %s at iteration : %d" % (str(w), time))



# def batch_perception(d, x, w, n):
#     time = 0
#     ls = check_error(d, x, w)
#     while (is_error(ls, d, x, w)):
#         w = change_weight(ls, d, x, w, n)
#         ls = check_error(d, x, w)
#         time += 1
#         ##############
#         print("iteration : %d, weight : %s" %(time, str(w)))
#         ##############
#     print("completet weight : %s at iteration : %d" % (str(w), time))

def is_error(ls, d, x, w):
    return len(ls) > 0

def check_error(d, x, w):
    ls_error = []
    for i in range(len(x)):
        sum = 0
        for j in range(len(x[i])):
            sum += d[i] * w[j] * x[i][j]
        if sum <= 0 : 
            ls_error.append(i)
    return ls_error

def change_weight(ls, d, x, w, n):
    for i in ls:
        for j in range(len(x[i])):
            w[j] += d[i] * n * x[i][j]
    return w

# d = [-1, -1, -1, 1]   # AND
d = [-1, 1, 1, 1]   # OR
# d = [1, 1, 1, -1]   # NAND
# d = [1, -1, -1, -1]   # NOR
# d = [-1, 1, 1, -1]   # XOR
# d = [1, -1, -1, 1]   # XNOR


x = [(-1,0,0), (-1,0,1), (-1,1,0), (-1,1,1)]
w = [0, 0, 0]
n = 0.5
batch_perceptron(d, x, w, n)