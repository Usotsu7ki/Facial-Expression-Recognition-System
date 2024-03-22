# Facial-Expression-Recognition-System

### 
<br>test branch client server and admin-page
<br>请注意：client和server的依赖库并没有上传，请自行配置环境

<br>请注意：管理员注册码是12345678
<br>未完成功能：连接和表情数据传输，表情数据显示，脸部的框
<br>当前问题：在点back button回到login界面后，再次登录出现服务器发送给客户端的第一条消息无法被正确接收的情况
<br>介于上面这个情况，我把返回主界面的按钮删了

<br>2.26:添加record功能，在python编译器下会新建record文件夹，里面存.avi
<br>2.26:连接服务器地址现在需要先读取address.txt的服务器地址
<br>2.26:更改了一些类的命名
<br>2.27:增加进度条，修复help和contact us的ui显示问题

<br>3.8:增加注册和忘记密码
<br>3.12:camera window适配新ui， 增加打开录像文件夹功能
<br>3.21:Apply new UI with buttons changing styles, add screenshot function, Add comments in Eng


<br>3.23:Change client sending frames logic. From triggered by send_timer, to sending after receiving messages from server(face recog data later). 
<br>The first frame sending will be triggered by listening thread after launched 1 seconds, then it will listen server messages
<br>Also, add a thread used to ensure sending is normal. If sending error, try to send after 10 seconds
