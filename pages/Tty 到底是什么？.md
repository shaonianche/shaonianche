title:: Tty 到底是什么？
author:: [[laixintao]]
full-title:: "Tty 到底是什么？"
type:: [[Readwise]]
category:: [[articles]]
url:: https://www.kawabangga.com/posts/4515

- [[Readwise]][[2023-03-27]]
	- 因为 `Ctrl+W` 是一个叫 TTY 的东西提供的，其余的三个是 shell 提供的 ([View Highlight](https://read.readwise.io/read/01gwgmrgpanr34wg0mfcbhr60y))
- New highlights added [[2023-03-27]] at 1:33 PM
	- 上面还有一个叫做 “Line discipline” 的东西。这是什么鬼？
	  
	  如它的名字所说，用来“管教” line 的。命令在输入之后，在按下 `Enter` 键之前，其实是存储在 TTY 里面的。存在 TTY 的 line 就可以被 Line discipline 所“管教”。比如它提供的功能有：通过 `Ctrl+U` 删除，也就是说，你按下 `Ctrl+U` 之后，TTY 并不会发送字符给后面的程序，而是会将当前缓存的 line 整个删掉。同理，`Ctrl+W` 删除一个字符也是 Line discipline 所提供的功能。（哇！你现在能通过我的面试了！）我会在后面证明这是 TTY 提供的功能。 ([View Highlight](https://read.readwise.io/read/01gwgr3syade518e7xxperyns8))
	- Line discipline 最大的用处，其实是一个可编程的中间人。它可以 buffer 20 个 TTYs 的内容，直到有一个人按下 Enter 的时候，才会真正将内容发送给后端的程序。一个 Line discipline 模块可以 cache 20 个 TTYs，假设我们需要 30s 输入一个命令的话，那么每一个用户差不多有 1.5s 的执行时间。几乎快了 100 倍。 ([View Highlight](https://read.readwise.io/read/01gwgr49g9w80pbvt5xgxvzn3t))