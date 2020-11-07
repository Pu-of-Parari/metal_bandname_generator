# band name generator

モダンメタル風のバンド名を自動で生成するツールです。

## SETTING
Python >= 3

## USAGE
以下を実行してください。
`python generate.py`


以下が出力されるのでモードを選んでください。
```
mode:
1: generate the words you want to use and the num of words you set(e.g. bring 4)
2: set the acronym you want to use(e.g. BMTH)
3: set hte word count and generate a Markov chain model(e.g. 4)
mode? >>
```

モード別の概要は以下です。
```
1: 使いたい単語と生成したい単語数を指定してバンド名生成を行います。(例：bring 4)
2: 生成したいバンド名の頭文字を指定してバンド名生成を行います。(例：BMTH)
3: 生成したい単語数を指定しマルコフ連鎖モデルを使用してバンド名生成を行います。
```
モードごとに聞かれる値を設定することで10個のバンド名を自動で生成します。


## 実行デモ
### モード1: 使いたい単語と単語数を指定

```
mode:
1: generate the words you want to use and the num of words you set(e.g. bring 4)
2: set the acronym you want to use(e.g. BMTH)
3: set hte word count and generate a Markov chain model(e.g. 4)
mode? >> 1
seed? >> Bring
word num? >> 4
--------------------------
Bring Funeral Against You
Bring Deftones Airlines Kids
Hesitation Dire Bring Psyopus
Lions Barren Bring Dismemberment
Rorschach Bring Hand Bloodshed
Bring Pereo Hound This
Take Remains Bring Skycamefalling
Bring Sick Bunchofuckingoofs Annisokay
Rock Bring Fall Drivers
Devil Bring s Sacred
```

### モード2: 生成したいバンド名の頭文字を指定

```
mode:
1: generate the words you want to use and the num of words you set(e.g. bring 4)
2: set the acronym you want to use(e.g. BMTH)
3: set hte word count and generate a Markov chain model(e.g. 4)
mode? >> 2
initial? >> BMTH
--------------------------
Bullet Minutemen Thee Hoax
Burst Meat Treason Hand
Burden Minus Trooper Hollow
Blitzkrieg Mantis Treatment Horse
Botch Me Troy Hat
Beasts Mad Tattoo Hacktivist
Break Moxy They Headpins
Brat Murphy Thrice Hearts
Blue Mountain They Houses
Brides Macabre Tigers Hotel
```

### モード3: 生成したい単語数のみを指定しマルコフ連鎖モデルで生成

```
mode:
1: generate the words you want to use and the num of words you set(e.g. bring 4)
2: set the acronym you want to use(e.g. BMTH)
3: set hte word count and generate a Markov chain model(e.g. 4)
mode? >> 3
word num? >> 4
--------------------------
diamond the unseen mastedon
bulldozer botch grand funk
discharge atomkraft gwen stacy
settle the head wound
stones mindrage story of
inside evergreen terrace antidemon
surgery kix we do
veni domine the undead
easy action the out
seed blood brothers deep
```

## ADVANCE
`./band_list`内のジャンル別ファイルを指定することでそのジャンルのバンド名で出現する単語のみを使用して生成することも可能です。
