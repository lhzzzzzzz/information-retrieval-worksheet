def read_file(file_path):
    file_dict = {}
    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            line = line.split()
            term = line[0]
            file_list = [int(x) for x in line[1:]]
            file_dict[term] = file_list
    return file_dict

def mergeAND(list1, list2):
    maxlist, minlist = (list1, list2) if len(list1) >= len(list2) else (list2, list1)
    maxlistnum, minlistnum = len(maxlist), len(minlist)

    pointer_min = pointer_max = 0


    merge_list = []

    while pointer_min < minlistnum and pointer_max < maxlistnum:
            if minlist[pointer_min] <= maxlist[pointer_max]:
                merge_list.append(minlist[pointer_min])
                if minlist[pointer_min] == maxlist[pointer_max]:
                    pointer_max += 1
                pointer_min += 1
            else:
                merge_list.append(maxlist[pointer_max])
                pointer_max += 1

    merge_list.extend(maxlist[pointer_max:])
    merge_list.extend(minlist[pointer_min:])
    
    return merge_list


def mergeOR(list1, list2):
    maxlist, minlist = (list1, list2) if len(list1) >= len(list2) else (list2, list1)
    maxlistnum, minlistnum = len(maxlist), len(minlist)

    pointer_min = pointer_max = 0


    merge_list = []

    while pointer_min < minlistnum and pointer_max < maxlistnum:
            if minlist[pointer_min] < maxlist[pointer_max]:
                merge_list.append(minlist[pointer_min])
                pointer_min += 1
            if minlist[pointer_min] == maxlist[pointer_max]:
                pointer_max += 1
                pointer_min += 1
            else:
                merge_list.append(maxlist[pointer_max])
                pointer_max += 1

    merge_list.extend(maxlist[pointer_max:])
    merge_list.extend(minlist[pointer_min:])
    
    return merge_list


# file_dict = read_file("./index.txt")

list1 = [1,2,3,4]
list2 = [4,5,6]
print(mergeOR(list1, list2))
