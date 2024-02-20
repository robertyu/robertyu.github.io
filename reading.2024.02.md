## MISC

#### 密碼管理的另類思考

[這篇](https://nyk.ma/posts/password-store/) 講得很清楚. (作者一堆Emacs的文)

> 外面商業化的產品真的有比較安全嗎?

[pass](https://www.passwordstore.org/) - the standard unix password manager

#### Rust寫的Console檔案管理
[yazi](https://github.com/sxyazi/yazi)

#### 開源的Spotify Client (可惜了, 我想轉Apple了)

[spotube](https://github.com/KRTirtho/spotube), 用[Dart](https://dart.dev/)寫的

### Noted

* [Bell inequality/Bell's theorem](https://en.wikipedia.org/wiki/Bell%27s_theorem), 真難懂.
* [Spray foam](https://en.wikipedia.org/wiki/Spray_foam) - 噴塗泡沫（在英國稱為expanding foam）是由兩種材料製成的化學產品，異氰酸酯和聚醇樹脂，在混合時會發生反應，噴塗後可膨脹至其液體體積的30-60倍。這種膨脹使其成為一種特殊的包裝材料，能夠適應被包裝產品的形狀，並且幾乎不透氣，具有很高的隔熱價值。

## Cook

[rogrammer's guide about how to cook at home (Simplified Chinese only)](https://github.com/Anduin2017/HowToCook), 簡中, 但是很不錯用.

## Rust

#### 演算法大集

[All Algorithms implemented in Rust](https://github.com/TheAlgorithms/Rust)

## Development

* [How CloudKit uses FoundationDB and Record Layer](https://read.engineerscodex.com/p/how-apple-built-icloud-to-store-billions)
* [Python cleanup script for macOS](https://github.com/mac-cleanup/mac-cleanup-py) 感覺有用!
*  [Syntax Error #11: Debugging Python](https://www.syntaxerror.tech/syntax-error-11-debugging-python/)

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
* 

#### [ComfyUI](https://github.com/comfyanonymous/ComfyUI?tab=readme-ov-file)

The most powerful and modular stable diffusion GUI, api and backend with a graph/nodes interface.

看起來很炫, 現在真心沒空玩, 記錄一下.

#### [Web LLM](https://github.com/mlc-ai/web-llm)

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

## Open AI

#### >> [openai-translator](https://github.com/openai-translator/openai-translator?tab=readme-ov-file)

基于 ChatGPT API 的划词翻译浏览器插件和跨平台桌面端应用 - Browser extension and cross-platform desktop application for translation based on ChatGPT API.

[簡中說明書](https://github.com/openai-translator/openai-translator/blob/main/README-CN.md)

#### >> [gpt-crawler](https://github.com/BuilderIO/gpt-crawler?tab=readme-ov-file)

這個挺貼合需求的, 間單來說就是把整個目標網站爬下來縮成json, 方便塞給OpenGPT用.

## System

#### Nginx 的 log

現在是用 google analytics, 不過現在都更新到這邊了. 

前一陣子有想自己弄HTML, 那時候在找的 log 分析工作, 結果發現這個. [goaccess](https://goaccess.io/get-started), 很符合線下的概念, [repo](https://github.com/allinurl/goaccess).

介紹是說 GoAccess is a real-time web log analyzer and interactive viewer that runs in a terminal in *nix systems or through your browser. 

可以是 console realtime, html generated, 也可以用 docker 跑, 相對來說就不用埋 JS, 這點是我最想要的.

