# 毕业设计论文(V1.0)
[TOC]

## 引言

## 第一章 绪论

## 第二章 技术理论
### 2.1 CMS系统搜索引擎Elasticsearch
        Elasticsearch是一个开源的搜索引擎，建立在一个全文搜索引擎库Apache Lucene基础之上。Lucene 可以说是当下最先进、高性能、全功能的搜索引擎库--无论是开源还是私有。
        Lucene 是许多互联网公司的标准搜索引擎，但它不适合大数据和云计算环境。
        ElasticSearch 最大的特点是提供近乎实时的搜索服务。虽然它是用Java实现的，但是集成了有很多客户端支持比如PHP，Ｒuby，Perl，Python，Scala.NE，JavaScript,Erlang和Clojure.Django,Couchbase和SearchBox也集ElasticSearch中． MongoDB，CounchDB，ＲabbitMQ、ＲSS、Sofa、JDBC、文件系统，Dropbox，ActiveMQ，LDAP，亚马逊，SQS，St9，OAI 和 Twitter 可以直接导入到ElasticSearch。Zookeeper and internal Zen Discovery可用于发现自动节点，所有的分片和副本可以移动到任何节点的ElasticSearch集群中。索引可以分发到指定的分片和节点，而且它是ＲESTFUL架构的。
        因为我们想支持全文检索，所以需要为每一条日志建立索引;但同时，日志事件在一定时间后自动可以被丢弃。ElasticSearch的设计模式如下:
        
```json
{
" _default_" : {
" _ttl" : { / /Default TTL is 6 months．
" enabled" : true，
" default" : 7776000000} ，
" _source" : {
" enabled" : false} ，
" properties" : {
" env" : { / /whole env is used as term in Lucene．
" type" : " string"，
" index" : " not_analyzed" } ，
" eventbody" : { / /log event body is
indexed．
" type" : " string" } ，
" hostname" : {
" type" : " string"，
" index" : " not_analyzed" } ，
" logfilename" : {
" type" : " string"，
" index" : " not_analyzed" } ，
" logpath" : {
" type" : " string"，
" index" : " not_analyzed" } ，
" logtype" : {
" type" : " string"，
" index" : " not_analyzed" } ，
" timestamp" : { / /timestamp and nanotime are
used for sorting
" type" : " long"，
" ignore_malformed" : false} ，
" nanotime" : {
" type" : " long"，
" ignore_malformed" : false}
} } }
```

### 2.2
### 2.3

## 第三章 软件设计

## 第四章 测试
### 4.1 测试环境
#### 4.1.1 CentOS
        由于没有足够的资金支持，基于硬件创建了虚拟机。本研究使用Linux虚拟服务器（Linux virtual server，LVS）技术进行负载均衡，从而提供给用户访问一台超高性能服务器的效果。
        LVS技术支持通过配置多个高速局域网服务器来进行任务分配，其对外的接口则为固定的IP地址和端口，从而提供任务分发转移的负载调度功能。
        此外，LVS技术支持热处理，在正常工作的情况下增加或者删除节点。LVS的负载调度器（director）可以设置3种工作模式：
        一是地址转换，负载调度器通过算法将内网地址进行映射，外网数据分组通过映射的地址进行分发;
        二是通过IP隧道，负载调度器进行调度请求，通过IP隧道客户端数据分组进行封装发给服务器，服务器直接响应客户端；
        三是直接路由。适用于集群内的服务器都在一个网段，数据分组直接由负载调度器发给实际服务器，该种方式速度快，且开销较少。
        LVS调度算法主要有等比例轮转、加权轮循、目标地址散列调度、源地址散列调度等静态调度算法以及最少连接、加权最少连接、永不排队、动态目标地址散列、带复制的动态目标地址散列等动态调度算法。IP虚拟服务器（IP virtual server，IPVS）技术是一种工作在网络模型第四层的高效交换机，可以针对不同的网络选择不同的调度算法。在小型的分布式负载中，唯一从软件技术上能达到硬件F5量级的方案就是采用LVS技术。

|表4-1 硬件测试环境||
|:--|:--|
|ElasticSearch服务器||
|CPU数目|4|
|CPU主频|2.67G|
|内存|4G|
|硬盘容量|500G|
|碎片|5|
|副本|0|
|ES服务器的数量|1|

#### 4.1.2 WindosServer 2016
1. 服务支持组件安装方法
     1.1 系统自带组件的安装方法
        Win2016 系统默认的情况下已经安装了Internet信息服务(IIS)管理器、ASP 及 ASPX，直接通过点击开始菜单→控制面版→添加或删除程序→添加/删除 Windows组件(A)，弹出 Windows组件向导。在这里添加需要安装的各种 Win2016系统自带的组件服务，如电子邮件服务，这一组件可以使用Win2016系统自带的电子邮件组件来配置小型邮件服务器，这是 Win2016系统的一项新功能。如果要安装其它组件的支持，选中应用程序服务器，然后点击下面的详细信息按钮，就会弹出一个窗口，再在该窗口里选择你需要安装的其它服务。
2. 非系统自带组件的安装方法
        默认的情况下，CGI、PHP、JMAIL、MySql并不是Win2016自带的组件服务，下面分别介绍一下它们的安装方法。
      2.1 CGI 支持安装方法
        首先登陆www.cgi.net网站，下载ActivePerl-5.8.3.809-MSWin32-x86.msi，安装CGI的支持软件.然后点击开始菜单→程序→管理工具→Internet信息服务(IIS)管理器，在弹出IIS管理器窗口中，双击本地计算机，在弹出的关联菜单中，右键点击网站选择属性后弹出网站属性窗口，再点击主目录→配置→映射，弹出一个添加/编辑应用程序扩展名映射窗口，在可执行 文件(X)文本框中输入C:\Perl\bin\perlis.dll，在扩展名(E)：里输入.cgi，在动限制为(L)文本框中输入：GET,HEAD,POST,TRACE 。点击WEB服务扩展，分别选中Perl CGI Extension及Perl ISAPI Extension选项，点击允许使用这两个扩展服务，因为这两个CGI支持的扩展在默认情况下是禁止使用的。
    2.2 PHP 支持安装方法
        Win2016在IIS6.0的安全性方面有了提高，所在在win2016中IIS6的PHP配置和win2K的也略有不同。首先到www.php.net网站下载php-4.3.6-Win32 PHP支持软件。注意：在安装php-4.3.6-Win32之前确保IIS6.0已经启动了，并且能够访问。接着将php-4.3.6-Win32解压到c:\php，将PHP目录内的php.ini-dist文件拷贝到Windows目录内，改名为 php.ini，根据需要修改 php.ini文件内容，
        如要使用session功能，请建立c:\tmp目录，并将php.ini文档内session.save_path的值设置成为绝对路径c:\tmp，将PHP目录内的Php4ts.dll文件复制到C:\Windows\System32目录内。打开开始菜单→程序→管理工具→Internet 信息服务(IIS)管理器，就给弹出IIS管理器窗口，在该窗口中，我们双击本地计算机，就会弹出一个关联菜单，右键点击网站选择属性后弹出网站属性窗口，再点击主目录→配置→映射,在弹出的窗口中，在可执行文件(X) 文本窗口里输入C:\php\sapi\php4isapi.dll，在扩展名(E)：里输入.php，再选择动→限制为(L)：GET,HEAD,POST,TRACE 。最后，点击web服务扩展→新建web服务扩展，就会弹出一个新建服务器扩展窗口，在扩展名(X)中输入php再在要求的文件(E)：里添加地址C:\php\sapi\php4isapi.dll并勾选设置状态为允许(S)。然后点击确定，这样就能让你的IIS6.0支持PHP了。
    2.3 Jmail 支持安装方法
        下载Jmail v4.4 Professional支持软件，双击安装文件JMail44_pro.exe，然后根据提示安装即可。这个可以让你的网站自动发出
        大量的电子邮件的免费邮件服务器，通过Jmail 服务器，可以使你的论坛等程序自动向网友注册时填写的邮箱地址发送注册成功邮件，功能强大，为WEB服务器不可缺少的组件。
    2.4 MySql 数据库支持安装方法
        首先到www.mysql.net网站下载mysql，双击运行MySql的安装程序 setup.exe，根据提示把MySql安装在 C:\Mysql的目录下。
        MySql安装完以后，开始配置Mysql，进到CMD命令提示符窗口，输入以下命令CD\MySql\Bin进入MySql的Bin目录。然后输入安装命令mysqld-nt.exe –install。屏幕将会出现一句Service successfully installed，表示安装成功。为了让MySql在每次系统启动时能自动启动，我们还须进行如下配置， 点击开始菜单→程序→管理工具→服务，找到MySql 服务，点击鼠标右键选择启动，这时 MySql全部安装成功。注意：在MySql安装好后，系统会自动建立一个默认的ROOT 管理员帐号，这个ROOT帐号却是空口令的。如果我们不给这个管理员ROOT帐号设置一个口令，那将等于给黑客打开了入侵服务器大门。 防范方法很简单，给管理员帐号ROOT设置一个口令。在CMD命令提示符下进入C:\Mysql\Bin目录，然后输入以下命令：mysqladmin -u root -p password 新密码，如果我们要为ROOT设置一个密码为active，我们只要输入以下命令：mysqladmin -u root -p password active
        
3. PHP优化
          通过对php.ini(x:\wamp\bin\php/php5.4.12)中的主要相关参数进行合理调整和设置加以实现.
          ()函数禁用(disable_functions=)推荐的禁用函数包括phpinfo、passthru\、exec、1system、popen、ｃhroot、escapeshellcmd、escapeshellcmd、shell_exec、proc_open、proc_get_status等．若服务器中含有一些系统状态检测的PHP程序，则应排除禁用shell_exec，proc_open,proc_get_status等函数．
          (2)脚本最大执行时间(max_execution_time=30)．如果一个PHP脚本被请求，必须在max_execution_time时间内执行完毕，否则停止执行并反馈超时错误．一般该选项保持默认，当PHP脚本确需较长执行时间时，应适当增大该时间设置．
          (3)脚本耗用内存限制(memory_limit=128M).可根据服务器配置适当调高内存限制，这样将Moodle缓存在内存中，以减少对外存的访问，从而显著提高平台访问速度．
          (4)全局函数声明(register_globals=Off)．此配置影响到PHP如何接收传递过来参数．将该选项设置为On很可能在增加安全漏洞的同时隐藏了数据来源，从而引起严重的安全性问题．如果没有特殊的需要，应保留默认设置．
          (5)最大上传文件尺寸限制(upload_max_filesize=2M．根据实际应用需求及服务器配置，可以适当增大该设置．比如在File Uploads区域将允许上传文件的最大值upload_max_filesize=2M调整为8M;Data Handing区域，通过表单POST给PHP的所能接收的最大值(包括表单里的所有值)post_max_filesize=2M，修改为8M．设置上述参数后，上传小于８M的文件一般不成问题．但如果超过８M，还需设置Resource Limits区域参数，将每个PHP页面运行的最大时间max_execution_time=30调整为600，接收数据所需的最大时间max_input_time=60调整为600．
          (6)Session对话存储位置．将Session存放目录指向一个不能通过Web方式访问，但具备可读写属性的文件夹，可有效保存会话数据，方便维护，提高系统安全性．
          (7)最大会话生存周期(session.gc_maxlifetime=1440)．延长会话生存周期可以提高系统的稳定性．
4. MySQL优化
        在客户端使用show variables和show status来查看变量设定值和当前值．通过动态调整MySQL参数来增加缓存，使MySQL性能达到优化[6],从而提高Moodle运行速度．
```sql
MySQL:my.ini(X:\wamp\bin\mysql\mysql5.6.12)
# innodb_buffer_pool_size=16M >>调整为64M(增大buffer_pool_size到50%-80%)
# innodb_additional_mem_pool_size=2M >>调整为8M
# innodb_log_file_size=5M >>调整为32M(增大buffer_pool_size的25%)
```
        

## 第五章 总结


## 参考文献

## 致谢

## 附录