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


数据集包含 5.5 万首唐诗、26 万首宋诗、2.1 万首宋词和其他古典文集。诗人包括唐宋两朝近 1.4 万古诗人，和两宋时期 1.5 千古词人。数据来源于[https://github.com/chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)。

我已经做成**全简体**文本，并且简化了数据和说明。

**适合构建古文诗词数据集和机器学习** 


## 数据集格式
目前还没有统一的json键值对，之后会一起统一到title和content两个key里面。
### 曹操诗集
```json
[
  {
    "title": "度关山",
    "paragraphs": [
      "天地间，人为贵。",
      "立君牧民，为之轨则。",
      "车辙马迹，经纬四极。",
      "黜陟幽明，黎庶繁息。",
      "于铄贤圣，总统邦域。",
      "封建五爵，井田刑狱。",
      "有燔丹书，无普赦赎。",
      "皋陶甫侯，何有失职？",
      "嗟哉后世，改制易律。",
      "劳民为君，役赋其力。",
      "舜漆食器，畔者十国，",
      "不及唐尧，采椽不斫。",
      "世叹伯夷，欲以厉俗。",
      "侈恶之大，俭为共德。",
      "许由推让，岂有讼曲？",
      "兼爱尚同，疏者为戚。"
    ]
  },
  {
    "title": "短歌行 其一",
    "paragraphs": [
      "对酒当歌，人生几何！譬如朝露，去日苦多。",
      "慨当以慷，忧思难忘。何以解忧？唯有杜康。",
      "青青子衿，悠悠我心。但为君故，沉吟至今。",
      "呦呦鹿鸣，食野之苹。我有嘉宾，鼓瑟吹笙。",
      "明明如月，何时可掇？忧从中来，不可断绝。(明明 一作：佼佼)",
      "越陌度阡，枉用相存。契阔谈䜩，心念旧恩。(谈䜩 一作：谈宴)",
      "月明星稀，乌鹊南飞。绕树三匝，何枝可依？",
      "山不厌高，海不厌深。周公吐哺，天下归心。(海 一作：水)"
    ]
  },
  ...
]
```

### 楚辞
```json
[
  {
    "title": "离骚",
    "section": "离骚",
    "author": "屈原",
    "content": [
      "帝高阳之苗裔兮，朕皇考曰伯庸。",
      "摄提贞于孟陬兮，惟庚寅吾以降。",
      "皇览揆余初度兮，肇锡余以嘉名：",
      "名余曰正则兮，字余曰灵均。",
      "纷吾既有此内美兮，又重之以修能。",
      "扈江离与辟芷兮，纫秋兰以为佩。",
      "汨余若将不及兮，恐年岁之不吾与。",
      "朝搴阰之木兰兮，夕揽洲之宿莽。",
      "日月忽其不淹兮，春与秋其代序。",
    ],
  }
  {
    "title": "云中君",
    "section": "九歌",
    "author": "屈原",
    "content": [
      "浴兰汤兮沐芳，华采衣兮若英",
      "灵连蜷兮既留，烂昭昭兮未央",
      "謇将憺兮寿宫，与日月兮齐光",
      "龙驾兮帝服，聊翱游兮周章",
      "灵皇皇兮既降，猋远举兮云中",
      "览冀洲兮有余，横四海兮焉穷",
      "思夫君兮太息，极劳心兮忡忡"
    ]
  },
  ...
]
```

### 论语
```json
[
  {
    "chapter": "学而篇",
    "paragraphs": [
      "子曰：“学而时习之，不亦说乎？有朋自远方来，不亦乐乎？人不知而不愠，不亦君子乎？”",
      "有子曰：“其为人也孝弟，而好犯上者，鲜矣；不好犯上而好作乱者，未之有也。君子务本，本立而道生。孝弟也者，其为仁之本与！”",
      "子曰：“巧言令色，鲜矣仁！”"
    ]
  },
  {
    "chapter": "为政篇",
    "paragraphs": [
      "子曰：“为政以德，譬如北辰，居其所而众星共之。”",
      "子曰：“《诗》三百，一言以蔽之，曰：‘思无邪’。”",
      "子曰：“道之以政，齐之以刑，民免而无耻。道之以德，齐之以礼，有耻且格。”",
      "子曰：“吾十有五而志于学，三十而立，四十而不惑，五十而知天命，六十而耳顺，七十而从心所欲，不逾矩。”"
    ]
  },
  ...
]
```

### 诗经
```json
[
  {
    "title": "关雎",
    "chapter": "国风",
    "section": "周南",
    "content": [
      "关关雎鸠，在河之洲。窈窕淑女，君子好逑。",
      "参差荇菜，左右流之。窈窕淑女，寤寐求之。",
      "求之不得，寤寐思服。悠哉悠哉，辗转反侧。",
      "参差荇菜，左右采之。窈窕淑女，琴瑟友之。",
      "参差荇菜，左右芼之。窈窕淑女，钟鼓乐之。"
    ]
  },
  {
    "title": "葛覃",
    "chapter": "国风",
    "section": "周南",
    "content": [
      "葛之覃兮，施于中谷，维叶萋萋。黄鸟于飞，集于灌木，其鸣喈喈。",
      "葛之覃兮，施于中谷，维叶莫莫。是刈是濩，为𫄨为绤，服之无斁。",
      "言告师氏，言告言归。薄污我私，薄浣我衣。害浣害否，归宁父母。"
    ]
  },
  ...
]
```














- 全唐诗 [json](./json)
- 全宋诗 [json](./json)
- 全宋词 [ci](./ci)
- 五代·花间集 [wudai/huajianji](./wudai/huajianji)
- 五代·南唐二主词 [wudai/nantan](./wudai/nantang)
- 论语 [lunyu](./lunyu)
- 诗经 [shijing](./shijing)
- 幽梦影 [youmengying](./youmengying)
- 四书五经 [sishuwujing](./sishuwujing)
- 蒙學 [mengxue](./mengxue)
- 纳兰性德诗集 [nalanxingde](./nalanxingde)










## 贡献

本项目目的是借助技术来生成格式化(JSON)数据，让开发者更方便快速的构建诗词类应用程序。身单力薄，欢迎更多人来维护，你可以通过以下方法来参与贡献：

- 直接提交 PR 或者通过 issue 讨论来优化完善此数据库，理论上古诗歌体非宗教类都欢迎加入，部分有争议性的数据需要社区投票讨论决定是否加入。关于诗句的纠错在创建 PR 时请标明出处。更多规范请[参考贡献规范文档](https://github.com/chinese-poetry/chinese-poetry/wiki/%E5%8F%82%E4%B8%8E%E8%B4%A1%E7%8C%AE%E8%A7%84%E8%8C%83)。

- 如果你没有办法直接参与完善的过程，你也可以通过 「[Patreon 周期性赞助](https://www.patreon.com/jackeygao)」的形式来持续帮助并激励我去优化完善此数据库。如果您不喜欢周期性赞助，你也可以通过「[支付宝](https://github.com/jackeyGao/JackeyGao.github.io/blob/master/static/images/alipay.png)」或者「[微信赞赏码](https://github.com/jackeyGao/JackeyGao.github.io/blob/master/static/images/wechat.jpg)」进行一次性赞助(备注留下邮箱)。

## 使用此诗歌数据的机器学习案例

数据来自：[https://github.com/chinese-poetry/chinese-poetry](https://github.com/chinese-poetry/chinese-poetry)

- [pytorch-poetry-gen](https://github.com/justdark/pytorch-poetry-gen)  *a char-RNN based on pytorch*
- [Clover27](https://github.com/Clover27) **/** [ancient-Chinese-poem-generator](https://github.com/Clover27/ancient-Chinese-poem-generator)  *Ancient-Chinese-Poem-Generator*

- [chenyuntc](https://github.com/chenyuntc) **/** [pytorch-book](https://github.com/chenyuntc/pytorch-book/blob/master/chapter9-神经网络写诗(CharRNN)/) *简体唐诗生成(char-RNN)，可生成藏头诗，自定义诗歌意境，前缀等。*
- [PaddlePaddle](https://github.com/PaddlePaddle) **/** [PaddleNLP](https://github.com/PaddlePaddle/PaddleNLP#%E4%BA%A4%E4%BA%92%E5%BC%8Fnotebook%E6%95%99%E7%A8%8B) *基于ERNIE-GEN(Transformer)的深度学习诗词生成，可自行修改逻辑来生成多种诗词风格。*

</details>

## License
Apache
