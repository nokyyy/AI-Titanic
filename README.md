# AI-Titanic

http://18.191.177.9/
AI TitanicのサイトIPアドレスです 
 
# Features

PythonのDjangoを使用した、webアプリです。Scikit-learnでTitanic生存/死亡データを学習させて「pkl」ファイルにその学習データを保存しました。
そのデータをDjangoから呼び出して、Django上で打ち込まれた値を元に推定結果をブラウザに表示させるようにしました。
Webアプリのフロントはjsを用いて選択値に対して画像の変更を行うようにプログラムを組んだりしました。
環境はAWSのEC2を用いて、ubuntu20とgunicorn、nginxで負荷分散をしました。

# Requirement
 
* python3
* JavaScriptが動くブラウザ
 
# Installation

インストール必要なものはPipfileがあるので「pip install pipenv」をしていただき、
「pipenv install」でDjangoの動作に必要なバージョンのモジュールを全てinstallしてくれます。
＊ python3.7をinstallしてある環境かPipfileにある「python3.7」の項目をご自身のpythonのバージョンに書き換えてから行ってください。

# Author

nokyyy
 
# License
 
 nokyyy owns copyright on this site nokyyy uploaded
