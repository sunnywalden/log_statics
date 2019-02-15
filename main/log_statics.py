#!/usr/bin/python

#-*- coding:utf-8 -*-



import datetime


#log_dir = '/data/logs/nginx/tv_search/'
log_dir = 'logs/'

log_file = 'access_tv_search_preview.log'

#last_minute = (datetime.datetime.now() - datetime.timedelta(minutes=1)).strftime("%d/%b/%Y:%H:%M")
last_minute = '19/Jun/2018:09:43'

#print(last_minute )

def response_collecting():

    res = []


    with open(log_dir + log_file,'r') as f:
        record = f.readline().strip()
        #print(record)

        while record:
            if record.find(last_minute):
                response_time = float(record.split(' ')[1])
                response_status = int(record.split(' ')[9])

                res.append([response_time,response_status])
                #yield response_time,response_status
                #print(response_time,response_status)
                record = f.readline().strip()

    #print(res)
    return res

def summary():

    all_res_time = 0.0
    all_res_status = 0

    all_caculator,long_res_caculator = 0,0


    responses = response_collecting()


    for res in responses:
        res_time = res[0]
        response_status = res[1]

        #print(res_time,response_status)

        if res_time and response_status:
            all_res_time += res_time
            all_res_status += response_status
            all_caculator += 1

            if res_time > 0.1:
                long_res_caculator += 1
        else:
            break

    avg_res_time = all_res_time / all_caculator
    avg_res_status = int(all_res_status / all_caculator)
    avg_long_res_rate = float(long_res_caculator / all_caculator)

    if avg_res_status > 200:
        res_status = False
    else:
        res_status = True

    return avg_res_time,res_status,avg_long_res_rate



if __name__ == '__main__':
    avg_res_time,res_status,long_res_rate = summary()
    print(avg_res_time,res_status,long_res_rate)






