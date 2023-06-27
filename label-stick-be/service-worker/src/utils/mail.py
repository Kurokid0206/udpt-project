import smtplib
import logging
from jinja2 import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr

SMTP_ENDPOINT = ""
SMTP_PORT = 587
SMTP_USER_NAME = ""
SMTP_PASSWORD = ""

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)


def send_mail(data: dict):
    html_template = "mail.html"
    template = Template(html_template["Body"].read().decode("utf-8"))
    send_mail_template(template.render(**data), data)


def send_mail_template(template, data: dict):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = data["subject"]
    msg["From"] = formataddr(("US Codingo", data["from_email"]))
    data["to_email"] = (
        data["to_email"] if isinstance(data["to_email"], list) else [data["to_email"]]
    )
    msg["To"] = ", ".join(data["to_email"])
    html_part = MIMEText(template, "html")
    msg.attach(html_part)

    try:
        smtp_server = smtplib.SMTP(host=SMTP_ENDPOINT, port=SMTP_PORT)
        smtp_server.starttls()
        smtp_server.login(user=SMTP_USER_NAME, password=SMTP_PASSWORD)
        smtp_server.sendmail(data["from_email"], data["to_email"], msg.as_string())
        smtp_server.quit()
    except Exception as e:
        log.exception(e)
    else:
        log.info("Email sent successfully")
