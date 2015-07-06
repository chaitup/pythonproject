## in file /app/private/mail_queue.py
import time
while True:
    rows = db(db.queue.status=='pending').select()
    for row in rows:
        if mail.send(to=row.email,
            subject=row.subject,
            message=row.message):
            row.update_record(status='sent')
        else:
            row.update_record(status='failed')
        db.commit()
    time.sleep(60) # check every minute