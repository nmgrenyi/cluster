import sys
import math
import itertools
import heapq


def get_dimension_nop_list(data):
    List = []
    n = 0
    for line in open(data):
        line1 = line.split(',')
        length = len(line1)
        line2 = line1[0:length-1]
        line3 = []
        for d in line2:
            line3.append(float(d))
        line4 = [[n],line3]
        n = n + 1
        List.append(line4)
    global number_of_points
    number_of_points = len(List)
    global dimensions
    dimensions = len(List[0][1])
    return List

def No_of_point():
    No_of_points = []
    for i in range(number_of_points):
        No_of_points.append(i)
    return No_of_points

def get_heap(List):
    heap = []
    for i in itertools.combinations(List,2):
        distancekey = distance(i[0][1],i[1][1])
        tempheap = [distancekey,[[i[0][0],i[0][1]],[i[1][0],i[1][1]]]]
        heapq.heappush(heap,tempheap)
    return heap

def distance(list1,list2):
    length=len(list1)
    sum2 = 0
    for i in range(length):
        x = list1[i]
        y = list2[i]
        total = (x - y)*(x - y)
        sum2 = sum2 + total
    distance = math.sqrt(sum2)
    return distance


def hcluster(heap,No_of_points,List,K):
    cluster_times = number_of_points
    k = int(K)
    dict_of_step = {}
    while cluster_times >= 2:
        min_distance = heapq.heappop(heap)
        L = min_distance
        L1 = L[1][0]
        L2 = L[1][1]
        L10 = L[1][0][0]
        L20 = L[1][1][0]
        L11 = L[1][0][1]
        L21 = L[1][1][1]
        L30 =[]
        List.remove(L1)
        List.remove(L2)
        for i in L10:
            if i in No_of_points:
                No_of_points.remove(i)
                L30.append(i)
            else:
                No_of_points.remove(L10)
                for p in L10:
                    L30.append(p)
                break
        for j in L20:
            if j in No_of_points:
                No_of_points.remove(j)
                L30.append(j)
            else:
                No_of_points.remove(L20)
                for q in L20:
                    L30.append(q)
                break
        No_of_points.append(L30)
        No_of_points1 = []
        No_of_points1 = No_of_points
        cluster_times = cluster_times - 1
        dict_of_step[cluster_times] = list(No_of_points1)
        L31 = []
        for i in range(len(L11)):
            new_element = (L11[i]+L21[i])/2
            L31.append(new_element)
        L3 = [L30,L31]
        List.append(L3)
        heap = get_heap(List)
    return dict_of_step[k]

def precision_recall(data,hc):
    list_of_label = []
    for line in open(data):
        line1 = line.split(',')
        length = len(line1)
        line2 = line1[length-1]
        line3 = line2.replace('\n','')
        list_of_label.append(line3)
    myset = set(list_of_label)
    
    n = 0
    totalx = 0
    for item in myset:
        n = list_of_label.count(item)
        m = n * (n - 1) / 2
        totalx = totalx + m

    p = 0
    q = 0
    totaly = 0
    for line in hc:
        p = len(line)
        q = p * (p - 1) / 2
        totaly = totaly + q

    list_of_hcluster_pairs = []
    for h in hc:
        for i in itertools.combinations(h,2):
            temp = []
            for ii in i:
                temp.append(ii)
            temp.sort()
            list_of_hcluster_pairs.append(temp)
    list_of_goldstand_pairs = []
    dict_of_goldstand_pairs = {}
    pointer = 0
    for line in open(data):
        line1 = line.split(',')
        length = len(line1)
        temp_label = line1[length-1]
        label = temp_label.replace('\n','')
        dict_of_goldstand_pairs.setdefault(label,[])
        point_list = dict_of_goldstand_pairs[label]
        point_list.append(pointer)
        dict_of_goldstand_pairs[label] = point_list
        pointer = pointer + 1
    for g in dict_of_goldstand_pairs:
        for i in itertools.combinations(dict_of_goldstand_pairs[g],2):
            temp = []
            for ii in i:
                temp.append(ii)
            temp.sort()
            list_of_goldstand_pairs.append(temp)
    z = 0
    for i in list_of_hcluster_pairs:
        if i in list_of_goldstand_pairs:
            z = z + 1
        else:
            continue
    recall = float(z) / float(totalx)
    pre = float(z) / float(totaly)
    print recall
    print pre
    


if __name__ == '__main__':
    inputdata = sys.argv[1]
    inputdata1 = sys.argv[2]
    List = get_dimension_nop_list(inputdata)
    heap = get_heap(List)
    No_of_points = No_of_point()
    hc = hcluster(heap,No_of_points,List,inputdata1)
    precision_recall(inputdata,hc)
    print hc
