import datetime 
from apscheduler.schedulers.background import BackgroundScheduler 
from apscheduler.triggers.cron import CronTrigger
from src.services.rate_receiver import return_rate
from src.database.database import SessionLocal, engine, Base
from src.models.model import RateLogs
import time 

Base.metadata.create_all(bind=engine)

def scheduled_save_rate():
    with SessionLocal() as session:
        try: 
            latest_rate = return_rate()
            new_rec = RateLogs(rate=latest_rate)

            session.add(new_rec)
            session.commit()
            print(f"Successfully saved rate {latest_rate} to db")

        except Exception as e:
            session.rollback()
            print(f"error while saving to db: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(
    scheduled_save_rate,
    trigger=CronTrigger(hour='*', minute=0),
    id='hourly_rate_saver',
    next_run_time=datetime.datetime.now()
)

scheduler.start()
print("Scheduler started. Press Ctrl+C to exit.")

# Keep the main process alive so the background worker thread can run
try:
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print("Scheduler stopped.")