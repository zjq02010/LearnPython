from twilio.rest import Client

# 使用twilio服务发送免费短信
# twilio 账号：zjq02010@163.com  密码: zhao1,,,
accound_sid ="AC72e9b90610e591c41e66add779ed8d7b"
auth_token = "56c56232d913d42cb479a6b886d51c37"
client = Client(accound_sid, auth_token)
message = client.messages.create(
    from_= "+12396037980",
    to="+8616602782565",
    body="注意，计算已完成"
)
