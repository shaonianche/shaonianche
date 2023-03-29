- bash commands
	- 查找所有图片
		- ```bash
		  for f in **/*.jpg; do echo "$f"; done
		  ```
	- 统计常用历史命令
		- ```bash
		  history |
		  awk '{CMD[$2]++;count++;}END \
		  { for (a in CMD)print CMD[a] " " \
		  CMD[a]/count*100 "% " a;}' |
		  grep -v "./" |
		  column -c3 -s " " -t |
		  sort -nr |
		  nl |
		  head -n10
		  ```
	- 备份文件
		- ```bash
		  cp file{,.bak}
		  ```