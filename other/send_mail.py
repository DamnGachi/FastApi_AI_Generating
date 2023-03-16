import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery.utils.log import get_task_logger
from config import RECIPIENT_MAIL, SENDER_MAIL, SENDER_PASSWORD
from main import celery_app

logger = get_task_logger(__name__)


@celery_app.task
def send_email(subject, body, image_bytes):
    msg = MIMEMultipart()
    msg["From"] = SENDER_MAIL
    msg["To"] = RECIPIENT_MAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    image = MIMEImage(image_bytes)
    image.add_header("Content-Disposition", "attachment", filename="image.png")
    msg.attach(image)

    try:
        smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
        smtp_server.starttls()
        smtp_server.login(SENDER_MAIL, SENDER_PASSWORD)
        smtp_server.sendmail(SENDER_MAIL, RECIPIENT_MAIL, msg.as_string())
        smtp_server.quit()
        logger.info("Email sent to %s", RECIPIENT_MAIL)
    except Exception as e:
        logger.error("Failed to send email to %s: %s", RECIPIENT_MAIL, e)
