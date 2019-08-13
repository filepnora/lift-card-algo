def convert(data):
    result = []
    for sub in data.split(","):
        if "-" in sub:
            if sub.startswith("-"):
                index_of_split_place = sub.find("-", 1)
                start = int(sub[0:index_of_split_place])
                end = int(sub[index_of_split_place+1:])
                my_range = range(start, end+1)
                for i in my_range:
                    result.append(i)
            else:
                small = sub.split("-")    
                for i in range(int(small[0]), int(small[1])+1):
                    result.append(i)
        else:
            result.append(int(sub))   
    return result


if __name__ == "__main__":
    print(convert("-5--4,-2-2,5-7"))

