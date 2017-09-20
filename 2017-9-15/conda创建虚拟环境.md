# conda创建虚拟环境
#### 1.查看包
* conda list:查看安装了那些包
* conda env list：查看有那些虚拟环境
* conda -V：查看conda的版本

#### 2.创建虚拟环境
conda命令创建虚拟环境时，必须指定一个或者几个你需要的package。
```
conda create -n py2 python=2.7 anaconda
```
这样就会安装anaconda2版本

#### 3.切换环境
* Linux：source activate name
* windows：activate name

#### 4.关闭环境
* Linux：source deactivate
* Windows：deactivate

#### 5.移除虚拟环境
```
conda remove -n name --all
```
## virtualenv创建虚拟环境
#### 1.安装virtualenv
```
$ pip install virtualenv
```

#### 2.创建虚拟环境
```
$ mkdir myproject
cd myproject
virtualenv venv
```
创建了一个名为myproject的文件夹，在这个文件夹里创建虚拟环境venv
#### 3.激活虚拟环境
* Linux：venv/bin/activate
* windows: venvscriptsactivate

#### 4.退出虚拟环境
同conda
