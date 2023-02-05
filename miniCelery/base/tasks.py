from celery import shared_task


@shared_task('send email')
def send_invite_email():
    # django send email config
    pass