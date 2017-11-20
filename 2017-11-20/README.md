# 那些鲜为人知的Linux命令2

## 1 <空格> 命令

你在终端上键入的每个命令都会记录到history，也能用history命令重新调用。

如何骗过history 命令呢？在终端，只需要在键入命令之前输入一个或多个空格，这样你的命令就不会被记录了。

让我们体验一下吧，先在终端尝试五个常见的 Linux 命令并在命令之前留个空(例如** ls, pwd, uname, echo “hi”** 和 who)，然后检查这些命令是不是记录在历史中。

```
avi@localhost:~$  ls
avi@localhost:~$  pwd
avi@localhost:~$  uname
avi@localhost:~$  echo “hi”
avi@localhost:~$  who
```
```
avi@localhost:~$  ls
avi@localhost:~$  pwd
avi@localhost:~$  uname
avi@localhost:~$  echo “hi”
avi@localhost:~$  who
```
现在运行 history 命令来查看上面已执行的命令是否已经被记录了.
```
avi@localhost:~$ history
cd /dev/ 
ls 
dd if=/dev/cdrom1 of=/home/avi/Desktop/squeeze.iso 
ping www.google.com 
su
```
```
avi@localhost:~$ history
cd /dev/ 
ls 
dd if=/dev/cdrom1 of=/home/avi/Desktop/squeeze.iso 
ping www.google.com 
su
```
你看到没有最后执行的命令没有被记录。我们也可以用另一个命令cat | bash欺骗history，结果跟上面一样。

## 2 stat 命令

Linux中的stat命令用来显示文件或文件系统的状态信息。当用文件名作为参数时，stat将会展示文件的全部信息。状态信息包括文件 大小、块、权限、访问时间、修改时间、状态改变时间等。
```
avi@localhost:~$ stat 34.odt 
  File: `34.odt'
  Size: 28822   Blocks: 64 IO Block: 4096   regular file 
Device: 801h/2049d  Inode: 5030293 Links: 1 
Access: (0644/-rw-r--r--)  Uid: ( 1000/ avi)   Gid: ( 1000/ avi) 
Access: 2013-10-14 00:17:40.000000000 +0530 
Modify: 2013-10-01 15:20:17.000000000 +0530 
Change: 2013-10-01 15:20:17.000000000 +0530
```
```
avi@localhost:~$ stat 34.odt 
  File: `34.odt'
  Size: 28822   Blocks: 64 IO Block: 4096   regular file 
Device: 801h/2049d  Inode: 5030293 Links: 1 
Access: (0644/-rw-r--r--)  Uid: ( 1000/ avi)   Gid: ( 1000/ avi) 
Access: 2013-10-14 00:17:40.000000000 +0530 
Modify: 2013-10-01 15:20:17.000000000 +0530 
Change: 2013-10-01 15:20:17.000000000 +0530
```
## 3 + . 和 + .

上面的组合键事实上不是一个命令，而是传递最后一个命令参数到提示符后的快捷键，以输入命令的倒序方式传递命令。按住 Alt或Esc再按一下 “.”。

## 4 pv 命令

在电影里尤其是好莱坞电影你可能已经看见过模拟文本了，像是在实时输入文字，你可以用pv命令仿照任何类型模拟风的文本输出，包括流水线输出。pv可能没有在你的系统上安装，你需要用apt或yum获取安装包，然后安装pv到你的机器。
```
root@localhost:# echo "Tecmint [dot] com is the world's best website for qualitative Linux article" | pv -qL 20
```
```
root@localhost:# echo "Tecmint [dot] com is the world's best website for qualitative Linux article" | pv -qL 20
```
输出样式
```
Tecmint [dot] com is the world''s best website for qualitative Linux article
Tecmint [dot] com is the world''s best website for qualitative Linux article
```
## 5 mount | colum -t

上面的命令用一个很不错的格式与规范列出了所有挂载文件系统。
```
avi@localhost:~$ mount | column -t
avi@localhost:~$ mount | column -t
```
输出样式
```
/dev/sda1on  / type  ext3 (rw,errors=remount-ro) 
tmpfson  /lib/init/rw  type  tmpfs(rw,nosuid,mode=0755) 
proc on  /proc type  proc (rw,noexec,nosuid,nodev) 
sysfson  /sys  type  sysfs(rw,noexec,nosuid,nodev) 
udev on  /dev  type  tmpfs(rw,mode=0755) 
tmpfson  /dev/shm  type  tmpfs(rw,nosuid,nodev) 
devpts   on  /dev/pts  type  devpts   (rw,noexec,nosuid,gid=5,mode=620) 
fusectl  on  /sys/fs/fuse/connections  type  fusectl  (rw) 
binfmt_misc  on  /proc/sys/fs/binfmt_misc  type  binfmt_misc  (rw,noexec,nosuid,nodev) 
nfsd on  /proc/fs/nfsd type  nfsd (rw)
```
```
/dev/sda1on  / type  ext3 (rw,errors=remount-ro) 
tmpfson  /lib/init/rw  type  tmpfs(rw,nosuid,mode=0755) 
proc on  /proc type  proc (rw,noexec,nosuid,nodev) 
sysfson  /sys  type  sysfs(rw,noexec,nosuid,nodev) 
udev on  /dev  type  tmpfs(rw,mode=0755) 
tmpfson  /dev/shm  type  tmpfs(rw,nosuid,nodev) 
devpts   on  /dev/pts  type  devpts   (rw,noexec,nosuid,gid=5,mode=620) 
fusectl  on  /sys/fs/fuse/connections  type  fusectl  (rw) 
binfmt_misc  on  /proc/sys/fs/binfmt_misc  type  binfmt_misc  (rw,noexec,nosuid,nodev) 
nfsd on  /proc/fs/nfsd type  nfsd (rw)
```
## 6 Ctr+l 命令

在进行下一步之前，我先问一下，你是如何清理你的终端？呵呵，你会在提示符后键入 “clear”。好的。用上面的命令执行清理终端都将成为过去。你只需要按下Ctr+l，看看它如何立即清理你的终端。

## 7 curl 命令

在命令行下如何检查你的未读邮件？这个命令对于工作在没有图形界面的服务器的人佷有用。它会在运行期间再次要求输入密码，你不需要在上面一行硬编码你的密码，否则会有其它安全风险。
```
avi@localhost:~$ curl -u avishek1210@gmail.com --silent "https://mail.google.com/mail/feed/atom" | perl -ne 'print \t if //; print "$2\n" if /<(title|name)>(.*)<\/\1>/;'
avi@localhost:~$ curl -u avishek1210@gmail.com --silent "https://mail.google.com/mail/feed/atom" | perl -ne 'print \t if //; print "$2\n" if /<(title|name)>(.*)<\/\1>/;'
```
输出样式
```
Enter host password for user 'avishek1210@gmail.com': 
Gmail - Inbox for avishek1210@gmail.com 
People offering cars in Delhi - Oct 26 
    Quikr Alerts 
another dependency question 
    Chris Bannister 
    Ralf Mardorf 
    Reco 
    Brian 
    François Patte 
    Curt 
    Siard 
    berenger.morel 
Hi Avishek - Download your Free MBA Brochure Now... 
    Diya 
★Top Best Sellers Of The Week, Take Your Pick★ 
    Timesdeal 
aptitude misconfigure? 
    Glenn English 
Choosing Debian version or derivative to run Wine when resource poor 
    Chris Bannister 
    Zenaan Harkness 
    Curt 
    Tom H 
    Richard Owlett 
    Ralf Mardorf 
    Rob Owens

Enter host password for user 'avishek1210@gmail.com': 
Gmail - Inbox for avishek1210@gmail.com 
People offering cars in Delhi - Oct 26 
    Quikr Alerts 
another dependency question 
    Chris Bannister 
    Ralf Mardorf 
    Reco 
    Brian 
    François Patte 
    Curt 
    Siard 
    berenger.morel 
Hi Avishek - Download your Free MBA Brochure Now... 
    Diya 
★Top Best Sellers Of The Week, Take Your Pick★ 
    Timesdeal 
aptitude misconfigure? 
    Glenn English 
Choosing Debian version or derivative to run Wine when resource poor 
    Chris Bannister 
    Zenaan Harkness 
    Curt 
    Tom H 
    Richard Owlett 
    Ralf Mardorf 
    Rob Owens
```
## 8 screen 命令

screen命令能断开一个会话下的一个长时间运行的进程并能再次连接，如有需要，也提供了灵活的命令选项

要运行一个长时间的进程，我们通常执行
```
avi@localhost:~$ ./long-unix-script.sh
avi@localhost:~$ ./long-unix-script.sh
```
缺乏灵活性，需要用户持续当前的会话，但是如果我们执行上面的命令是：
```
avi@localhost:~$ screen ./long-unix-script.sh
avi@localhost:~$ screen ./long-unix-script.sh
```
它能在不同会话间断开或重连。当一个命令正在执行时按“Ctrl + A”然后再按“d”来断开。

重新连接运行：
```
avi@localhost:~$ screen -r 4980.pts-0.localhost
avi@localhost:~$ screen -r 4980.pts-0.localhost
```
注解：在这里，这个命令的稍后的部分是screen id，你能用‘screen -ls’命令查看。欲了解更多关于screen命令和它们的用法，请阅读我们的一些帮助文章：10 个screen命令的示例。

## 9 file

‘file’是一个能提供关于文件类型信息的命令。
```
avi@localhost:~$ file 34.odt
34.odt: OpenDocument Text
avi@localhost:~$ file 34.odt
34.odt: OpenDocument Text
```
## 10 id

上面的命令会打印真正的和有效的用户和组的id。