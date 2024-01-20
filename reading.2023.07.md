## MISC

* [Degate](https://github.com/DegateCommunity/Degate) : A modern and open-source cross-platform software for chips reverse engineering. [Web Site](https://www.degate.org/)
* [Run-in-Sandbox](https://github.com/damienvanrobaeys/Run-in-Sandbox): Run PS1, VBS, CMD, EXE, MSI, Intunewin, MSIX, or extract ISO, ZIP in Windows Sandbox very quickly just from a right-click. Prerequisites: At least Windows 10 1903, Windows Sandbox feature enabled, Admin rights to install the tool.
* [Payapl 網站整合](https://developer.paypal.com/docs/checkout/standard/integrate/?_ga=2.257555011.999652037.1687856298-967158204.1687856298)
*  找時間真的要好好搞清楚 怎麼用鍵盤移動: [How to move the cursor word by word in the OS X Terminal](https://stackoverflow.com/questions/81272/how-to-move-the-cursor-word-by-word-in-the-os-x-terminal), 垂直選擇的部分: [Sublime](https://superuser.com/questions/93573/select-text-in-iterm-using-keyboard)
*  [not-yet-awesome-rust](https://github.com/not-yet-awesome-rust/not-yet-awesome-rust): A curated list of Rust code and resources that do NOT exist yet, but would be beneficial to the Rust community. 只能說這社群真給力
*  [Advanced macOS Command-Line Tools](https://saurabhs.org/advanced-macos-commands): macOS is fortunate to have access to the huge arsenal of standard Unix tools. There are also a good number of macOS-specific command-line utilities that provide unique macOS functionality.
*  [yt-dlp](https://github.com/yt-dlp/yt-dlp): yt-dlp is a youtube-dl fork based on the now inactive youtube-dlc. The main focus of this project is adding new features and patches while also keeping up to date with the original project. 現在抓 twitter 要靠這個了, 先設個tlink變數 `tlink=https://twitter.com/...`, 然後呼叫`yt-dlp $tlink --cookies-from-browser chrome`, 要給檔案名稱: `yt-dlp $tlink --cookies-from-browser chrome -o xx.mp4`
*  [AZ command line repo management](https://learn.microsoft.com/en-us/cli/azure/acr/manifest?view=azure-cli-latest)
*  Telegram bot/API 的部分搬到 [Telethon](https://github.com/LonamiWebs/Telethon), 比較過真的這個方便, telegram-bot-python 改版改廢了. [文件](https://docs.telethon.dev/en/stable/concepts/entities.html).
*  [Telegram Bot 怎麼取得 chat id](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
*  Github Token GG 被更新了怎麼辦, 在linux下面直接改 `/repo/.git/config`, 換掉token就好了. 網路上眾說紛紜, Github自己也不出台個文件.
*  `error: Can not find Rust compiler`, build docker images出現這個, 如果是 python base, 就是python版本太舊了, 被package淘汰了.
*  影片轉音檔: `ffmpeg -i sample.avi -ss 00:03:05 -t 00:00:45.0 -q:a 0 -map a sample.mp3` 或是 `ffmpeg -i sample.avi -ss 00:03:05 -t 00:00:45.0 -q:a 0 -map a sample.m4a`, [詳細討論](https://stackoverflow.com/questions/9913032/how-can-i-extract-audio-from-video-with-ffmpeg)
*  [Server Side Public License](https://szlin.me/2018/11/09/%E6%B7%BA%E8%AB%87-server-side-public-license/) 這篇講這個License講得很清楚. [FerretDB](https://github.com/FerretDB/FerretDB) 這個是因為MongoDB改License之後衍生的 : A truly Open Source MongoDB alternative.
*  [Reddit上面在笑.Net](https://www.reddit.com/r/dotnet/comments/14picbr/comment/jqj3n2w/?utm_source=share&utm_medium=ios_app&utm_name=ioscss&utm_content=1&utm_term=1&context=3)
*  [OpenCat](https://github.com/PetoiCamp/OpenCat). An open source quadruped robot pet framework for developing Boston Dynamics-style four-legged robots that are perfect for STEM, coding & robotics education, IoT robotics applications, AI-enhanced robotics application services, and research. __Boston Dynamics 開源版__
*  [React 還是Vue？我對Web 前端現狀的看法](https://cali.so/blog/react-or-vue-my-take-on-web-dev), 這篇探討React/Vue的比較, 個人是覺得頗中肯, 感覺跟自己經驗差不多, 不知道是否會有反方論證.
*  [New drug to regenerate lost teeth](https://www.kyoto-u.ac.jp/en/research-news/2021-03-31), 這個厲害了, 希望哪天真的能搞定, 成年換齒.
*  [cacao](https://github.com/ryanmcgrath/cacao): Rust bindings for AppKit (macOS) and UIKit (iOS/tvOS). __Experimental, but working!__
*  [工程師生涯](https://www.chunfuchao.com/posts/everything-you-do-is-ultimately-pointless/) 這真的是經歷過的感悟.
* [Zig](https://github.com/ziglang/zig): General-purpose programming language and toolchain for maintaining robust, optimal, and reusable software.
* [Martin](https://github.com/maplibre/martin): Blazing fast and lightweight PostGIS, MBtiles and PMtiles tile server
* [gping](https://github.com/orf/gping): Ping, but with a graph, Base on Rust.
* [eruda](https://github.com/liriliri/eruda): Console for mobile browsers. 為手機網頁前端設計的調試面板。
* [windmill](https://github.com/windmill-labs/windmill#how-to-self-host): Open-source developer platform to turn scripts into workflows and UIs. Open-source alternative to Airplane and Retool. 這個看起來挺炫的, 不知道人多的時候會怎樣. 雖說我不會用 (沒幾隻小貓的話, 用這個只是增加負擔), 但我可以欣賞.
* [python-tools](https://github.com/pxng0lin/python-tools), 列下來是想看看他會更新多久.


----
# ML Topics

## LLM
* [embedchain](https://github.com/embedchain/embedchain): Framework to easily create LLM powered bots over any dataset. python base. Embedchain abstracts the entire process of loading a dataset, chunking it, creating embeddings and then storing in a vector database.
* 大型語言模型（LLM）已經很強了，但還可以更強。通過結合知識圖譜，LLM 有望解決缺乏事實知識、幻覺和可解釋性等諸多問題, 介紹一篇綜述LLM 與知識圖譜聯合相關研究的論文，其中既包含用知識圖譜增強LLM 的研究進展，也有用LLM 增強知識圖譜的研究成果，還有LLM 與知識圖譜協同的最近成果。文中概括性的框架展示非常方便讀者參考。[大型語言模型與知識圖譜協同研究綜述：兩大技術優勢互補](https://www.jiqizhixin.com/articles/2023-07-03-6)
* [LLM Powered Autonomous Agents](https://lilianweng.github.io/posts/2023-06-23-agent/) 這篇可能是個機會, tools看這塊.
* [composer](https://github.com/mosaicml/composer): Train neural networks up to 7x faster. A PyTorch Library for Efficient Neural Network Training. We've implemented more than two dozen speedup methods that can be applied to your training loop in just a few lines of code, or used with our built-in Trainer. We continually integrate the latest state-of-the-art in efficient neural network training.

## TTS
* [Prime Voice AI](https://beta.elevenlabs.io/): 這要錢, 不過免費可用, 聲庫優
*  [voice-library](https://beta.elevenlabs.io/voice-library) Get access to an ever-growing library of high quality AI voices and discover characters that perfectly fit your needs. 有蠻多現成品的.

## Codepilot
* [copilot-analysis](https://github.com/mengjian-github/copilot-analysis), 對codepilot做逆向工程, 完整的過程
* 

## GPT
* [gpt-migrate](https://github.com/0xpayne/gpt-migrate): Easily migrate your codebase from one framework or language to another. Migration is a costly, tedious, and non-trivial problem. __Do not trust__ the current version blindly and please use responsibly. Please also be aware that costs can add up quickly as GPT-Migrate is designed to write (and potentially re-write) the entirety of a codebase.
* [openai_function_call](https://github.com/jxnl/openai_function_call): Helper functions to create openai function calls w/ pydantic. Pydantic is all you need: An OpenAI Function Call Pydantic Integration Module.We try to provides a powerful and efficient approach to output parsing when interacting with OpenAI's Function Call API. One that is framework agnostic and minimizes any dependencies. It leverages the data validation capabilities of the Pydantic library to handle output parsing in a more structured and reliable manner.
* [botsonic](https://writesonic.com/botsonic), 這速度真快.
* [AI and the automation of work](https://www.ben-evans.com/benedictevans/2023/7/2/working-with-ai), 歷史回顧跟預測.
* [prompt-engineering](https://github.com/brexhq/prompt-engineering). Tips and tricks for working with Large Language Models like OpenAI's GPT-4. 2023, May 17.
* 


____

# Coding

## PSQL
* `\x on`, `\x off`, `\x auto`, `\pset format` output formating.
* `select Column1, Column2, count(*) from yourTable group by Column1, Column2 HAVING count(*) > 1`, duplicated records query.
* `\pset format csv`, output format as csv
* query by datetime compare: `SELECT * FROM table WHERE update_date >= '2013-05-03'::date AND update_date < ('2013-05-03'::date + '1 day'::interval);`, update version: `UPDATE mytable SET field1 = '2015-12-31'::timestamp + EXTRACT(HOUR FROM field1) * INTERVAL '1 HOUR' + EXTRACT(MINUTE FROM field1) * INTERVAL '1 MINUTE' + EXTRACT(SECOND FROM field1) * INTERVAL '1 SECOND' `
* `WITH rows AS (...) INSERT INTO dealer (user_id) SELECT id FROM rows RETURNING id;`, 有點繞, 不過就是這樣SELECT, INSERT, RETURN.
* 

## React Chart
* [recharts](https://recharts.org/en-US/examples/CustomContentTreemap) 清爽, [repo](https://github.com/recharts/recharts)
* [react-vis](https://github.com/uber/react-vis), Uber家用的, Data Visualization Components (試了一下, 不好用, 文件少, stackoverflow沒啥討論, 要自己啃source code, 放棄)
* [Apache ECharts](https://echarts.apache.org/), [repo](https://github.com/apache/echarts) : About
Apache ECharts is a powerful, interactive charting and data visualization library for browser, 這個很齊, 啥鬼圖都有


## React
* [tail file to frontend](https://stackoverflow.com/questions/60795932/react-for-displaying-the-log-file-in-real-time-flask-backend)
* [tail file to fronent - package: react-lazylog](https://www.npmjs.com/package/react-lazylog)
* [The Difference Between useState and useRef in React](https://plainenglish.io/blog/the-difference-between-usestate-and-useref-in-react-fa3ccd9aeda5)
* [拖時間] `const delay = ms => new Promise(res => setTimeout(res, ms));`, 然後 `const yourFunction = async () => {  await delay(5000);  console.log("Waited 5s");  await delay(5000);  console.log("Waited an additional 5s");};`, [討論](https://stackoverflow.com/questions/14226803/wait-5-seconds-before-executing-next-line)
* 
