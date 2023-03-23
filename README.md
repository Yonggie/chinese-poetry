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
  
]
```
### 唐诗1
```json
[
  {
    "author": "刘禹锡",
    "title": "蜀先主庙",
    "content": [
      "天地英雄气，千秋尚凛然。",
      "势分三足鼎，业复五铢钱。",
      "得相能开国，生儿不象贤。",
      "凄凉蜀故伎，来舞魏宫前。"
    ],
    "prologue": "此诗歌颂了开国之君刘备的历史功绩。天地英雄的气派，千秋还存在的凛然正气。在三足鼎立的形势下，从事兴复汉室。得到诸葛丞相，便开创了蜀国；生个儿子刘禅，却不像先贤。令人感到凄凉的是，蜀国原来的歌伎，竟来到洛阳的魏宫起舞。"
  },
  {
    "author": "王建",
    "title": "新嫁娘",
    "content": [
      "三日入厨下，洗手作羹汤。",
      "未谙姑食性，先遣小姑尝。"
    ],
    "prologue": "此诗朴素生动地刻划了封建社会媳妇对婆婆，特别是新嫁娘初到婆婆家，那种畏惧谨慎的心理状态。　　按照习俗，新嫁娘婚后的第三天要下厨做菜。　　第三天下厨房，洗手后煮羹汤，不熟悉婆婆的口味，先请小姑尝试。"
  }
]
```
### 幽梦影
```json
[
  {
    "content": "读经宜冬，其神专也；读史宜夏，其时久也；读诸子宜秋，其致别也；读诸集宜春，其机物也。",
    "comment": [
      "曹秋岳曰：可想见其南面百城时。",
      "庞笔奴曰：读《幽梦影》则春、夏、秋、冬，无时不宜。"
    ]
  },
  {
    "content": "经传宜独坐读，史鉴宜与友共读。",
    "comment": [
      "孙恺似曰：深得此中真趣，固难为不知者道。",
      "王景州曰：如无好友，即红友亦可。"
    ]
  }
]
```
### 元曲
其中中文的``“”``符号被统一替换成了``”``符号。
```json
[
  {
    "author": "关汉卿",
    "content": [
      "半世为人，不曾教大人心困。",
      "虽是搽胭粉，只争不裹头巾，将那等不做人的婆娘恨。"
    ],
    "title": "诈妮子调风月・仙吕/点绛唇"
  },
  {
    "author": "关汉卿",
    "content": [
      "男儿人若不依本分，一个抢白是非两家分。",
      "壮鼻凹硬如石铁，教满耳根都做了烧云。",
      "普天下汉子尽教都先有意，牢把定自己休不成人。",
      "虽然两家无意，便待一面成亲，不分晓便似包着一肚皮干牛粪。",
      "知人无意，及早抽身。"
    ],
    "title": "诈妮子调风月・混江龙"
  },
]
```

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
