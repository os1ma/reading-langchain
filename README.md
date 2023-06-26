# reading-langchain

勉強会「[LangChain ソースコードリーディング／テーマ：OpenAI Chat API を「ちゃんと」使う](https://studyco.connpass.com/event/286514/)」で使用したソースコード。

## 依存関係

- Python
- Poetry

バージョンは [.tool-verisons](.tool-versions) に書かれています。

> **Note**
> .tool-verisons は [asdf](https://asdf-vm.com/) の設定ファイルです。

## 実行手順

Python のパッケージは Poetry で管理しています。
以下のコマンドでインストールしてください。

```console
poetry install
```

各サンプルコードは以下のコマンドで実行できます。

```console
poetry run python reading_langchain/<ファイル名>
```
