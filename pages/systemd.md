title:: systemd
author:: [[陈少举]]
full-title:: "\#笔记 Linux 下，在 systemd 的服务配置文件里，若需要做到服务进程崩溃后自动重启，可在对应配置文件的[Service]下指定 Restart=on-Failure（失败时重启）和 RestartSec=5s（等待 5 秒重启），存盘退出后执行 Systemctl Daemon-Reload 即可。"
type:: [[Readwise]]
category:: [[articles]]
url:: https://twitter.com/chenshaoju/status/1493656018014052353?s=20

- [[Readwise]][[2023-03-27]]
	- 在 systemd 的服务配置文件里，若需要做到服务进程崩溃后自动重启，可在对应配置文件的[Service]下指定 Restart=on-failure（失败时重启）和 RestartSec=5s（等待 5 秒重启），存盘退出后执行 systemctl daemon-reload 即可 ([View Highlight](https://read.readwise.io/read/01gwga6f4jyhhr5ze1v6a9am2h))