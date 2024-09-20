## 🔖 Articles
	- [有关 TLS/SSL 证书的一切 | 卡瓦邦噶！](https://omnivore.app/me/tls-ssl-19203dd5381)
	  site:: [kawabangga.com](https://www.kawabangga.com/posts/5330)
	  author:: unknown
	  labels:: [[TLS/SSL]]
	  date-saved:: [[2024-09-18]]
		- ### Highlights
			- > Client –trust–> Root CA –trust–> Intermediate CA –NOT trust –> kawabangga.com — NOT trust –> 我 sign 的 super-bank.com [⤴️](https://omnivore.app/me/tls-ssl-19203dd5381#80dc5aea-4fbc-4b24-8414-e3f694c26008)
			- > * 一个证书只能有一个 issuer，因为 issuer 是证书的固定字段，不是一个 List；
			  * 签名的本质，只是 append 一个 private key 加密的 hash 值；
			  * 中级证书不被客户端直接信任，客户端信任的只有 Root CA； [⤴️](https://omnivore.app/me/tls-ssl-19203dd5381#62363d86-0c7a-41fe-bf0b-922d0a4626aa)
			- > 现在有两种主流的方式，一种是 [CRL](https://en.wikipedia.org/wiki/Certificate%5Frevocation%5Flist)，一种是 [OCSP](https://en.wikipedia.org/wiki/Online%5FCertificate%5FStatus%5FProtocol)。
			  > 
			  原理上，就是 CA 证书自身带有这个信息，告诉客户端在校验证书的时候，应该去访问这个 URL 列表，查看自己要验证的证书是否在吊销列表中，如果在，就不要信任。 [⤴️](https://omnivore.app/me/tls-ssl-19203dd5381#a2cf3364-8f41-46dd-8886-88bbe41bb9e6)
			- > [OCSP Stapling](https://en.wikipedia.org/wiki/OCSP%5Fstapling) 可以解决以上问题。它的核心原理是：
			  > 
			  1. 网站定期去访问 CA 的 OCSP 服务，确认自己的证书是没有被吊销的，拿到 OCSP Response；
			  2. 客户端访问网站的时候，网站连同证书一起出示 OCSP Response，证明自己的证书是没有被吊销的； [⤴️](https://omnivore.app/me/tls-ssl-19203dd5381#c6cf6ab0-a800-4586-8228-23b72ed06cd5)
			- > * CA 在签发证书的时候，必须将签发的证书放到 CT 数据库中，CT 会给证书加 SCT；CA 将签名的证书发回给网站，这个证书是带有 SCT 的；
			  * 客户端访问网站时候，只有证书带有 SCT 才会信任；这样，就保证了所有客户端信任的证书，都在 SC 数据库里面有记录；
			  * 网站可以监控 SC 数据库，关注是否有 CA 签发了自己不知情的证书； [⤴️](https://omnivore.app/me/tls-ssl-19203dd5381#8cfaa8fa-bd39-47d3-8f24-d08a1859682c)
	- [TCP 延迟分析 | 卡瓦邦噶！](https://omnivore.app/me/tcp-191db3bf433)
	  collapsed:: true
	  site:: [kawabangga.com](https://www.kawabangga.com/posts/6378)
	  author:: unknown
	  date-saved:: [[2024-09-10]]
		- ### Highlights
		  collapsed:: true
			- > Ping 的延迟指的是 RTT, Round Trip Time. 即一个包发过去，对方发一个包回来，总延迟是 200ms。一种误解是认为 ping 测得的延迟是 200ms，所以一个请求发过去是 200ms，响应发回来是 200ms，总延迟是 400ms。如果仔细想一想的话，我们在发送端测量延迟的时候，没有办法只测量一个包从发送端达到接收端的延迟。除非是让接收端在回复的时候记录收到包的时间？但是发送端和接收端的时钟可能不一致，如果精确测量的话，协议上就要依赖不同的机器时钟对齐。直接让总时间除以 2？这也意义不大，因为包去和回的路线不一定一样，延迟也不一定是一半一半。所以**我们在讨论延迟的时候，都是默认 RTT**。 [⤴️](https://omnivore.app/me/tcp-191db3bf433#72375542-d3cd-4bbe-92ef-7d40de67251b)
	- [网络中的环路和防环技术 | 卡瓦邦噶！](https://omnivore.app/me/-191db35b2e1)
	  collapsed:: true
	  site:: [kawabangga.com](https://www.kawabangga.com/posts/6291)
	  author:: unknown
	  date-saved:: [[2024-09-10]]
		- ### Highlights
		  collapsed:: true
			- > TTL 的设计原本是为了**防止网络出现环路**，限制一个包能被转发的最大次数。每次转发都会 -1，最后到 0 的时候，如果包还没有到达目的地，设备就会丢弃这个包（然后可能发一个 ICMP 告诉 Src IP 这个包因为 TTL 减到 0 而寿终正寝了） [⤴️](https://omnivore.app/me/-191db35b2e1#275a6ac2-4b68-4ca3-bbbe-2104e6f811bf)
	- [理解网络的分层模型 | 卡瓦邦噶！](https://omnivore.app/me/-191dafc1068)
	  collapsed:: true
	  site:: [kawabangga.com](https://www.kawabangga.com/posts/6295)
	  author:: unknown
	  date-saved:: [[2024-09-10]]
		- ### Highlights
		  collapsed:: true
			- > 这样很多问题其实也就不是问题了。比如「粘包」问题，是一个被人诟病的面试题。它是问「如果使用 TCP 发送多个包，这些包粘在一起无法分开怎么办？」这么问出来就显得提问者不懂 TCP，因为 TCP 的设计就是**帮助用户发送一个字节流**，它本身就没有「包」这个概念，所有的数据就是要「粘」在一起发送的。这并不能说是一个问题，而是 TCP 本身的特性。如果你使用 TCP 协议，你就要在这之上设计自己的协议，把自己的协议设计成可以让 TCP 使用「流」的方式传送。比如，HTTP 协议是使用 `\r\n\r\n` 来分割来 Header 和 Body，然后通过读 Header 中 `Content-length` 的长度来判断 Body 要读到那里；Redis 协议大致是先用一个数字表示内容的长度，读完了的话，再读就是下一个请求了。 [⤴️](https://omnivore.app/me/-191dafc1068#d1943514-bbb9-4fd3-b11d-d2dcbd63344b)
	- [为什么 中文 不 需要 空格](https://omnivore.app/me/-191da04c1e3)
	  collapsed:: true
	  site:: [微信公众平台](https://mp.weixin.qq.com/s/AL66AhcLjGbyEnbNvyJ2FA)
	  author:: 科学大院
	  date-saved:: [[2024-09-10]]
	  date-published:: [[2024-09-09]]
		- ### Highlights
		  collapsed:: true
			- > 英语作为一种字母书写系统，每个字母表示一个音素，通常由多个字母组成一个单词。英语文本用空格清晰而明确地标记了一个词的起始和结束位置，即**词边界**。中文就不需要标记词边界么？
			  > 
			  中文是一种典型的表意书写系统，每个汉字表示一个音节或语素。中文文本由连续的汉字组成，不同的词之间没有用空格分隔。大多数中文词可以用一到两个汉字表示，词长较短且变化较小（平均词长为1.40个汉字，标准差为0.57）。因此，中文读者在阅读时容易预测词的长度，从而更快识别词的开始和结束位置，即**中文词边界位置的不确定性较小**。 [⤴️](https://omnivore.app/me/-191da04c1e3#9d7590f7-11b2-49da-9164-b26a24de3529)
	- [想必多年后，那字也被沙尘抹去的石碑，依然屹立 – Telegraph](https://omnivore.app/me/telegraph-191d9e14c1d)
	  collapsed:: true
	  site:: [Telegraph](https://telegra.ph/%E6%83%B3%E5%BF%85%E5%A4%9A%E5%B9%B4%E5%90%8E%E9%82%A3%E5%AD%97%E4%B9%9F%E8%A2%AB%E6%B2%99%E5%B0%98%E6%8A%B9%E5%8E%BB%E7%9A%84%E7%9F%B3%E7%A2%91%E4%BE%9D%E7%84%B6%E5%B1%B9%E7%AB%8B-08-30)
	  author:: unknown
	  date-saved:: [[2024-09-10]]
	  date-published:: [[2024-08-30]]
		- ### Highlights
		  collapsed:: true
			- > 以乐观与开放的态度去接受新事物，总是一个伟大理念与事物的开始。   
			  这场伟大的里程碑式胜利，是属于所有真正热爱游戏的玩家和开发者的。 [⤴️](https://omnivore.app/me/telegraph-191d9e14c1d#76d4c808-1b2d-4ea2-ac52-97bd62e3938d)
			- > 很多开发者总想做对的事情，害怕自己做错了。   
			  但这游戏再次证明了**游戏不是要做对的事情，而是要做有趣的、没见过的东西。**   
			  当你想做对的事情的时候，那就意味着已经有人做过这件事情，证明他是对的了。 [⤴️](https://omnivore.app/me/telegraph-191d9e14c1d#63b24f52-b4da-4e4e-85b2-ef0e9f4ad144)
	- [After six years in China, our bureau chief says farewell](https://omnivore.app/me/after-six-years-in-china-our-bureau-chief-says-farewell-1919c2913ae)
	  collapsed:: true
	  site:: [archive.ph](https://archive.ph/Dc6U5)
	  author:: unknown
	  date-saved:: [[2024-08-29]]
	  date-published:: [[2024-08-29]]
		- ### Highlights
		  collapsed:: true
			- >  [⤴️](https://omnivore.app/me/after-six-years-in-china-our-bureau-chief-says-farewell-1919c2913ae#85bed7b3-f7af-4e43-b521-85798c2aab46)
	- [What Every Programmer Should Know About Memory](https://omnivore.app/me/cpumemory-18cf2b84eb6)
	  collapsed:: true
	  site:: [akkadia.org](https://www.akkadia.org/drepper/cpumemory.pdf)
	  author:: Ulrich Drepper Red Hat, Inc. drepper@redhat.com
	  date-saved:: [[2024-01-10]]
		- ### Highlights
		  collapsed:: true
			- > As CPU cores become both faster and more numerous, the limiting factor for most programs is now, and will be for some time, memory access. Hardware designers have come up with ever more sophisticated memory handling and acceleration techniques–such as CPU caches–but these cannot work optimally without some help from the programmer. Unfortunately, neither the structure nor the cost of using the memory subsystem of a computer or the caches on CPUs is well understood by most programmers. This paper explains the structure of memory subsys- tems in use on modern commodity hardware, illustrating why CPU caches were developed, how they work, and what programs should do to achieve optimal performance by utilizing them. [⤴️](https://omnivore.app/me/cpumemory-18cf2b84eb6#a9a8f670-5716-4f08-8430-c6e9c4c77b24)
	- [【Rust 研学】 | Iceoryx2 : 汽车领域关键中间件迈向 Rust](https://omnivore.app/me/rust-iceoryx-2-rust-18d5452c1d5)
	  collapsed:: true
	  site:: [Weixin Official Accounts Platform](https://mp.weixin.qq.com/s/OHTZU4MhkzYvQQNwwYMBkQ)
	  author:: 张汉东
	  date-saved:: [[2024-01-29]]
	  date-published:: [[2024-01-19]]
		- ### Highlights
		  collapsed:: true
			- > 大多数先进的驾驶辅助系统（ADAS）实现了诸如车道保持辅助或自动紧急制动等功能，这些系统基于微控制器 ECU。在这样的 ECU 上，数十个或数百个组件以不同的频率运行子任务。通常，这些组件嵌入在 **AUTOSAR 经典运行时环境**（RTE）中，这是一个行业标准，旨在促进供应商和原始设备制造商之间的互操作性。 [⤴️](https://omnivore.app/me/rust-iceoryx-2-rust-18d5452c1d5#12eb24fc-34f5-41e9-ba53-605390bbc41c)
			- > > 引自：\# 详解博世智驾中间件——EDMS\[4\]
			  > 
			  **软件定义汽车的总体架构可以分为四层架构**：
			  > 
			  * 硬件平台，异构分布式硬件架构；
			  * 系统软件层，包括虚拟机、系统内核、POSIX、Autosar 等；
			  * 应用中间件和开发框架包括功能软件、SOA 等；
			  * 应用软件层，包括智能座舱 HMI、ADAS/AD 算法、网联算法、云平台等。
			  > 
			  广义操作系统是指基于内核 OS 之上的 Middleware（中间件），包括了系统软件层（内核、虚拟化、中间件）、功能软件层（共性功能模块以及相关中间件）和 API 接口。 [⤴️](https://omnivore.app/me/rust-iceoryx-2-rust-18d5452c1d5#68820403-2e4b-4773-987a-8af8e04eca7b)
			- > eclipse-zenoh/zenoh [⤴️](https://omnivore.app/me/rust-iceoryx-2-rust-18d5452c1d5#13ef1161-6e7b-4058-b43f-98d89664c7e2) 
			  
			  note:: https://github.com/eclipse-zenoh/zenoh
			- > 目前行业普遍采用的智能驾驶操作系统包括 QNX Neutrino、RT Linux，以及其他 RTOS（如 FreeRTOS、VxWorks 等），基于第三代微内核技术的开源微内核 seL4 也愈发受到国内车企和科技企业的关注，理想、蔚来、莲花汽车、地平线、小米等科技企业相继加入了 seL4 基金会，共同推动 seL4 微内核的发展。 [⤴️](https://omnivore.app/me/rust-iceoryx-2-rust-18d5452c1d5#93fa5060-9305-4507-895b-2f50f667d5aa)
	- [重新思考浏览器输入了 URL 并按下回车之后到底发生了什么——本地 DNS 部分](https://omnivore.app/me/url-dns-18d12e762a7)
	  collapsed:: true
	  site:: [nova.moe](https://nova.moe/rethink-type-url-dns/)
	  author:: unknown
	  date-saved:: [[2024-01-16]]
	  date-published:: [[2024-01-08]]
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
	  site:: [plantegg](https://plantegg.github.io/2019/06/02/%E5%8F%B2%E4%B8%8A%E6%9C%80%E5%85%A8_SSH_%E6%9A%97%E9%BB%91%E6%8A%80%E5%B7%A7%E8%AF%A6%E8%A7%A3--%E6%94%B6%E8%97%8F%E4%BF%9D%E5%B9%B3%E5%AE%89/)
	  author:: unknown
	  date-saved:: [[2024-01-17]]
	  date-published:: [[2019-06-02]]
		- ### Highlights
		  collapsed:: true
			- > ### github 上你的公钥
			  > 
			  github可以取到你的公钥，如果别人让你查看他的服务器，直接给 [https://github.com/plantegg.keys这个链接，让他把下载的key](https://github.com/plantegg.keys%E8%BF%99%E4%B8%AA%E9%93%BE%E6%8E%A5%EF%BC%8C%E8%AE%A9%E4%BB%96%E6%8A%8A%E4%B8%8B%E8%BD%BD%E7%9A%84key) 加到 \~/.ssh/authorized\_keys 里面就行了 [⤴️](https://omnivore.app/me/ssh-plantegg-18d180982a8#0d53ed7a-8377-4efc-9210-a4e08c0d4c6a)
	- [Linear Method 中文版 | 产品研发的原则和最佳实践](https://omnivore.app/me/linear-method-18ce7e40a53)
	  collapsed:: true
	  site:: [Linear Method 中文版](https://linear-method.cn/manage-design-projects.html)
	  author:: unknown
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
	  collapsed:: true
	  site:: [thaddeusjiang.com](https://thaddeusjiang.com/2019-05-16-qian-duan-xing-nen-you-hua-yi-xing-nen-ping-gu)
	  author:: unknown
	  date-saved:: [[2023-12-14]]
	  date-published:: [[2019-05-16]]
		- ### Highlights
			- > 使用 incognito 模式主要是为了避免 Chrome 插件对测试的影响。 对于准备测试环境，还有一些其他方法。查看 
			  > 
			  ##  [⤴️](https://omnivore.app/me/2019-05-16-thaddeus-jiang-18c664ee572#63bc5aee-88c5-46e6-8fef-06d53999651d)
	- [2023年诺贝尔经济学奖得主：什么让女性难以兼顾事业和家庭？-虎嗅网](https://omnivore.app/me/2023-18b186f267b)
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
	  collapsed:: true
	  site:: [macoscontainers.org](https://macoscontainers.org)
	  author:: unknown
	  date-saved:: [[2023-09-27]]
		- ### Highlights
			- > We’re announcing initial 0.0.1 release of macOS native containers. Yes, you can now **run macOS inside macOS**, build images using Docker and distribute them using registries. [⤴️](https://omnivore.app/me/mac-os-containers-initiative-18ad44e0b60#cfc5ee80-e641-4601-9b7f-4695551182a1)