title:: Linux內核設計的藝術
author:: [[新設計團隊]]
full-title:: "Linux內核設計的藝術"
type:: [[Readwise]]
category:: [[books]]

- [[Readwise]][[2023-03-29]]
	- BIOS程序被固化在計算機主機板上的一塊很小的ROM芯片裡。通常，不同的主機板所用的BIOS也有所不同，就啟動部分而言，各種類型的BIOS的基本原理大致相似。為了便於大家理解，我們選用的BIOS程序只有8KB，所佔地址段為0xFE000～0xFFFFF，如圖1-1所示。現在CS：IP已經指向了0xFFFF0這個位置，這意味著BIOS開始啟動了。隨著BIOS程序的執行，屏幕上會顯示顯卡的信息、內存的信息……說明BIOS程序在檢測顯卡、內存……這期間，有一項對啟動（boot）操作系統至關重要的工作，那就是BIOS在內存中建立中斷向量表和中斷服務程序。 ([View Highlight](https://read.readwise.io/read/01gwp51mprg8apzh4nppffznxb))