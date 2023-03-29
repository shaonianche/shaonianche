title:: /Bin /Usr/Bin 和 /Usr/Local/Bin 的故事
author:: [[by laixintao]]
full-title:: "/Bin /Usr/Bin 和 /Usr/Local/Bin 的故事"
type:: [[Readwise]]
category:: #articles
url:: https://www.kawabangga.com/posts/3777

- [[Readwise]][[2023-03-27]]
	- 这些 bin 的位置，仅仅是几个目录而已，并没有本质的区别。哪些命令放在哪里，完全看用户和发行版的喜好。比如，有一些发行版[将 `/bin` 作为 `-> /usr/bin` 的符号链接](https://www.freedesktop.org/wiki/Software/systemd/TheCaseForTheUsrMerge/)。`[`命令，Ubuntu 放在 `/usr/bin` 下，OS X 就放在了 `/bin` 下。
	  
	  但是通常来说，我们都认为这几个目录这样安排：
	  
	  •   `/bin` 放置系统的关键程序，比如 `ls` `cat` ，对于“关键”的定义，不同的发行版会有不同的理解；
	  •   `/usr/bin` 放置发行版管理的程序，比如 Ubuntu 自带 `md5sum` ，这个 binary 就会在这个目录下；
	  •   `/usr/local/bin` 放置用户自己的程序，比如你编译了一个 gcc，那么 gcc 这个可执行 binary 应该在这个目录下；
	  •   除此之外，还有对应的三个目录 `/sbin` `/usr/sbin` `/usr/local/sbin` ，放置系统管理的程序，比如 `deluser` `chroot` `service` ；
	  
	  需要再次强调，这是一种文件的管理方式而已，你甚至可以把自己的 binary 放到 `$HOME/bin` 下。还有，OS X 用 [homebrew](https://brew.sh/) 安装的软件，会放在 `/usr/local/Cellar` 下，然后在 `/usr/local/bin` 创建一个指向相关 bin 目录的符号链接；但是在 Ubuntu 下，会放到 `/usr/bin` 下。 ([View Highlight](https://read.readwise.io/read/01gwgs0w2n38hpr8cvxhxwgm88))