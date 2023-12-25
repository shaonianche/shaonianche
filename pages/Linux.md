- Oracle cloud 开启 root 登录 #Oracle #Linux
	- #!/bin/bash
	  echo root:123456789 |sudo chpasswd root
	  sudo sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/g' /etc/ssh/sshd_config;
	  sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config;
	  sudo service sshd restart
- VPS 基准测试脚本
	- https://github.com/oooldking/script #vps #测试
	- ```bash
	  wget -qO- --no-check-certificate https://raw.githubusercontent.com/oooldking/script/master/superbench.sh | bash
	  ```
	-