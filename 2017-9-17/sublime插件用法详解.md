# sublime 插件介绍及用法详解
##### ColorPicker
###### 介绍
     通常，如果你想使用一个颜色选择器则可能打开 Photoshop 或 GIMP。而在 Sublime Text 中，你可以使用内置的颜色选择器。

###### 用法
    To insert or change a selected color, use:
       1. Linux: ctrl+shift+c
       2. Windows: ctrl+shift+c
       3. OS X: super+shift+c
       By default, the hex color code is inserted using uppercase letters (#ABCDEF, for example). To use lowercase letters (#abcdef) instead, copy the contents of Preferences → Package Settings → ColorPicker → Settings—Default to the empty file created by selecting Preferences → Package Settings → ColorPicker → Settings—User, then change "color_upper_case" to false.
       
##### SublimeREPL
###### 介绍
    这可能是对程序员很有用的插件。SublimeREPL 允许你在 Sublime Text 中运行各种语言（NodeJS ， Python，Ruby， Scala 和 Haskell 等等）。
###### 用法
      参照：(https://github.com/wuub/SublimeREPL)
      
##### SublimeLinter插件
###### 介绍
    SublimeLinter 是前端编码利器——Sublime Text 的一款插件，用于高亮提示用户编写的代码中存在的不规范和错误的写法，支持 JavaScript、CSS、HTML、Java、PHP、Python、Ruby 等十多种开发语言。这篇文章介绍如何在 Windows 中配置 SublimeLinter 进行 JS & CSS 校验。
    
##### SideBarEnhancements插件
###### 介绍
    SideBarEnhancements是一款很实用的右键菜单增强插件；在安装该插件前，在Sublime Text左侧FOLDERS栏中点击右键，只有寥寥几个简单的功能；强大的是，该插件还能让我们自定义快捷键呼出某个浏览器以预览页面！这样就不用到项目目录下寻找和拖动到特定浏览器中预览了。
    安装此插件后，点击菜单栏的preferences->package setting->side bar->Key Building-User，键入以下代码：
    [   
    { "keys": ["ctrl+shift+c"], "command": "copy_path" },
    //chrome
    { "keys": ["f2"], "command": "side_bar_files_open_with",
            "args": {
                "paths": [],
                "application": "C:\\Users\\jeffj\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe",//换成自己的路径
                "extensions":".*"
            }
     }

##### HTML-CSS-JS Prettify
###### 介绍
    一款集成了格式化（美化）html、css、js三种文件类型的插件，即便html,js写在PHP文件之内。插件依赖于nodejs，因此需要事先安装nodejs，然后才可以正常运行。插件安装完成后，快捷键ctrl+shift+H完成当前文件的美化操作。插件对html、css文件的美化不是非常满意，但还可以，后面将说明如何修改css美化脚本。本人用起来超级爽的，鉴于篇幅，就不赘述，可以参见这篇介绍: (http://frontenddev.org/article/sublime-does-text-three-plug-ins-html-and-css-js-prettify.html)
###### 用法
```Ctrl+Shift+h```

##### WakaTime
###### 介绍
    WakaTime可以做到精确地统计到你花在某个项目上的时间;WakaTime针对不同的IDE，拥有不同的插件，在Sublime上安装着插件，就能统计到我使用Sublime进行的所有项目的行为。可以高效管理和知晓自己code时间；并且，统计完善。