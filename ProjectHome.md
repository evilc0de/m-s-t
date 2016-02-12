<h3>简介<br>
<br>==========<h3 />
M.S.T.是一款基于python2.7的国产漏洞利用平台<br>
专注于web exp<br>
区别于msf对web的忽略<br>
使用者可以使用py轻松编写自己的插件<br>
官方网站提供了插件的上传与下载<br>
非常利于exp的共享与自动化攻击的实现<br><br>
<h3>下载<br>
<br>==========<h3 />
由于code.google.com不再提供下载<br>
下载请移步百度托管：<br>
<br>
<a href='http://mstoor.duapp.com/?do=download'>M.S.T.Downloads</a><br><br>
SVN托管:<br>
<a href='http://code.google.com/p/m-s-t/source/browse/'>http://code.google.com/p/m-s-t/source/browse/</a><br>
<h3>插件<br>
<br>==========<h3 />
使用者可以根据自己的需求编写插件<br>
也可以到官方望着那提交、下载、更新插件<br>
<a href='http://mstoor.duapp.com/?do=index'>插件下载</a><br>
<a href='http://mstoor.duapp.com/post/'>插件提交</a><br><br>
<h3>安装<br>
<br>==========<h3 />
该平台基于python2.7<br>
可跨平台运行<br>
支持linux,windows,mac<br>
使用前请确保安装了python<br>
如果没有，<br>
<a href='http://python.org/download/'>python Download</a> 下载安装<br>
windows:<br>
可直接命令行mst.py或者<b>双击mst.py</b><br>
linux和mac:<br>
<b>python mst.py</b><br><br>
<h3>基础命令<br>
<br>==========<h3 />
【help】------------------------------------------显示帮助<br>
【show】------------------------------------------列表插件<br>
【searh】-----------------------------------------搜索插件<br>
【use】-------------------------------------------使用插件<br>
【cls】-------------------------------------------清除屏幕<br>
【exit】------------------------------------------退出程序<br>
【update】----------------------------------------更新程序<br>
【show】+【exploit】------------------------------列表exp插件<br>
【show】+【payload】------------------------------列表payload插件<br>
【show】+【multi】--------------------------------列表辅助插件<br>
【show】+【all】----------------------------------列表所有插件<br>
【use】+【id】/【插件全称】-----------------------使用该插件<br>
【update】+【mst】--------------------------------更新主程序<br>
【update】+【plugins】----------------------------更新插件<br>
【info】------------------------------------------显示插件描述<br>
【opts】------------------------------------------显示插件配置<br>
【set】+【参数】+【值】---------------------------设置参数<br>
【exploit】---------------------------------------开始攻击/识别/run<br><br>
<h3>
插件编写<br>
<br>==========<h3 />
1=》<br>
定义mstplugin类<br>
2=》<br>
类下定义exploit函数<br>
3=》<br>
插件被加载时，会把exploit实例化<br>
4=》<br>
类下：<br>
infos=[['Name','Text'],['Name','Text']]#插件信息<br>
opts=[['opt1','default value','Text'],['opt2','default value','Text']]#插件参数<br>
5=》<br>
exploit函数下：<br>
直接使用opt1和opt2<br>
<a href='http://mstoor.duapp.com/view/?pid=12'>编写示例</a><br>
<br>
<h3>内建函数<br>
==========<h3 />
多色彩输出=><br>
color.cprint('str',RED/GREEN/YELLOW)<br>
