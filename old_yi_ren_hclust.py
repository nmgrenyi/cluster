import sys
import math
import itertools
import heapq


def get_dimension_nop(data):
    dic = {}
    i = 0
    for line in open(data):
        line1 = line.split(',')
        length = len(line1)
        line2 = line1[0:length-1]
        line3 = []
        for d in line2:
            line3.append(float(d))
        dic[i] = line3
        i = i + 1
    print dic
#    print "111"
    global number_of_points
    number_of_points = len(dic)
    global dimensions
    dimensions = len(dic[0])
#    print number_of_points
#    print dimensions
    all_points=[]
    for i in dic:
        all_points.append(dic[i])
#    print all_points
    return all_points


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

def get_heap(all_points):
    heap = []
    for i in itertools.combinations(all_points,2):
        distance_pair={}
#        print i[0]
#        print i[1]
#        print distance(i[0],i[1])
        distance_pair[distance(i[0],i[1])] = [i[0],i[1]]
        heapq.heappush(heap,distance_pair)
    '''
    for i in all_points:
        for j in all_points:
            if i != j:
                distnace_pair=[]
                distance_pair=[distance(i,j),[i,j]]
                heap.append(distance_pair)'''
#    print heap
#    print len(all_points)
#    print len(heap)
#    print heapq.heappop(heap)
    return heap


def hclustering(heap,all_points):
    not_used_list=all_points
    cluster_iteration_times = number_of_points
    all_cluster_dict = {}
    while cluster_iteration_times >= 2:
        min_distance_cluster = heapq.heappop(heap)
        print min_distance_cluster
        print "222"
        print cluster_iteration_times
        cluster1 = heap[min_distance_cluster][0]
        print cluster1
        cluster2 = heap[min_distance_cluster][1]
        print cluster2
        if cluster1 in not_used_list and cluster2 in not_used_list:
            not_used_list.remove(cluster1)
            not_used_list.remove(cluster2)
            new_cluster = []
            for i in range(len(cluster1)):
#                print i
#                print len(cluster1)
                new_cluster_element = (cluster1[i] + cluster2[i])/2
                print new_cluster_element
                new_cluster.append(new_cluster_element)
                print new_cluster
            not_used_list.append(new_cluster)
            heap = []
            for i in itertools.combinations(not_used_list,2):
                distance_pair=[]
#                print i[0]
#                print '333'
#                print i[1]
#                print distance(i[0],i[1])
                distance_pair=[distance(i[0],i[1]), [i[0],i[1]]]
                heapq.heappush(heap,distance_pair)
            all_cluster_dict[cluster_iteration_times] = list(not_used_list)
            print not_used_list
            print "not_used_list"
            cluster_iteration_times = cluster_iteration_times - 1
    print all_cluster_dict

    


if __name__ == '__main__':
    inputdata = sys.argv[1]
    inputdata1 = sys.argv[2]
    all_points = get_dimension_nop(inputdata)
    heap = get_heap(get_dimension_nop(inputdata))
#    hclustering(heap,all_points)
