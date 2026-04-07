# 課題： data.txt を読み込んで，文字の n-gram (n = 1, 2) を
# 表示するプログラムを作成してください．
# すでに書かれている箇所は変更しても構いません．

def n_gram(text, n):
    """テキストを n-gram に分割する関数"""


if __name__ == "__main__":
    """メイン関数"""
    
    unigram = n_gram(text, 1)
    bigram = n_gram(text, 2)

    # 1-gram (unigram, ユニグラム)
    print("あ", unigram["あ"])
    print("い", unigram["い"])
    print("う", unigram["う"])

    # 2-gram (bigram, バイグラム)
    print("あ あ", bigram["あ あ"])
    print("あ い", bigram["あ い"])
    print("あ う", bigram["あ う"])
    print("い あ", bigram["い あ"])
    print("い い", bigram["い い"])
    print("い う", bigram["い う"])
    print("う あ", bigram["う あ"])
    print("う い", bigram["う い"])
    print("う う", bigram["う う"])

