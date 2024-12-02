# 信号処理実習

信号処理におけるプログラミングの実習のためのリポジトリです．実行環境の構築方法について解説しています．

## 環境構築

### uvのインストール
まず[uvのリポジトリ](https://github.com/astral-sh/uv)にアクセスし，uvのインストールをしてください．
windowsの場合，
```powershell
Powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex
```
というのをPowershellで実行すればよいです．
実行すると，`uv.exe, uvx.exe`という二つの実行ファイルが`C:\Users\<username>\.local\bin`に作られます．
(この`<username>`は個別のユーザーごとに異なります)

このディレクトリを環境変数`Path`に追加します．
```powershell
$env:Path = "C:\Users\<username>\.local\bin;$env:Path"
```

`uv --version`と実行してバージョン情報が表示されたら，無事インストールできています．

### uvを用いた環境構築
プロジェクトのディレクトリを作成し，ディレクトリ内にpyproject.tomlをコピーします．`uv sync`とすれば，pyproject.tomlを参照して，必要なライブラリをインストールしてくれます．
実行後にディレクトリの中には`.venv`というディレクトリと`uv.lock`というファイルが作成されます．前者は仮想環境に関するもので，後者は最終的にインストールされたライブラリに関する情報です．

### uvで作成した仮想環境へのアクセス
`.\.venv\Scripts\activate`を実行することで仮想環境にアクセスできます．Powershellで実行ポリシーによって実行できないというエラーが出ることがあります．
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
と入力し実行ポリシーを変更すれば実行できます．これは一時的なものなので，シェルを終了すると再度実行できなくなります．
仮想環境にアクセスすると，先頭に`(exercise)`と付きます．
これは`pyproject.toml`にて指定したプロジェクトの名前です．
`deactivate`と入力すれば，仮想環境から出ることができます．

もし他の名前の仮想環境が欲しければ，プロジェクトのディレクトリで，`uv venv <virtual_env_name>`と入力してください．
直下に`.venv`と同じように`<virtual_env_name>`のフォルダができます．その中の`<virtual_env_name>\Scripts\activate`を実行すれば，`<virtual_env_name>`という名前の仮想環境に入れます．

### gitのインストール
windowsユーザは[git for windows]を利用することをお勧めします．
[gitのオフィシャルページ](https://git-scm.com)にアクセスし，
Portable版のインストーラをダウンロードし，実行すると`PortableGit`というフォルダが作られます．
`PortableGit\bin`を`Path`に追加します．先ほど同様に
```powershell
$env:Path = "<path to PortableGit>\PortableGit\bin;$env:Path"
```
とすればよいです．あくまでこれは一時的なものなので，シェルを終了すると再入力する必要があります．

`git --version`と入力してバージョン情報が得られたなら成功です．


### gitによるローカルリポジトリの整備
プロジェクトのファイルで`git init`と入力してください．`.git`という隠しフォルダが作られます．
`git status`とすると，コミットできるファイルがリストされます．ここでは`pyproject.toml`と`uv.lock`が入っていると思います．
これらのファイルを`git add <ファイル名>`でステージングしてください．ステージングできたら`git status`によって状態を確認すると緑色でステージングされていることが示されます．
`git commit -m "<コミットメッセージ>"`によってコミットをしてください．これによって履歴を記録できます．`git status`で確認するとコミットできるものはないと言われます．
`git log`を見ると履歴を確認できます．先ほど記録した履歴が確認できます．

### GitHubにてリモートリポジトリを作成
アカウント登録をして，ログインしてください．
新しいリポジトリを作ってください．
設定よりSSH and GPG keysに行き，SSH keysを設定します．
`ssh-keygen`によって公開鍵と秘密鍵のペアを作成します．
このうち公開鍵のほうをコピペして，New SSH keysより登録します．
`ssh -T git@github.com`でauthnticateされたらOKです．

### GitHubにプッシュ
プロジェクトのディレクトリにて
`git remote add origin <URL>`
`git push -u origin master`
と入力してください．これでリモートリポジトリにローカルリポジトリの情報を記録できました．
GitHubのページにアクセスすると，コミットした情報が見られるようになっています．これでいつでもあなたはGitHubより開発途中のコードを履歴付きで回収できるようになりました．

## コードの実行方法
仮想環境の外からは，`uv run python hoge.py`という風に打てば，hoge.pyを実行することが出来ます．
仮想環境に入れば，普通に`python hoge.py`で実行できます．

前述の環境構築を行ったうえで，
```
uv run python hello.py
```
と実行してグラフが表示されるのであれば，環境は正しく構築できています．

## コードの静的解析（リント）
Ruffという静的解析ツール（リンター）を導入しています．`uv run ruff check`または`uvx ruff check`と打てば，静的解析を実行します．
問題を見つけてくれたら教えてくれますし，`--fix`というオプションを`check`の後につけて実行すれば勝手に直してくれることもあります．
問題が無ければ，`All checks passed!`と出力されます．
書いたコードを実際に実行する前に静的解析を行えば，バグで困る確率を下げられます．書いたコードはチェックしてから実行するといいと思います．