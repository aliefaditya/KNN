import csv
import math

k = 100


def read_csv(path):
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile)
        data = []
        for row in spamreader:
            data.append(parse_data(row))
        return data


def parse_data(row):
    parsed = []
    for data in row:
        try:
            parsed.append(int(data))
        except ValueError:
            parsed.append(data)
    return parsed


def write_csv(path, tested):
    with open(path, 'w') as csvfile:
        spamwriter = csv.writer(csvfile)
        for data in tested:
            spamwriter.writerow(data)
    print('Succesfully write data to ', path)


def classify_list(test_list, train_list):
    tested = []
    for index, test in enumerate(test_list):
        print('Processing test case #', index)
        tested.append(test)
        tested[len(tested)-1][len(test)-1] = classify(test, train_list)
    return tested


def classify(test, train_list):
    distance = []
    for train in train_list:
        distance.append([train[len(train)-1], calculate_distance(test, train)])
    sorted_distance = sorted(distance, key=lambda train: train[1])
    return get_class(sorted_distance)


def calculate_distance(test, train):
    return math.sqrt(
        (test[1] - train[1])**2 +
        (test[2] - train[2])**2 +
        (test[3] - train[3])**2 +
        (test[4] - train[4])**2
    )


def get_class(sorted_distance):
    hoax = [0, 0]
    trimmed = sorted_distance[0:k]
    for trim in trimmed:
        hoax[trim[0]] = hoax[trim[0]] + 1
    return 0 if hoax[0] > hoax[1] else 1


train = read_csv('./train.csv')
train.pop(0)
test = read_csv('./test.csv')
header = test.pop(0)
tested = classify_list(test, train)
tested.insert(0, header)
write_csv('./tested.csv', tested)
