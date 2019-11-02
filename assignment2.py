
import pandas as pd
names = ['Iris-virginica','Iris-versicolor','Iris-setosa']
def read():
    read_data = open('iris.data').readlines()

    data = []
    data2 =[]
    for i in range(len(names)):
        data.append([])
        data2.append([])
    print(data)
    for i in range(len(read_data)):
        arow = read_data[i].split(',')
        if len(arow)!= 5:
            break
        row = []

        for j in range(4):
            print(arow[j])
            row.append(float(arow[j]))
            data2[names.index(arow[4])].append(float(arow[j]))

        for j in range(len(names)):
            if(arow[4].rstrip() == names[j]):
                data[j].append(row)
        print(row)

    data = pd.DataFrame.from_records(data)
    return data,


if __name__ == '__main__':
    data = read()
    print(data)
    #modify data to access category-feature
