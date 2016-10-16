# Google Search Blocklist (A Chrome Extension)
## 简介
本项目是一个 Chrome 扩展。

本项目是为了让使用 Chrome 的用户更方便地利用 [useless-websites](https://github.com/Feiox/useless-websites)。

本项目基于 Google 为 Chrome 提供的 [Personal Blocklist](https://chrome.google.com/webstore/detail/nolijncfnkgaikbjbdaogikpmpbdcdef) ，做了如下修改：
- 可以从本地文件加载屏蔽列表
- 升级到最新的 jQuery，修复了旧版产生的 CSP 问题
- 修复一些细小问题，删除了一些不必要的文件
- 删除了原扩展的 key，不与原扩展冲突

## 使用方法
- 将本项目 git clone 到本地
- 在 chrome [扩展程序页](chrome://extensions/) 中勾选“开发者模式”
- 点击“加载已解压的扩展程序”，选择项目所在文件夹（加载后可取消勾选“开发者模式”）
- 通过 git pull 更新屏蔽列表
- 两种方式修改屏蔽列表：
 1. 直接修改 domains.js（注意排序）
 2. 修改 domains.csv 并用 python 脚本 csv2js.py 处理（会自动排序）

## 几点说明
- 用户自行添加的域名仍然保存在 Chrome 的 localStorage 中
- 加载屏蔽列表时自行添加的域名和从文件加载的域名分别排序，自行添加的排在前面


******

# [互联网垃圾网站列表](https://github.com/Feiox/useless-websites)

这里是收集到的互联网上的垃圾网站列表。

## 使用
您可以这样利用它：

* Chrome
  * [Personal Blocklist](https://chrome.google.com/webstore/detail/nolijncfnkgaikbjbdaogikpmpbdcdef)
    您可以将它导入到 Personal Blocklist 插件中，用以屏蔽 Google 搜索结果中的垃圾网站。

* Firefox
  * [Hide Unwanted Results of Google Search](https://addons.mozilla.org/en-US/firefox/addon/hide-unwanted-results-of-go/)
    Hide(block) site specific unwanted results of Google Search Also support Bing Search

另外：
* [uBlock Origin](https://github.com/gorhill/uBlock)
  An efficient blocker for Chromium and Firefox. Fast and lean.

P.S.
*我并不是一个 FF 用户，希望您能帮助我找到更多更好用的这类插件*

## 对垃圾网站的定义

* 堆砌关键词换取 SEO，本身并无任何价值
* 虚假搜索引擎，例如 [问叔叔搜索](http://wenshushu.com/?q=abc)、[森林搜索](http://senlinso.com/k/abc)、[谷粉搜搜（假）](http://gfsoso.99lb.net/)
* 恶意爬虫内容聚合站，例如 [人人 IT](http://fanli7.net/index.html)

*P.S. 并不完整，欢迎补充*

## 贡献

我们欢迎任何人向我们贡献垃圾网站的域名列表。
请您通过 issue 提交您找到的垃圾站，或讨论某个站点是否应该被列为垃圾站。
我们也提供了一个简单的 Python 处理脚本，来处理格式、重复等问题。

## 授权协议

The MIT License
