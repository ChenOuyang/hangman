import random as r

def consume():
    data_store = 0
    data_sum = 0

    while 1:
        data = yield
        data_store += sum(data)
        data_sum += len(data)
        print('The running average is %f' % (data_store/float(data_sum)))

def produce(consumer):

    while 1:
        data = r.sample(range(6),3)
        print('produced %s' % data)
        consumer.send(data)
        yield

if __name__ == '__main__':
    consumer = consume()
    producer = produce(consumer)
    next(consumer)

    for _ in range(10):
        print('Producing......')
        next(producer)


        
