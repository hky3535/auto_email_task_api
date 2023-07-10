# auto_email_task_api

## 后端http服务api
* 通过post请求发送email任务
```json
{
    "basic": {
        "smtp_server": "smtp服务器地址",
        "smtp_port": "smtp服务器端口",
        "smtp_user": "本人邮箱地址",
        "smtp_password": "smtp服务密码"
    },
    "tasks": [
        {
            "from": "本人邮箱地址（必须与smtp_user一致）",
            "to": ["目标邮箱地址00", "目标邮箱地址01", "目标邮箱地址02", "..."],
            "cc": ["抄送邮箱地址00", "抄送邮箱地址01", "抄送邮箱地址02", "..."],
            "subject": "主题0",
            "body": "正文0",
            "file": "附件绝对路径0（可以留空）"
        }, 
        {
            "from": "本人邮箱地址（必须与smtp_user一致）",
            "to": ["目标邮箱地址10", "目标邮箱地址11", "目标邮箱地址12", "..."],
            "cc": ["抄送邮箱地址10", "抄送邮箱地址11", "抄送邮箱地址12", "..."],
            "subject": "主题1",
            "body": "正文1",
            "file": "附件绝对路径1（可以留空）"
        }
    ]
}
```
## 运行方式
* 在任何一个目录git clone https://github.com/hky3535/auto_email_task_api.git
* python3 main.py
* 程序仅使用python3.8及以上源码的库，不需要额外pip任何库