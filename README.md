# Remote procedure call

## 使い方
サーバ起動
``` bash
python server.py
```

クライアントからリクエスト
``` bash
node dist/client/src/client.js <関数名> <パラメータ>
```

使用できる関数
- floor(double x)
- nroot(int n, int x)
- reverse(string s)
- validAnagram(string str1, string str2)
- sort(string[] strArr)