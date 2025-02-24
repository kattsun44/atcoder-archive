# 要素を降順にする
n = gets.chomp.split("").sort.reverse
len = n.size
ans = 0

# 2^(len-1) 通りの部分集合を生成
(1 << len-1).times do |bit|
  s1, s2 = [], []
  len.times do |i|
    # bit の i 番目が 1 であれば、i 番目の要素を部分集合 s1 に含める
    s1 << n[i] if bit[i] == 1
    # bit の i 番目が 0 であれば、i 番目の要素を部分集合 s2 に含める
    s2 << n[i] if bit[i] == 0
  end
  ans = [s1.join.to_i * s2.join.to_i, ans].max
end

puts ans
