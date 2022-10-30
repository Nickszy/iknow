from apscheduler.schedulers.background import BackgroundScheduler

def myjob():
    print('hello')

if __name__=='__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(myjob, 'interval', seconds=2)
    scheduler.start()
