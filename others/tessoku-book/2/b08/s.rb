# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_cg
# B08 - Counting Points

# ### 問題文
# 二次元平面上に N 個の点があります．i 個目の点の座標は (Xi,Yi) です．
# 「x 座標が a 以上 c 以下であり，y 座標が b 以上 d 以下であるような点は何個あるか？」
# という形式の質問が Q 個与えられるので，それぞれの質問に答えるプログラムを実装してください．
# なお，入力される値はすべて整数です．

n = gets.to_i
x, y = n.times.map { gets.chomp.split.map(&:to_i) }.transpose
q = gets.to_i
abcd = q.times.map { gets.chomp.split.map(&:to_i) }
