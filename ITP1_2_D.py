# 長方形の中に円が含まれるかを判定するプログラムを作成してください。
# 次のように、長方形は左下の頂点を原点とし、右上の頂点の座標 (W,H)が与えられます。
# また、円はその中心の座標 (x,y)と半径rで与えられます。

W,H,x,y,r = map(int,input().split())

# 座標(x,y)が、0に半径rを足した座標から、HやWから半径rを引いた範囲内に収まっていれば
# 長方形の中に円が収まっていると言える
if 0+r <= x <= H-r and 0+r <= y <=H-r:
    print('Yes')
# そうでなければ円は長方形からはみ出ている
else:
    print('No')