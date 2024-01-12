import datetime as dt
import math
def solution(fees, records):
    car = {}
    fee = {}
    
    for record in records:
        r = record.split()
        if r[2] == 'IN':
            car[r[1]] = r[0]
        else:
            o = dt.datetime.strptime(r[0], '%H:%M')
            i = dt.datetime.strptime(car[r[1]], '%H:%M')
            time = (o-i).seconds/60
            if r[1] not in fee:
                fee[r[1]] = time
            else:
                fee[r[1]] += time
            del(car[r[1]])
    
    if len(car) != 0:
        for k, v in car.items():
            o = dt.datetime.strptime('23:59', '%H:%M')
            i = dt.datetime.strptime(v, '%H:%M')
            time = (o-i).seconds/60
            if k not in fee:
                fee[k] = time
            else:
                fee[k] += time
                
    fee = sorted(fee.items())

    answer = []
    for f in fee:
        if f[1] - fees[0] <= 0: 
            answer.append(fees[1])
        else:
            cost = fees[1]
            cost += math.ceil((f[1] - fees[0]) / fees[2]) * fees[3]
            answer.append(cost)

    return answer