# auto_email_task_api

## 后端http服务api
* 通过post请求发送email任务
```
{
    "basic": {
        "smtp_server": "smtp服务器地址",
        "smtp_port": smtp服务器端口,
        "smtp_user": "本人邮箱地址",
        "smtp_password": "smtp服务密码"
    },
    "tasks": [
        {
            "from": "本人邮箱地址",
            "to": "目标邮箱地址0",
            "subject": "主题0",
            "body": "正文0",
            "file": "附件绝对路径0"
        }, 
        {
            "from": "本人邮箱地址",
            "to": "目标邮箱地址1",
            "subject": "主题1",
            "body": "正文1",
            "file": "附件绝对路径1"
        }
    ]
}
```