# Text Frontend

中文TTS相关资源过于零散，不仅没有大规模数据集，连个正常的能精准做CN TTS的都很少，这一块可能连越南都不如。本仓库主要将TTS的前端部分单独整理成一个仓库，这样对于TTS的引擎，就不需要考虑太多前端处理的东西，你拿到拼音和韵律之后转一下token就可以合成了。

当前的版本主要考虑三个问题：

- 韵律Prosody预测；
- 多音字Polyphone预测；
- 拼音预测；

那么基本上TTS的前端问题就差不多解决了。

目前的实现，主要是基于PaddleSpeech，将其的操作结合一些个人经验，变成一个简单的统一化的函数。当中用到的模型可以基于ONNXRuntime推理，部署也更简单方便。


# 安装

```
python setup.py build develop
```

# 使用

tbd