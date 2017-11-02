# 树莓派新版镜像使用
### 0 写入镜像
```
镜像版本：2017-04-10-raspbian-jessie.img
烧制工具：Win32DiskImager
SD卡大小：64G
```

### 1 配置
由于新版系统默认不开启SSH的，所以在`boot`下新建一个`ssh`文件即可。如果想要连接wifi的话，树莓派的 /boot 目录下新建 wpa_supplicant.conf 文件，按照下面的参考格式填入内容并保存 wpa_supplicant.conf 文件。
```python
country=CN
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
 
network={
ssid="WiFi名字"
psk="密码"
key_mgmt=WPA-PSK
priority=1
}
 
network={
ssid="WiFi（另一个）"
psk="密码"
key_mgmt=WPA-PSK
priority=2
scan_ssid=1
}
```

### 2 禁止休眠

#### 一、禁止屏幕在图形界面下休眠

在`/etc/profile.d`路径下新建一个文件，如`Screen.sh`，并将下面两条命令写入该文件，即可以实现永久禁用。
```
xsetdpms 0 0 0
xsets off
```
#### 二、禁止屏幕在 Console 终端下休眠
执行下面的命令（重启后失效）：
```
setterm -blank 0
```

### 3 安装字体显示中文
#### 一、安装字体
```
sudo apt-get install ttf-wqy-zenhei
```
#### 二、安装输入法
```
sudo apt-get install scim-pinyin
```
#### 三、选择中文及输入法
安装完毕后输入
```
sudo raspi-config
```
然后选择`change_locale`，在`Default locale for the system environment`中选择`zh_CN.UTF-8`,配置完成之后，输入命令
```
sudo reboot
```



