<p align="center">
  <a href="https://github.com/chinese-poetry/chinese-poetry">
      <img src="https://avatars3.githubusercontent.com/u/30764933?s=200&v=4" alt="chinese-poetry">
  </a>
</p>

<h2 align="center">Chinse-Poetry: 中文诗歌古典文集数据集</h2>

本项目Fork于：[https://github.com/chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)。

本项目主要贡献点：
- 变更全简体；
- 处理类似``「」``等杂字符；
- 整理统一目录，修改汉字，方便理解和程序统一处理；
- 统一键值对，方便构建机器学习数据集


数据集包含 107891首唐诗、275581首宋诗和其他古典文集。诗人包括唐宋两朝近 1.4 万古诗人，和两宋时期 1.5 千古词人。

我已经做成**全简体**文本，并且简化了数据和说明。

**适合构建古文诗词数据集和机器学习** 

## 使用
带上``depth=1``会快很多，不然大部分是git的commit pack文件占用时间，慢。
```
git clone xxx --depth=1
```

## 数据集格式
统一的json键值对，一般是在``title``,``content``两个键里面，部分带``author``、``section``等其他信息。

其中在``元曲``的文本中，中文的``“”``符号被统一替换成了``”``符号。

## 规模
目前粗略估计(未去重)
数据集总规模：``396242个（诗/词/文）``
唐诗：``107891个``
宋词：``275581个``
千家诗：``226个``

## 赞助

本项目目的构建方便于机器学习使用的中文诗歌数据集，基于他人项目，站在巨人肩膀上进行工作。欢迎更多人来维护，你可以通过以下方法来参与贡献：

- 直接提交 PR 或者通过 issue 讨论。

- 也可以通过「支付宝」或者「微信赞赏码」进行一次性赞助(备注留下邮箱)。
<p align="center">
  <a href="https://github.com/chinese-poetry/chinese-poetry">
      <img src="./images/wechatpay.jpg" alt="chinese-poetry" height=200px>
      <img src="./images/alipay.jpg" alt="chinese-poetry" height=200px>
  </a>
</p>

## 使用此诗歌数据的机器学习案例

数据来自：[https://github.com/chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)

- [pytorch-poetry-gen](https://github.com/justdark/pytorch-poetry-gen)  *a char-RNN based on pytorch*
- [Clover27](https://github.com/Clover27) **/** [ancient-Chinese-poem-generator](https://github.com/Clover27/ancient-Chinese-poem-generator)  *Ancient-Chinese-Poem-Generator*

- [chenyuntc](https://github.com/chenyuntc) **/** [pytorch-book](https://github.com/chenyuntc/pytorch-book/blob/master/chapter9-神经网络写诗(CharRNN)/) *简体唐诗生成(char-RNN)，可生成藏头诗，自定义诗歌意境，前缀等。*
- [PaddlePaddle](https://github.com/PaddlePaddle) **/** [PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP#%E4%BA%A4%E4%BA%92%E5%BC%8Fnotebook%E6%95%99%E7%A8%8B) *基于ERNIE-GEN(Transformer)的深度学习诗词生成，可自行修改逻辑来生成多种诗词风格。*

</details>

## License
Apache
