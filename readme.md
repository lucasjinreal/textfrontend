# Text Frontend

中文 TTS 相关资源过于零散，不仅没有大规模数据集，连个正常的能精准做 CN TTS 的都很少，这一块可能连越南都不如。本仓库主要将 TTS 的前端部分单独整理成一个仓库，这样对于 TTS 的引擎，就不需要考虑太多前端处理的东西，你拿到拼音和韵律之后转一下 token 就可以合成了。

> WIP: work still in progress.

当前的版本主要考虑三个问题：

- 韵律 Prosody 预测；
- 多音字 Polyphone 预测；
- 拼音预测；

那么基本上 TTS 的前端问题就差不多解决了。

目前的实现，主要是基于 PaddleSpeech，将其的操作结合一些个人经验，变成一个简单的统一化的函数。当中用到的模型可以基于 ONNXRuntime 推理，部署也更简单方便。

# 安装

note: 我们不需要paddle

```
pip install -r requirements.txt
python setup.py build develop
```

# 使用

```python
from textfrontend.zh_frontend import FrontEnd

fe = FrontEnd()
fe.get_phonemes('从前有座山，山里有座庙，庙里有个老和尚')
```


# QA

1. `  from pypinyin_dict.phrase_pinyin_data import large_pinyin
OverflowError: line number table is too long`

大概是python3.10的问题