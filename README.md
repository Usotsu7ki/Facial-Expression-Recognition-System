# Facial-Expression-Recognition-System

### 
### This is branch for client(including login,camera, register and forget password), server and admin-window
<br>Be cautious: client andserver的lib并没有upload, please配置环境 by your own
<br>Be cautious: 目前最新版本的Server端在钟qifeng那

<br>Be cautious: 目前管理员注册码是12345678
<br>当前问题：在点back button回到login界面后，再次登录出现服务器发送给客户端的第一条消息无法被正确接收的情况
<br>介于上面这个情况，我把返回主界面的按钮删了
<br>----------------------------------------------------------------------------------------
#### Update 
<br>11.29: add server, client and admin on github
<br>2:24: add qss for client 
<br>2.26:add record function, under python compiler it will mkdir folder for it, recording save in .avi
<br>2.26:will loading address.txt for server address rather than write in code
<br>2.26:change some class naming
<br>2.27:add loading bar, repair bugs showing in help and contact us 

<br>3.8:Add register and forget password functions
<br>3.12:for camera window apply new ui, add function open record folder
<br>3.21:Apply new UI with buttons changing styles, add screenshot function, Add comments in Eng


<br>3.23:Change client sending frames logic. From triggered by send_timer, to sending after receiving messages from server(face recog data later). 
<br>The first frame sending will be triggered by listening thread after launched 1 seconds, then it will listen server messages
<br>Also, add a thread used to ensure sending is normal. If sending error, try to send after 10 seconds
<br>Add receive recog result from server, spilt, then display using rectangle and texts.
<br>However, did not know how to add rectangle and text into recording

<br>3.28: repair bug, apply new ui according to fiseha's suggestions
<br>3.29: add drawing logics for different faces, add local address ip get for admin for self exclusion in connecting-sockets list 


brfore launching, please check whether running the server locally, if server and client are running differently, please change global_setting.isLocal to False, also, change address.txt, using the ip of the server        -by biylj9
