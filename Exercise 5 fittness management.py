import datetime


def gettime():
    return datetime.datetime.now()


def work(name, item, act):
    # Name of Client
    client1, client2, client3 = 'aritra_', 'ranvijay_', 'virat_'
    if name == 1:
        name = client1
    elif name == 2:
        name = client2
    else:
        name = client3

    # Food or Exercise
    if item == 1:
        name += 'food.txt'
    if item == 2:
        name += 'exercise.txt'

    # Lock or Retrieve
    if action == 2:
        with open(name) as f:
            print('***Here is you data!***\n')
            print(f.read())

    elif action == 1:
        text = input('***Start Writing Below***\n')
        t = str(gettime())
        with open(name, 'a+') as f:
            f.write('\n [ {} ] {}'.format(t, text))
            print('*****Data Updated Sucessfully!****')
    else:
        with open(name, 'r+') as f:
            f.truncate(0)
            print('+---Logs Deleted!---+')


            # Driver Function
print('Hello Welcome to Health Management System\n')
action = int(input('1:Log or 2:Retrieve 3.Delete logs\n'))
name = int(input('1:Aritra 2:RanVijay 3.Virat\n'))
item = int(input('1:Food 2:Exercise\n'))
work(name, item, action)