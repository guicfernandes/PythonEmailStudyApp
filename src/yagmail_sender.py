import yagmail

receiver = "teste@gmail.com"
body = "Hello there from Yagmail"
filename = "./data/Dont-Say-The-Words-Jobs.pdf"

yag = yagmail.SMTP("teste@gmail.com")
yag.send(
    to=receiver,
    subject="Yagmail test with attachment",
    contents=body,
    attachments=filename,
)
