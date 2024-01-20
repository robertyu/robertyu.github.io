## ML

* [Google Research 與 Google DeepMind 開發的新氣象模型 MetNet-3](https://blog.research.google/2023/11/metnet-3-state-of-art-neural-weather.html)這個模型建立在之前的 MetNet 與 MetNet-2 上, 能提供高解析度的 24 小時氣象預測, 包括降水、地面溫度、風速方向和露點等核心變數. MetNet-3 的預測以 2 分鐘為一個時間間隔, 空間解析度介於 1 到 4 公里, 在多區域的 24 小時預測上, 表現超越了現有最佳的單一和多成員基於物理的數值天氣預測模型(NWP), 如 HRRR 和 ENS. <br/> MetNet-3 利用直接觀察氣象數據來訓練和評估, 這些數據來自各種傳感器, 包括地面氣象站和軌道衛星. 它還引入了一種名為 "densification" 的技術, 將傳統基於物理的模型中的數據同化和模擬過程結合成單一神經網路通過, 從而提高了預測的精準度.<br/> MetNet-3 的另一大優勢是其高時空解析度的直接觀測數據, 它可以提供每隔 2 分鐘的完全密集型 24 小時預測, 同時利用來自美國各地約 1000 個氣象站的數據點學習. 此外, 它還預測了每個輸出變量和位置的邊際多項概率分佈, 提供了比平均值更豐富的信息. [論文的連結](https://arxiv.org/abs/2306.06079).
* [E4S](https://e4s2023.github.io/) 是一種比傳統換臉技術更進階、更細緻的面部交換技術. 它利用 "區域GAN反演"（Regional GAN Inversion, 簡稱RGI）來單獨處理臉部的形状和紋理，如皮膚色調、痣或皺紋. 基於預訓練的 StyleGAN 模型，E4S 用特製的編碼器識別並獨立處理臉部各個部位. 它透過樣式和掩碼交換來執行換臉, 並用 "重新著色網絡" 調整光照條件, 確保換臉後的外觀自然逼真. 最後, "面部修復網絡" 會修正換臉過程中可能出現的細節問題. [paper](https://arxiv.org/abs/2310.15081), [repo](https://github.com/e4s2023/E4S2023)
* 

### LLM

* [Meta](https://ai.meta.com) 的 [quick start guide for Llama](https://ai.meta.com/llama/get-started/)
*

### OpenAI

* 11/7 OpenAI Dev Day [Keynote](https://www.youtube.com/watch?v=U9mJuUkhUzk)
* 這是 [台灣ikala的sega cheng 的文章](https://www.facebook.com/219981/posts/pfbid02cACgazwHnWf2tHFF1s8siRG4cDcqiWeqSGr2aUn3HpuzjUKH6zy8LdVymDQ2TT1Xl/) -> __精簡版__: OpenAI 的 DevDay 沒大突破，只說了 API 便宜了、token 長度增加、能用自己資料庫、自訂模型但價格不明。這次會議主要對開發者說明技術更新。OpenAI 現在專注在改善 AI 基礎架構，但這恰恰是應擔心的地方，因為他們的 GPT-4 雖強，但除了 Anthropic 之外，沒有其他顯著對手。<br/>問題是，沒有超越 GPT-4 的特色，OpenAI 怎麼與 Google、Amazon、Microsoft 這些 Big Tech 競爭？尤其是微軟，雖然曾是合作夥伴，現在卻各走各路，都想把 AI 模型拉到自己的雲端平台。<br/>OpenAI 選擇了封閉策略，全力以赴發展 GPT。但如果微軟不再看好 GPT 的長期潛力，那麼合作可能就會停止。其他 Big Tech 會提供多樣化的基礎設施和模型給開發者，因為模型已不是主要競爭力。隨著時間，模型製作和微調的成本會越來越低，使用成本也會下降。<br/>企業現在重視用自有資料來微調模型，並對 AI 的資安有所顧慮。他們更注重將 AI 應用到業務和提升生產力，像是 Google Workspace 和 Microsoft 365 這類工具和它們的 AI 功能，如 Duet AI 和 Copilot，正因為簡單易用而廣受歡迎。<br/>結論是，數位戰爭最終是生態系戰爭。若沒有獨到之處，就難以在既有生態系中脫穎而出。OpenAI 的挑戰在於，當他們的 GPT 特色不再獨一無二，面對 Big Tech 的全方位競爭，將會面臨越來越多的壓力。
* 我個人用chatgpt 最常用的兩個 (頗蠢) ```將上述用繁體中文表達 盡量用台灣用語, 必要的時候可以用英文來準確描述技術術語, 另外逗號請用 ", ", 句號請用 ". "```, ```重點描述內容 將概念列出 盡量用台灣用語, 必要的時候可以用英文來準確描述技術術語, 另外逗號請用 ", ", 句號請用 ". "```
* [搞笑ChatGPT](https://x.com/geekbb/status/1721896096832909795?s=20)
* ![img](/assets/images/20231108.01.jpg)
* [這篇講OpenAI的替代](https://x.com/bindureddy/status/1721919059971936719?s=20), 果然就是時間與金錢. 
* 11/9 ChatGPT 新版一開, 就被打掛 哈哈哈 -> updated [是自己出包](https://status.openai.com/incidents/00fpy0yxrx1q)
* [這篇推文要驗證一下](https://x.com/bitfool1/status/1722190312226124254?s=20)
* [generative-elicitation](https://github.com/alextamkin/generative-elicitation), 人類 -> prompt 中間的工具. 有 [論文](https://t.co/nmEYXkcZwJ), 主要分三個領域, 電子郵件驗證、內容推薦和道德推理. SOP for human to prompt.
* [這篇推文在講怎麼從chatgpt裡面撈出markdown](https://x.com/dotey/status/1718828190230089843?s=20)
* 

## Development

### Python
### Database
### Algorithm
### Editor

* 開發用等寬字型, [www.programmingfonts.org](https://www.programmingfonts.org/) 這個網站有很方便比對一百多種開源字體的應用.
* [sudovim](https://github.com/lambdalisue/suda.vim) 聽說很好用, 可惜MAC GG.
* [plenary.nvim](https://github.com/nvim-lua/plenary.nvim#plenaryprofile): neovim的lua lib: 這個程式庫在Neovim以外的環境中無法使用，因為它需要Neovim的函數支持。不過，它應該能與任何近期版本的Neovim兼容。


## MISC

* MAC M1/2/3 有時候玩遊戲會沒聲音, 這個是因為被 Microsoft Teams 的驅動程式卡住了, [參見](https://www.reddit.com/r/macgaming/comments/vrzuvl/mac_mini_m1_some_games_dont_have_sound_solved/) 解法: 移除 `/Library/Audio/Plug-Ins/HAL/MSTeamsAudioDevice.driver`
* [Tor + z-library 查找電子書](https://manateelazycat.github.io/2023/06/28/z-library/), 記錄一下, `sudo pacman -S python-pyqt5 python-pyqt5-sip torbrowser-launcher`, 用 Tor 瀏覽器訪問 z-library 的洋蔥連結： `zlibrary24tuxziyiyfr7zd46ytefdqbqd2axkmxm4o5374ptpc52fad.onion`, 註冊帳號後， 就可以自由的找電子書.
* [suc](https://the-dam.org/docs/explanations/suc.html): <br/>
這篇文章介紹了一種稱為 "suc" 的簡易通訊工具，它使用基於文本的方法來進行通訊。"suc" 利用簡單的 UNIX 指令和文本文件來創建一個類似於 Slack 的通訊平台。主要特點包括： <br/>__使用 SSH 認證和 UNIX 存取控制__："suc" 利用 SSH 進行用戶認證，並使用 UNIX 系統的存取控制來管理權限。 <br/>__基於文本文件的通訊頻道__：用戶通過更新文本文件來進行通訊，可以使用如 tail -f 等 UNIX 工具來閱讀和處理這些文件。 <br/>__支持關鍵字過濾和集中通知__：用戶可以通過關鍵字過濾來減少不必要的通知，或將多個通訊頻道合併成單一訊息流。 <br/>__允許自動化擴展__："suc" 支持透過機器人、掛鉤和腳本等進行半自動化的擴展。 <br/>__靈活的工具整合__："suc" 可以與各種語言編寫的工具整合，只要這些工具能夠讀寫文本。 <br/>__簡潔高效__："suc" 提供的功能與諸如 Mattermost 和 Slack 這樣的大型系統相當，但代碼量極小，這讓人懷疑為何需要那麼複雜的系統。 <br/>總的來說，"suc" 是一種基於 UNIX 傳統的簡潔而有效的通訊工具，適合希望利用文本和命令行工具進行通訊的用戶。
* [pre-commit](https://pre-commit.com): "pre-commit" 是一個用於管理和維護多語言 pre-commit 鉤子（hooks）的框架​​。它的主要用途和特點包括：<br/>__Git 鉤子腳本__：這些腳本有助於在代碼審查前識別簡單的問題，如缺少分號、多餘的空白和調試聲明​​。<br/>__多語言包管理器__："pre-commit" 是一個多語言的包管理器，用於 pre-commit 鉤子。使用者可以指定他們想要的鉤子列表，"pre-commit" 管理這些鉤子的安裝和執行，這些鉤子可以用任何語言編寫。它特別設計為不需要根訪問權限​​。<br/>__安裝__：在運行鉤子之前，需要安裝 pre-commit 包管理器​​。<br/>__配置文件__：用戶需要創建一個名為 .pre-commit-config.yaml 的文件來配置 pre-commit。這個配置文件可以使用預先建立的配置生成，並支持多種編程語言​​。<br/>__安裝 Git 鉤子腳本__：通過運行 pre-commit install 命令來設置 Git 鉤子腳本，這樣 pre-commit 將會在每次 git commit 時自動運行​​。<br/>__選擇性全面運行__：在添加新鉤子時，通常建議對所有文件運行鉤子（通常 pre-commit 只會在 git 鉤子期間對更改的文件運行）​​。<br/>綜合來看，"pre-commit" 為代碼開發提供了一個有效的方式，以自動化的形式管理和維護代碼質量，特別是在多語言環境中。
* [My response to the recent controversy about TCP Brutal](https://gist.github.com/tobyxdd/0993ac063b2eee94f7d36ddd786f52ce): 這篇文章是關於 TCP Brutal 的開發者針對該專案近期引起的爭議所發表的回應。TCP Brutal 是一種 TCP 傳輸控制協議，原本是為了應對中國獨特的互聯網環境而設計的，特別用於反審查代理。中國互聯網通過少數幾個政府控制的節點與全球互聯網相連，這些節點經常出現嚴重的擁堵，限制了帶寬，這導致了所謂的 "故意降低服務質量"。TCP Brutal 被設計來在這樣的環境下提高連接速度，但它會破壞擁塞公平性，從其他用戶那裡奪取帶寬。<br/>開發者說明，TCP Brutal 的起源可追溯至 2015 年，當時基於可靠的 UDP 協議開發了一個代理項目。他發現國際連接的封包丟失率不會隨速度變化（除非達到 ISP 的流量管控限制）。這在當時的中國代理圈子中是一個突破，因為當時沒有 BBR，而大家通常使用的 Cubic 協議依賴於丟包來作為擁塞信號，這是連接速度低的主要原因。後來，該項目被完全重寫為 Go 語言，並替換為基於 QUIC 的協議。開發者也在 Hysteria 中加入了 BBR，認為它比 Brutal 更優雅。盡管如此，基於社區的反饋，他仍保留了 Brutal。<br/>最後，開發者指出 Brutal 主要是為特定用途而設計的，並且在這種用途之外幾乎不可能使用，因為它需要應用程序支持和手動帶寬設置。因此，對於其他國家的用戶來說，它不太可能影響他們的互聯網體驗​. __[另外這篇講TCP Brutal講得蠻清楚的](https://blog.csdn.net/dog250/article/details/113706995)__.
* [A Video Game that Pays: Lessons Learned from Working Remotely](https://dtransposed.github.io/blog/2023/11/02/Remote-SWE/):這篇文章探討了遠程軟體工程工作的特點和學習經驗，特別是作者在遠程工作近兩年後獲得的洞察和教訓​​。以下是幾個關鍵觀點：<br/>__信任__：遠程工作成功的關鍵 - 作者指出，在遠程工作中，信任尤為重要。遠程工作允許人們按照自己的喜好規劃日程，結合工作和個人生活，這需要很強的自律和自我組織能力。相比於辦公室工作，遠程工作更多的是通過不斷產出高質量成果來建立信任，而不是單純的身體出勤​​。<br/>__日常溝通原則__ - 在遠程設置中，應確保同事能信任並依賴你。即使你當時不在線，他們也應該知道你最終會在那裡，不會讓他們掛住。這涉及到結束一天工作時讓同事能順利接手你的工作，學會異步溝通，並且不要讓尋求幫助的人等待太久​​。<br/>__清晰與準確性__：慢即是快 - 遠程工作要求你的溝通盡可能清晰和準確，這樣同事即使在你不在線時也能快速行動，不需要額外的澄清。這種溝通方式與異步工作的要求相關聯，目的是減少歧義，讓同事能迅速理解他們需要做什麼​​。<br/>__接受時區差異的挑戰__ - 在遠程設置中，通常會遇到與同事的時區差異。這可能導致同事在你的工作日尚未結束時已經下班，這對某些人來說可能是挑戰。例如，如果你在巴西遠程工作，與歐洲團隊互動，他們可能在你下午之前就已經完成了工作​​。<br/>總的來說，文章強調了在遠程軟體工程工作中建立信任、有效溝通和適應時區差異的重要性，並分享了一些具體的策略和經驗教訓。

### 想買的

* [鎮暴槍](https://www.ruten.com.tw/find/?q=鎮暴槍%20tcp) 這一陣子有摩托車騎士被逼車, 汽車車主下車就被摩托車騎士用這個射到不要不要的. 所以跑去搜尋了一下, 真是除了板凳之外的居家必備良品, 畢竟台灣野狗實在太多了. 記得配合這篇 [![Watch the video](https://img.youtube.com/vi/adIiAz9LNOY/hqdefault.jpg)](https://www.youtube.com/embed/adIiAz9LNOY) 這樣就可以在恐懼的狀況下抵抗野犬了!
* 

### 影視文化
### Cook

##### すき焼き
* 牛肩ロース肉（薄切り）：牛肩里脊肉（薄切片），300克
* 焼き豆腐：烤豆腐，1塊
* ねぎ：青蔥，2根
* しらたき：白滌麵，200克
* えのきたけ：金針菇，1包
* 生しいたけ：鮮香菇，4片
* 春菊：唐菜（春菊），100克
* 牛脂（またはサラダ油）：牛脂（或沙拉油），適量
* 卵：雞蛋，4個
* キッコーマン特選丸大豆しょうゆ：Kikkoman特選全豆醬油，100毫升
* マンジョウ濃厚熟成本みりん：萬城濃厚熟成本味醂，100毫升
* 砂糖：砂糖，4大匙
* 水：水，100毫升

* 將牛肉和烤豆腐切成方便食用的大小。將蔥切成1厘米寬的斜片。將白滌麵煮熟後切成適合食用的長度。將金針菇和鮮香菇的根部去掉後切半，將唐菜切成5厘米長。將（A）中的材料混合好備用。
* 中火加熱鍋子，將牛脂（或沙拉油）融化並使其均勻鋪在鍋底。
* 炒香蔥，香味出來後迅速煎牛肉，然後倒入（A）的醬汁。
* 將火調至小火，加入其他食材並用中火煮。為了讓味道充分滲透，烤豆腐需要在烹飪過程中翻面。待所有食材煮熟後，蘸上攪拌好的雞蛋液食用。


##### 壽司

* 海苔兩片, 小黃瓜, 尋味棒, 雞蛋兩顆, 米飯, 肉鬆 蝦卵/胡蘿蔔/蝦 之類的 
* 壽司醋: 白醋250cc, 昆布10g, 冰糖40g, 玫瑰鹽1/2匙 -> 泡2-3小時
* 煎蛋, 先塗油, 熱鍋, 蛋下去轉中火, 鍋子旋轉均勻加熱, 邊緣捲起來後, 翻面(手)關火. 蛋皮放涼捲起來切絲
* 煮飯 米:水 1:1 因為後面會加壽司醋 (__這邊要找一下比例__)
* 熱飯 分次加壽司醋 攪拌
* 保鮮膜 海苔 旁邊準備熱水手可以沾一下 (海苔細的朝下/外)

### 有趣
