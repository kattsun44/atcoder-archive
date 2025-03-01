# atcoder-archive

[AtCoder：競技プログラミングコンテストを開催する国内最大のサイト](https://atcoder.jp/home)

## 環境構築

### 初期設定

[online-judge-tools/oj](https://github.com/online-judge-tools/oj) をインストールする

```shell
python3 -m venv oj
source oj/bin/activate
python3 -m pip install online-judge-tools
```

`oj login` を実行
```shell
oj login https://atcoder.jp/
```

### 都度実行

ディレクトリを作成し移動
```shell
mkdir abc/abcXXX
cd abc/abcXXX
```

難易度別の回答ディレクトリ&ファイルを作成 (ref: [Alias for AtCoder - Kattsun.dev](https://kattsun.dev/posts/alias-for-atcoder/))

```shell
# Ruby の場合
mkdir {a..h}; touch a/s.rb; echo {b..h} | xargs -n 1 cp -v a/s.rb
```

テストファイルをダウンロード
```shell
cd a
oj d https://atcoder.jp/contests/abcXXX/tasks/abcXXX_a
```

テスト実行
```shell
# Ruby の場合
oj t -c "ruby s.rb" -d test
```

提出
```shell
# Ruby の場合
oj s s.rb
```
