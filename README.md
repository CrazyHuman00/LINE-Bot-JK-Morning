# 朝起こしてくれるLINE-Bot
朝JKがLINEで起こしてくれるLINEBotです。
pythonとGithubActionsで作成しました。

## 使用
### gitのクローン方法
git環境がある方はこちらのコマンドを入力してください
```bash:
git clone https://github.com/CrazyHuman00/LINE-Bot-JK-Morning
```

### pythonのバージョン確認
以下のコマンドでPythonのバージョンを確認できます。
```bash:
python --version
```

### info.jsonの記入
使用する際は同じディレクトリ内にinfo.jsonを用意してください。
LINEdevelopersで作成するのでLINEのアカウントが必要です。
```json:
{
    "CHANNEL_ACCESS_TOKEN": "YOUR_CHANNEL_ACCESS_TOKEN",
    "USER_ID": "YOUR_USER_ID"
}

```

