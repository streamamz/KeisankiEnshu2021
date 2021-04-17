# UNIX2補足
## SSH/SCP早わかり表
SSH/SCP早わかり表
- SSHログイン(例:dover)

-自宅から
```
ssh s2126??@dover.eps.s.u-tokyo.ac.jp
```
-地惑ネット(559など)から
```
ssh s2126??@dover
```
- SCPファイル転送(例:dover)

-ファイルをdoverの~(ホームディレクトリ)へ送る(自宅から)
```
scp okurimono s2126??@dover.eps.s.u-tokyo.ac.jp:
```
-ファイルをdoverの~(ホームディレクトリ)へ送る(地惑ネットから、以下同じ)
```
scp okurimono s2126??@dover:
```
-ファイルをdoverの~/mydir/へ送る
```
scp okurimono s2126??@dover:mydir/
```
-ファイルをdoverの/home2/sensei/submit/へ送る
```
scp okurimono s2126??@dover:/home2/sensei/submit/
```
-カレントディレクトリ以外にあるファイルをdoverの/home2/sensei/submit/へ送る
```
scp /dir1/dir2/dir3/okurimono s2126??@dover:/home2/sensei/submit/
```
-ファイルをdoverの~(ホームディレクトリ)からとってくる
```
scp s2126??@dover:moraimono .
```
-ファイルをdoverの~/mydir/からとってくる
```
scp s2126??@dover:mydir/moraimono .
```
-ファイルをdoverの/home2/sensei/kadai/からとってくる
```
scp s2126??@dover:/home2/sensei/kadai/moraimono .
```
-ファイルをdoverの/home2/sensei/kadai/からとってきてカレントディレクトリ以外に置く
```
scp s2126??@dover:/home2/sensei/kadai/moraimono /dir1/dir2/dir3/
```
-ディレクトリごとdoverの~(ホームディレクトリ)へ送る
```
scp -r okurimono_dir s2126??@dover:
```
-ディレクトリごとdoverの~(ホームディレクトリ)からとってくる
```
scp -r s2126??@dover:moraimono_dir .
```
- 559のファイルについて

edu,sakura,asanoは/home1/と/home2/が共有されています。
doverは独立しています。（セキュリティのため）
自宅から559で編集したファイルを取りに行くときは、
まずdoverにログインし、scpでsakuraからdoverに取ってきて、
次にdoverからログアウトして、scpでdoverから自宅に取ってきましょう。
逆もまた同じです。やってみてください。
(eduにもSSH/SCPできますが、うまくいかないことがあるので使わないでください。ファイルサーバのsakuraを使いましょう)

# 補足URL
- 公開鍵認証関連

https://qiita.com/kazokmr/items/754169cfa996b24fcbf5

- SSH関連

https://qiita.com/tabu_ichi2/items/446722c15e6b5678ccad

- Vim関連

https://qiita.com/meio/items/08143eacd174ac0f7bd5

