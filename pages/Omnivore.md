## 🔖 Articles
	- [重新思考浏览器输入了 URL 并按下回车之后到底发生了什么——本地 DNS 部分](https://omnivore.app/me/url-dns-18d12e762a7)
	  collapsed:: true
	  date-saved:: [[2024-01-16]]
		- ### Highlights
		  collapsed:: true
			- > 我们先来说说第一个问题——现代的浏览器本身会不会缓存 DNS 记录？
			  > 
			  答案是会的，以 Chrome 为例，我们需要先：
			  > 
			  1. 打开 `chrome://net-export/` 然后开始录制一段时间的记录
			  2. 打开  并上传刚刚的记录
			  > 
			  > 本来这个操作可以在 `chrome://net-internals/#dns` 一步完成的，不知道为啥 Chrome 搞成了上面两步，还引入了一个外部网站 [⤴️](https://omnivore.app/me/url-dns-18d12e762a7#2494f9b6-dbdc-4aa6-927a-37a6afe3c0f4)
			- > ## 浏览器是怎么发出的 DNS 请求 [⤴️](https://omnivore.app/me/url-dns-18d12e762a7#fd436867-77b8-47f0-b963-a210be0fef36)
			- > 操作系统提供了一个叫做 `getaddrinfo()` 的系统 API 供浏览器使用，所以浏览器需要发送一个 DNS 请求也只是和这个接口交互而已，浏览器本身不会自己发送任何奇怪的请求甚至直接读取一个系统文件。 [⤴️](https://omnivore.app/me/url-dns-18d12e762a7#0ccba0fe-a49f-4bd6-ad6f-8c5cd5e9a78b)
			- > 相对比较现代的电脑上，我们应用中的 DNS 请求也并没有直接发送到系统获得的 DNS 服务器上，而是发到了另一个系统级别的缓存中了。
			  > 
			  所以到这里，我们可以修正一下上面的回答，实际的请求顺序是：浏览器 DNS 缓存（未命中） -> 浏览器调用 `getaddrinfo()` 查询数据，其中，`getaddrinfo()` 的查询背后有多个缓存，顺序如下文所述。 [⤴️](https://omnivore.app/me/url-dns-18d12e762a7#63952631-1d01-43e9-9cec-3aa07717db46)
			- > 以我的电脑默认配置为例，实际的 DNS 查询顺序是：
			  > 
			  1. 浏览器 DNS 缓存
			  2. 浏览器调用 `getaddrinfo()` 查询数据，其中 `getaddrinfo()` 会根据如下顺序查询  
			   1. 先看 `/etc/hosts` 文件  
			   2. 通过主机名服务/mDNS 查询  
			   3. 通过 `systemd-resolved` 查询  
			   4. 最后通过 DHCP 下发的 DNS 查询
			  > 
			  > 在 Windows 系统上，这个 nssswitch 的功能被一个称为 Name Resolution Policy Table 的东西替代，可以参考文档 [The NRPT | Microsoft Learn](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn593632%28v=ws.11%29) [⤴️](https://omnivore.app/me/url-dns-18d12e762a7#8107bdfa-1ad5-4e29-880c-dad245637fa0)
	- [史上最全 SSH 暗黑技巧详解 | plantegg](https://omnivore.app/me/ssh-plantegg-18d180982a8)
	  collapsed:: true
	  date-saved:: [[2024-01-17]]
		- ### Highlights
		  collapsed:: true
			- > ### github 上你的公钥
			  > 
			  github可以取到你的公钥，如果别人让你查看他的服务器，直接给 [https://github.com/plantegg.keys这个链接，让他把下载的key](https://github.com/plantegg.keys%E8%BF%99%E4%B8%AA%E9%93%BE%E6%8E%A5%EF%BC%8C%E8%AE%A9%E4%BB%96%E6%8A%8A%E4%B8%8B%E8%BD%BD%E7%9A%84key) 加到 \~/.ssh/authorized\_keys 里面就行了 [⤴️](https://omnivore.app/me/ssh-plantegg-18d180982a8#0d53ed7a-8377-4efc-9210-a4e08c0d4c6a)
	- [Linear Method 中文版 | 产品研发的原则和最佳实践](https://omnivore.app/me/linear-method-18ce7e40a53)
	  collapsed:: true
	  date-saved:: [[2024-01-08]]
		- ### Highlights
		  collapsed:: true
			- > 我们收到很多关于我们如何管理设计和工程团队之间的交接的问题。我们在整个项目设计和实施过程中协作工作，并在编写项目规范时就开始合作。我们在项目团队中工作，所有面向用户的功能，团队中总有一名设计师。我们将设计和工程任务放在同一个团队中，并且设计会创建为独立的 issue。设计师提交他们自己的 issue。工程师们也提交他们自己的 issue。对于任何需要协作的事情，我们会使用 子issue 来分割设计和工程任务。 [⤴️](https://omnivore.app/me/linear-method-18ce7e40a53#8fe2f150-cdf0-4462-881c-0eea68b1a772)
			- > 总的来说，作为一个公司，我们在构建功能时使用项目来组织工作。在我们写完项目规格后，第一个设计任务通常是「探索设计」，我只是用一些时间（一天到一个星期）来探索不同的方向和选项，并弄清楚设计的部分。然后与团队分享，征求反馈意见。我经常在 Linear 评论中粘贴 Figma 截图，并 @提及我希望得到反馈的人。Adrien 喜欢在发布 Figma 链接的同时分享 Loom 视频，并简单描述并说明他希望得到什么反馈。 [⤴️](https://omnivore.app/me/linear-method-18ce7e40a53#d3e80741-3b21-41ed-a4b8-0e052a50fd66)
	- [爲什麼現代 Linux 不再需要 sbin（bin merge 的意義） | YHNdnzj's Blog](https://omnivore.app/me/linux-sbin-bin-merge-yh-ndnzj-s-blog-18b5f36b45a)
	  site:: [YHNdnzj&#39;s Blog](https://yhndnzj.com/2023/09/24/why-we-dont-need-sbin-anymore)
	  author:: Mike Yuan
	  date-saved:: [[2023-10-24]]
	  date-published:: [[2023-09-24]]
	  collapsed:: true
		- ### Highlights
			- > ### 「權限」究竟適用於誰
			  > 
			  要回答「sbin 是否還有意義」這個問題，有一個更底層的問題必須先被回答：「權限」事實上/應該作用於誰？思考下面的例子：當我們運行 fdisk 的時候，是我們沒有「運行命令」的權限，還是命令所要訪問的 device node 我們無權訪問？當我們編輯系統配置的時候，是沒有執行編輯器的權限，還是編輯器沒有向某個文件寫入的權限？我想答案很明晰：「命令本身」並沒有/不受所謂的權限限制，本質在於其需要訪問的資源。 [⤴️](https://omnivore.app/me/linux-sbin-bin-merge-yh-ndnzj-s-blog-18b5f36b45a#66d4adbc-7328-46e0-ae84-922e7acf6c1c)
	- [2019-05-16 前端性能优化（一）性能评估 ~ ThaddeusJiang](https://omnivore.app/me/2019-05-16-thaddeus-jiang-18c664ee572)
	  site:: [thaddeusjiang.com](https://thaddeusjiang.com/2019-05-16-qian-duan-xing-nen-you-hua-yi-xing-nen-ping-gu)
	  date-saved:: [[2023-12-14]]
	  date-published:: [[2019-05-16]]
		- ### Highlights
			- > 使用 incognito 模式主要是为了避免 Chrome 插件对测试的影响。 对于准备测试环境，还有一些其他方法。查看 
			  > 
			  ##  [⤴️](https://omnivore.app/me/2019-05-16-thaddeus-jiang-18c664ee572#63bc5aee-88c5-46e6-8fef-06d53999651d)
	- [2023年诺贝尔经济学奖得主：什么让女性难以兼顾事业和家庭？-虎嗅网](https://omnivore.app/me/2023-18b186f267b)
	  collapsed:: true
	  site:: [huxiu.com](https://www.huxiu.com/article/2155987.html?f=rss)
	  author:: 中信出版
	  labels:: [[RSS]]
	  date-saved:: [[2023-10-10]]
	  date-published:: [[2023-10-10]]
		- ### Highlights
			- > 北京时间10月9日下午，诺贝尔经济学奖获奖者名单揭晓，奖项授予哈佛大学经济学教授克劳迪娅·戈尔丁，以表彰其“增进了我们对女性劳动力市场结果的理解”。 [⤴️](https://omnivore.app/me/2023-18b186f267b#8408382e-be99-461c-b2fc-b322540272ef)
	- [为什么跑步后吃不下，游完泳却变饿死鬼？-虎嗅网](https://omnivore.app/me/-18b186f5710)
	  site:: [huxiu.com](https://www.huxiu.com/article/2153476.html?f=rss)
	  author:: 果壳
	  labels:: [[RSS]] 
	  date-saved:: [[2023-10-10]]
	  date-published:: [[2023-10-10]]
		- ### Highlights
			- > 除了游泳，多数运动在合适的强度和时间下，减肥效果还是不错的。因为运动不仅增加能量消耗，还能短暂抑制食欲，不让我们多吃。这样出量增加入量不变，能量缺口大了减重就快。 [⤴️](https://omnivore.app/me/-18b186f5710#bd87549c-5bda-4bb6-b8df-399f479ba0f7)
			- > 运动对食欲的影响以及如何通过运动来控制食欲。
			  > 
			  • 游泳后的饥饿感与水温有关，冷水增加消耗，温水则没有类似作用。
			  > 
			  • 运动不仅增加能量消耗，还能短暂抑制食欲，有助于减重。
			  > 
			  • 运动时间和强度是影响抑制食欲效果的关键，中等强度运动持续40分钟以上最有效。 [⤴️](https://omnivore.app/me/-18b186f5710#50b4f3c7-aa44-4264-8b0f-5df7472a94c3)
	- [AMS :: Notices of the American Mathematical Society](https://omnivore.app/me/ams-notices-of-the-american-mathematical-society-18ad457ce98)
	  collapsed:: true
	  site:: [American Mathematical Society](https://www.ams.org/journals/notices/202309/noti2781/noti2781.html)
	  author:: Ilya Kapovich
	  date-saved:: [[2023-09-27]]
	- [macOS Containers Initiative](https://omnivore.app/me/mac-os-containers-initiative-18ad44e0b60)
	  site:: [macoscontainers.org](https://macoscontainers.org)
	  date-saved:: [[2023-09-27]]
		- ### Highlights
			- > We’re announcing initial 0.0.1 release of macOS native containers. Yes, you can now **run macOS inside macOS**, build images using Docker and distribute them using registries. [⤴️](https://omnivore.app/me/mac-os-containers-initiative-18ad44e0b60#cfc5ee80-e641-4601-9b7f-4695551182a1)