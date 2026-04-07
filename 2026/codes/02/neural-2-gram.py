# "あ", "い", "う" のいずれかを入力とし、
# 次元数 3 の確率値を出力するニューラルネットワークを構築してください
# ニューラルネットワークの構成，使用する Python モジュールは問いません．
# 学習は不要で，重みは適当に（例えば乱数値に）設定してください．
# 例：入力 "あ" に対して，出力 [0.7, 0.2, 0.1] を得る．
# すでに書かれている箇所は変更しても構いません．

input_vec = {
    "あ": [1, 0, 0],
    "い": [0, 1, 0],
    "う": [0, 0, 1]
}

def neural_network(input_char):
    """ニューラルネットワークの関数"""

    return output_vec # 3次元の確率値を返す


if __name__ == "__main__":
    """メイン関数"""
    
    output_a = neural_network("あ")
    output_i = neural_network("い")
    output_u = neural_network("う")

    print("入力: あ, 出力:", output_a) # 全要素は非負の値で，合計は 1 でなければならない
    print("入力: い, 出力:", output_i)
    print("入力: う, 出力:", output_u)