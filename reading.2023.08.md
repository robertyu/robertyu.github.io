hain=srcnat => 離開路由器
chain=dstnat => 進入路由器

action=src-nat => 將來源地址偽裝成指定地址
action=dst-nat => 將目地地址偽裝成指定地址
action=masquerade => 將來源地址偽裝成本地地址(路由器)
action=redirect => 將目的地址偽裝成本地地址(路由器)

src-address => 來源地址
dst-address => 目地地址
in-interface => 來源端口
out-interface => 目地端口

所以...
chain=srcnat action=masquerade src-address=192.168.1.0/24
即為：將來源192.168.1.0/24連外(離開路由器)的ip，偽裝成路由器(本地)地址。

但這樣列會有很大問題，若路由器建了另一個網段192.168.2.0/24
因上面的規則命192.168.1.0/24連出都要先偽裝成路由器地址，
這樣192.168.2.0/24查連線進來的地址只會有路由器的地址，而非192.168.1.x的地址。

所以偽裝應該這樣做才算是佳:
方案1:
chain=srcnat action=masquerade src-address=192.168.1.0/24 dst-address=!192.168.2.0/24
將目地192.168.2.0/24設為例外，這樣連接這個網段時就不會再偽裝成路由器ip。

方案2:
chain=srcnat action=masquerade src-address=192.168.1.0/24 out-interface=pppoe-out1
當目地出口為pppoe-out1(網際網路)，才將來源192.168.1.0/24的ip偽裝成路由器地址。

以上是對來源地址進行偽裝(action=src-nat)；
反推對目的地址(action=dst-nat)進行偽裝，相信也很容易進行思考。

/interface pppoe-client disable pppoe-client-WAN
:delay 2s
/interface pppoe-client enable pppoe-client-WAN


sudo service cron reload

Ubuntu 22.04 and higher
resolvectl flush-caches


## 雜項

* 利用 Bluetooth 鎖 MAC 螢幕: [BLEUnlock](https://github.com/ts1/BLEUnlock)
* ffmpeg to webm.sh - `ffmpeg -i $(IN) -c:v libvpx -pass 1 -an -f rawvideo -y /dev/null  # Generates ffmpeg2pass-0.log`, `ffmpeg -i $(IN) -c:v libvpx -pass 2 -f webm -b:v 400K -crf 10 -an -y $(OUT).webm`
* [onionshare](https://github.com/onionshare/onionshare): Securely and anonymously share files, host websites, and chat with friends using the Tor network. OnionShare 是一個免費的開源工具，允許用戶通過 Tor 網絡安全地分享文件和主持網頁。因為它使用了 Tor，所以分享的內容對於監聽者和攔截者來說是匿名的和難以追踪的。
* [sharry](https://github.com/eikek/sharry): Sharry is a self-hosted file sharing web application. [web site](https://eikek.github.io/sharry). Sharry allows to share files with others in a simple way. It is a self-hosted web application. The basic concept is: upload files and get a url back that can then be shared.
* 

## API 測試

* [hoppscotch](https://github.com/hoppscotch/hoppscotch): Open source API development ecosystem, Lightweight: Crafted with minimalistic UI design. Fast: Send requests and get/copy responses in real-time.
* 

## Open AI

* 串接 [https://github.com/songquanpeng/one-api](https://github.com/songquanpeng/one-api)


## LLaMA

* [Fine-Tune LLaMA 2 with QLoRA](https://colab.research.google.com/drive/1Zmaceu65d7w4Tcd-cfnZRb6k_Tcv2b8g?usp=sharing)
* [Generative Agents: Interactive Simulacra of Human Behavior](https://github.com/joonspk-research/generative_agents), 這個挺有趣的, 一個RPG的遊戲, 可以用AI跑裡面的角色.
* [Sweep](https://github.com/sweepai/sweep): AI-powered Junior Developer for small features and bug fixes. Describe bugs, small features, and refactors like you would to a junior developer, and Sweep: 1. Reads your codebase, 2. Plans the changes, 3. __Writes a pull request with code__. support all languages GPT-4 supports, including Python, JS/TS, Rust, Go, Java, C# and C++.
* 