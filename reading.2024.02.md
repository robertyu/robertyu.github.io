## Local LLM

因為這幾天比較有空, 花了點時間弄 local LLM, 有點小小的心得.

千萬不要自己搞, 要跑 inference 就下載 [ollama](https://github.com/ollama/ollama), 裝好之後再去他的 [Library](https://ollama.com/library) 看喜歡哪個, 就pull/run哪個.

手頭是MAC的真心建議先跑上面的方法, 快又無腦, 有空想自己搞再自己搞.

然後 vscode 的 extension 請用 [continue](https://github.com/continuedev/continue), 方便設定 local LLM.

上面就先求有, 有空再求好.

## MISC

#### >>> 密碼管理的另類思考

[這篇](https://nyk.ma/posts/password-store/) 講得很清楚. (作者一堆Emacs的文)

> 外面商業化的產品真的有比較安全嗎?

[pass](https://www.passwordstore.org/) - the standard unix password manager

#### >>> Rust寫的Console檔案管理
[yazi](https://github.com/sxyazi/yazi)

#### >>> 開源的Spotify Client (可惜了, 我想轉Apple了)

[spotube](https://github.com/KRTirtho/spotube), 用[Dart](https://dart.dev/)寫的


#### >>> Incentives and the Cobra Effect

[source](https://boz.com/articles/incentives)

激勵措施和眼鏡蛇效應

當德里處於殖民統治下時，它遭受了大量有毒眼鏡蛇的困擾。為了控制眼鏡蛇的數量，政府對死亡的眼鏡蛇給予賞金。這促使企業家開始飼養眼鏡蛇以收集賞金。當政府發現這一情況時，他們停止了賞金計畫，這意味著所有飼養的眼鏡蛇變得毫無價值，因此被釋放了出去，從而顯著增加了眼鏡蛇的數量。

眼鏡蛇效應是指解決問題的方案無意中使問題變得更糟的情況。而這種情況比你可能想的要常見。類似的故事還包括在河內殺鼠的激勵措施、減少溫室氣體的激勵措施、減少麻醉品生產的激勵措施等等。

我也被一個想法所吸引，那就是聽起來很糟糕的激勵措施實際上可能產生好的結果。我聽一位南非的朋友講述了他們的城鎮合法化了瀕危犀牛的狩獵。這聽起來是一個令人震驚的壞主意。但他們設立了一個非常高的狩獵費用，獵人必須支付，這筆費用將與犀牛所在地的農場主分攤。過去會向偷獵者透露信息以便將犀牛趕出他們土地的農場主，現在會積極地保護犀牛免受偷獵者的侵害。我不知道這個計畫的普及程度如何，但我的朋友建議，至少在最初幾年內，犀牛的數量有了有意義的增加。

還有更多這樣的例子。將動物困於動物園和水族館的不受歡迎做法增加了保護野生動物的熱情。安全注射點減少了非法吸毒的負面外部效應。性教育減少了青少年懷孕的事件。

作為消費者，我們經常陷入這些陷阱。我最喜歡的例子是不限數據的手機套餐。每個人都認為他們想要一個不限數據的計畫。但在激勵層面，運營商的目標是提供剛好足以讓你不轉移運營商的最低服務水平。相反，如果你有一個按數據量付費的計畫，他們的激勵是使你使用數據的體驗盡可能快速和優秀，以便你傾向於使用更多。

我在經營公司的背景下一直在思考這個問題。人們提出看似常識的解決方案，最終卻在下游創造了大量的濫用激勵。例如：

“每個人都應該直接分享反饋，而不是通過經理”導致人們要么為了維護關係而隱瞞有價值的反饋，要么如果他們不能優雅地分享這種反饋就會破壞關係。這是經理接受訓練要做的事情。
“讓我們創建一個詳盡描述每個職位在每個級別所需做什麼的文檔”導致人們只做那些被寫下來的事情，而不是那些在該級別的人理所當然會理解的常識性事物。你試圖使其更加全面，就越被它困住。這些事情之所以含糊，是因為所有有意義的工作都包含大量的自由裁量權，人們往往只有在不確定性中運作得很好時才能證明他們處於某個水平。幾乎可以肯定地說，如果你需要告訴某人具體的工作內容，那麼他們還沒有達到那個水平，除了最初級的角色之外。
“讓我們與其他很多團隊進行跨校準”當這些團隊不深入理解彼此的工作時，會導致對價值創造的最低公分母理解。組織規模或某事獲得的媒體關注成為重要特徵，而實際上，用小團隊創造大影響或做沒有人看到的重要工作可能更應該被強調。

正如Sam Altman在最近的博客文章中寫道：“激勵是超能力; 謹慎設置它們。”


### Noted

* [Bell inequality/Bell's theorem](https://en.wikipedia.org/wiki/Bell%27s_theorem), 真難懂.
* [Spray foam](https://en.wikipedia.org/wiki/Spray_foam) - 噴塗泡沫（在英國稱為expanding foam）是由兩種材料製成的化學產品，異氰酸酯和聚醇樹脂，在混合時會發生反應，噴塗後可膨脹至其液體體積的30-60倍。這種膨脹使其成為一種特殊的包裝材料，能夠適應被包裝產品的形狀，並且幾乎不透氣，具有很高的隔熱價值。
* [Receive Insights on Building Boring Businesses](https://boringcashcow.com/) 
* [Vim 從入門到精通](https://gitlab.com/wsdjeg/vim-galore-zh_cn#vim-%E5%93%B2%E5%AD%A6) 真不錯
* [How I pwned half of America’s fast food chains, simultaneously.](https://mrbruh.com/chattr/), security, 講 [Firebase](https://firebase.google.com/)
* [Introduction to GPU Programming in Chapel](https://chapel-lang.org/blog/posts/intro-to-gpus/)
* [Modeless Vim 在 Hacker News 上面的討論](https://news.ycombinator.com/item?id=39008533), [repo](https://github.com/SebastianMuskalla/ModelessVim), 以下ChatGPT產生: 這篇文章的作者提出了一些理由來支持他的觀點，主要是認為vim的語法突出顯示和其他功能超越了其他基於終端的編輯器，這在概念上完全說得通。然而，作者也表達了一種強烈的不滿感，覺得這樣做有些亵渎原有的精神，就像是在特斯拉車上安裝V8引擎，或者在南瓜派中替換掉南瓜一樣。作者喜愛這種做法能讓更多人更容易地使用VIM，但同時也不喜歡這種做法的具體實現方式。對作者來說，這是一種讚揚和批評並存的情感表達。這表明在技術創新和傳統之間總是存在一種拉鋸，尤其是在軟件開發和使用者體驗的設計上。作者的這番話反映了對於保持原有工具精神與擴大其受眾之間的兩難選擇。
* [How to Build a Progressive Web App (PWA) with React](https://www.loginradius.com/blog/engineering/guest-post/how-to-build-a-progressive-web-app-with-react/)
* [使用 strace 了解程式讀取資料的來源](https://medium.com/fcamels-notes/%E4%BD%BF%E7%94%A8-strace-%E4%BA%86%E8%A7%A3%E7%A8%8B%E5%BC%8F%E8%AE%80%E5%8F%96%E8%B3%87%E6%96%99%E7%9A%84%E4%BE%86%E6%BA%90-aaa17ee2df2b)
* 

## Cook

[rogrammer's guide about how to cook at home (Simplified Chinese only)](https://github.com/Anduin2017/HowToCook), 簡中, 但是很不錯用.

## Rust

#### 演算法大集

[All Algorithms implemented in Rust](https://github.com/TheAlgorithms/Rust)

## Development

* [How CloudKit uses FoundationDB and Record Layer](https://read.engineerscodex.com/p/how-apple-built-icloud-to-store-billions)
* [Python cleanup script for macOS](https://github.com/mac-cleanup/mac-cleanup-py) 感覺有用!
*  [Syntax Error #11: Debugging Python](https://www.syntaxerror.tech/syntax-error-11-debugging-python/)
*  [Figure out who's leaving the company: dump, diff, repeat](https://rachelbythebay.com/w/2024/02/08/ldap/)

#### Remove downloaded tensorflow and pytorch(Hugging face) models] 
```
from transformers import file_utils
print(file_utils.default_cache_path)
```
然後手動砍

## TTS/STT

#### >>(TTS) Bert 系列

* [Bert-VITS2-ext](https://github.com/see2023/Bert-VITS2-ext)
* [Bert-VITS2](https://github.com/fishaudio/Bert-VITS2)


#### >> GPT-SoVITS

[repo](https://github.com/RVC-Boss/GPT-SoVITS)

1 min voice data can also be used to train a good TTS model! (few shot voice cloning)



## ML

#### [MLflow](https://mlflow.org/docs/latest/index.html)

MLflow是一個開源平台,專為協助機器學習從業者和團隊處理機器學習過程中的複雜性而設計. MLflow專注於機器學習項目的全生命週期,確保每個階段都是可管理的,可追蹤的,和可重現的.

> 看起來很美好, 不過 [Hacker News](https://news.ycombinator.com/item?id=33624018) 上面的討論就真的見仁見智了.

#### [annotated_deep_learning_paper_implementations](https://github.com/labmlai/annotated_deep_learning_paper_implementations)

🧑‍🏫 60 Implementations/tutorials of deep learning papers with side-by-side notes 📝; including transformers (original, xl, switch, feedback, vit, ...), optimizers (adam, adabelief, sophia, ...), gans(cyclegan, stylegan2, ...), 🎮 reinforcement learning (ppo, dqn), capsnet, distillation, ... 🧠

> 只能說 佛心來的

## LLM

#### [Machine Learning Compilation for Large Language Models (MLC LLM)](https://github.com/mlc-ai/mlc-llm)

Machine Learning Compilation for Large Language Models (MLC LLM) is a high-performance universal deployment solution that allows native deployment of any large language models with native APIs with compiler acceleration. The mission of this project is to enable everyone to develop, optimize and deploy AI models natively on everyone's devices with ML compilation techniques.

這個主打相容的 devices, AMD GPU, Metal, WebGPU 都吃. [doc](https://llm.mlc.ai/docs/)

#### [PowerInfer](https://github.com/SJTU-IPADS/PowerInfer)

High-speed Large Language Model Serving on PCs with Consumer-grade GPUs.

> Demo 的影片: PowerInfer v.s. llama.cpp on a single RTX 4090(24G) running Falcon(ReLU)-40B-FP16 with a 11x speedup!

這個玩法蠻奇妙的: 

這個分佈顯示，一小部分神經元，被稱為熱神經元，跨不同輸入時持續被激活，而大多數的神經元，稱為冷神經元，則根據特定輸入變化。PowerInfer利用這樣的洞察設計了一個GPU-CPU混合推論引擎：熱激活神經元預先加載到GPU上以快速訪問，而冷激活神經元則在CPU上計算，這樣顯著減少了GPU內存需求和CPU-GPU數據轉移。PowerInfer進一步整合了適應性預測器和神經元感知的稀疏操作符，優化了神經元激活的效率和計算的稀疏性。

評估顯示，在單個NVIDIA RTX 4090 GPU上，PowerInfer實現了平均每秒生成13.20個標記的速率，峰值達到29.08個標記/秒，跨越多種LLMs(包括OPT-175B)，僅比頂級服務器級A100 GPU低18%。這顯著超過了llama.cpp最多11.69倍，同時保持了模型的準確性。

#### [Vanna](https://vanna.ai/docs/)

這個很有趣，有想過想要弄在自己的環境 

只做中介, 這感覺好像是個很不錯的出路. [repo](https://github.com/vanna-ai/vanna?tab=readme-ov-file).

![中介](https://blog.robertiv.org/images/2024022014.png)


#### Stable Code 3B

[Hacker News上面的討論](https://news.ycombinator.com/item?id=39019532)

是有用M2 Max Macbook跑過, 不過卡在pytorch mps, 慢得要死, 弄了半天先放著.

也有試過 [deepseek](https://github.com/deepseek-ai/deepseek-coder), 不過也是超慢, 要找一下原因.

下個目標是[magicoder](https://github.com/ise-uiuc/magicoder), 希望三月份能抽時間搞一下. 不行再認真去找pytorch mps 的問題點在哪.

下面記錄一下用的相關資訊跟遇到mps issue然後去找到的資訊

* [[P] vanilla-llama an hackable plain-pytorch implementation of LLaMA that can be run on any system (if you have enough resources)](https://www.reddit.com/r/MachineLearning/comments/11ozl85/p_vanillallama_an_hackable_plainpytorch/)
* [brittlewis12/stable-code-3b-GGUF](https://huggingface.co/brittlewis12/stable-code-3b-GGUF) -> [What is GGUF and GGML?](https://medium.com/@phillipgimmi/what-is-gguf-and-ggml-e364834d241c) --> [GGML repo](https://github.com/ggerganov/ggml)
* [Compatibility with mps/Mac M1?](https://huggingface.co/stabilityai/stablecode-instruct-alpha-3b/discussions/6)
* [Pytorch inference taking 100% CPU and 10+ minute on M1 Macbook?](https://www.reddit.com/r/pytorch/comments/12z3a1m/pytorch_inference_taking_100_cpu_and_10_minute_on/)
* [MPS BACKEND - Pytorch Doc](https://pytorch.org/docs/stable/notes/mps.html)
* [transformers 的文件](https://github.com/huggingface/transformers/blob/main/README_zh-hant.md)
* [stable-code-3b - modeling_stablelm_epoch.py](https://huggingface.co/stabilityai/stable-code-3b/blob/main/modeling_stablelm_epoch.py)
* [transformers 的文件 - model](https://huggingface.co/docs/transformers/main_classes/model)
* [MPS backend out of memory](https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/9133)
* [Mac setup for PyTorch, fastai, transformers with GPU support in pure pip (no Conda)](https://pnote.eu/notes/pytorch-mac-setup/)

**20240220 UPDATE**

> <span style="background-color:yellow">幹 https://github.com/ollama/ollama 真好用</span>
> 
> <span style="background-color:yellow">我之前自己搞真浪費時間</span>
> 
> <span style="background-color:yellow">建議mac 使用者 下載[這個](https://github.com/ollama/ollama)就對了</span>
> 
> <span style="background-color:yellow">真香</span>

#### >> [ComfyUI](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file)

The most powerful and modular stable diffusion GUI, api and backend with a graph/nodes interface.

看起來很炫, 現在真心沒空玩, 記錄一下.

**20240220 update**

Comfyui 官方又對 Stable Cascade進行了更新，原來需要下載 7 個模型現在開源社區將其整合為了兩個，只需要選擇 C 階段和 B 階段的模型檔案就行。

同時Comfyui官方還放出了多種Stable Cascade玩法的示例工作流，包括文生圖、圖生圖、圖片融合。這次更新之後用合併的模型生成圖片質量和美觀度上都很不錯，我都是直接用的 Midjourney的提示詞。

就是還有個問題，生成的圖片都有偽影，這個比較離譜，非常影響畫面效果。希望過段時間可以修復一下。

[工作流及模型下載](https://comfyanonymous.github.io/ComfyUI_examples/stable_cascade/)

[source](https://twitter.com/op7418/status/1759834924075667679)

#### >> [Web LLM](https://github.com/mlc-ai/web-llm)

WebLLM是一個模組化、可自訂的JavaScript套件，能直接在網頁瀏覽器上帶來語言模型聊天功能，並支援硬體加速。所有操作完全在瀏覽器內完成，不需伺服器支持，利用WebGPU實現加速。這讓我們有機會為每個人建立AI助理，同時在享受GPU加速的優勢時，還能保障隱私。

> 應該試試看能做到什麼程度


#### >> [ml mgie](https://github.com/apple/ml-mgie)

Apple 放出來 open source 的 Guiding Instruction-based Image Editing via Multimodal Large Language Models / 影像編輯.

[demo](https://github.com/tsujuifu/pytorch_mgie?tab=readme-ov-file)

[introduce](https://mllm-ie.github.io/)

基於指令的圖像編輯通過自然語言指令提高了圖像操作的可控性和靈活性，無需繁複描述或區域遮罩。然而，人類指令有時對現有方法來說過於簡略，難以捕捉和遵循。多模態大型語言模型（MLLMs）在跨模態理解和視覺感知回應生成方面顯示出有希望的能力。我們探討了MLLMs如何促進編輯指令，並介紹了MLLM引導的圖像編輯（MGIE）。MGIE學習衍生表達性指令並提供明確指導。編輯模型通過端到端訓練共同捕捉這種視覺想象並進行操作。

注意 版權是 CC-BY-NC 不能商用.


#### >> [transformer-from-scratch](https://github.com/jsbaan/transformer-from-scratch)

兩年前的 repo 了, 找出來的原因是因為有想找個light weight的試試看.

相關的:

* [Implementing a Transformer from Scratch](https://towardsdatascience.com/7-things-you-didnt-know-about-the-transformer-a70d93ced6b2), 2022 Mar
* [transformer](https://github.com/hyunwoongko/transformer): Transformer: PyTorch Implementation of "Attention Is All You Need"
* [Attention Is All You Need](https://arxiv.org/abs/1706.03762) 2017
* [simpletransformers](https://github.com/ThilinaRajapakse/simpletransformers) : Transformers for Information Retrieval, Text Classification, NER, QA, Language Modelling, Language Generation, T5, Multi-Modal, and Conversational AI, **這 repo 活得很好**.
* [Simple Transformer](https://github.com/vkmenon/simple-transformer), 六年前.
* 

#### >> Diffusion-Model 

* [Pytorch implementation of Diffusion Models](https://github.com/dome272/Diffusion-Models-pytorch) 2022
* [Stable Diffusion WebUI Forge](https://github.com/lllyasviel/stable-diffusion-webui-forge) 這個活著, 要玩可以從這裡開始

#### >> OpenAI compatibility

[doc](https://ollama.com/blog/openai-compatibility)

一個殼 介面就OpenAI API format, 後面你想接啥都可以

[Hacker News 的討論](https://news.ycombinator.com/item?id=39307330)

ref:

* [Self-hosting LLMs is actually easy](https://euri.ca/blog/2024-llm-self-hosting-is-easy-now/)


#### >> exllamav2

[repo](https://github.com/turboderp/exllamav2)

A fast inference library for running LLMs locally on modern consumer-class GPUs

看完列表 深深覺得我是不是該買張4090了 

## Open AI

#### >> [openai-translator](https://github.com/openai-translator/openai-translator?tab=readme-ov-file)

基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用 - Browser extension and cross-platform desktop application for translation based on ChatGPT API.

[簡中說明書](https://github.com/openai-translator/openai-translator/blob/main/README-CN.md)

#### >> [gpt-crawler](https://github.com/BuilderIO/gpt-crawler?tab=readme-ov-file)

這個挺貼合需求的, 間單來說就是把整個目標網站爬下來縮成json, 方便塞給OpenGPT用.

#### >> sketch

[repo](https://github.com/approximatelabs/sketch)

簡單來說就一個殼 裡面幫你分析資料 然後往外呼叫 OpenAI API 把兩者串起來.

不過 repo 最後的 commit 在 2024 Jan 19, 我猜應該停了.

## System

#### Nginx 的 log

現在是用 google analytics, 不過現在都更新到這邊了. 

前一陣子有想自己弄HTML, 那時候在找的 log 分析工作, 結果發現這個. [goaccess](https://goaccess.io/get-started), 很符合線下的概念, [repo](https://github.com/allinurl/goaccess).

介紹是說 GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser. 

可以是 console realtime, html generated, 也可以用 docker 跑, 相對來說就不用埋 JS, 這點是我最想要的.

## 想買

* [Vernor Vinge合集](https://www.kobo.com/ww/en/ebook/the-collected-stories-of-vernor-vinge)
* 