n, q = gets.chomp.split(" ").map(&:to_i)
a = gets.chomp.split(" ").map(&:to_i)
xk = q.times.map { gets.chomp.split(" ").map(&:to_i) }

# キーがAの要素、バリューが出現位置の配列であるハッシュを作る
h = a.map { [_1, []] }.to_h

# 数列Aを走査する
a.each_with_index do |aa, i|
  h[aa] << i+1
end

# x を順に見ていく
xk.each do |x, k|
  # xi があるか確認
  if h[x].nil?
    puts -1
  elsif h[x][k-1].nil?
  # ki 回目の xi が登場する出現位置を見る
    puts -1
  else
    puts h[x][k-1]
  end
end
