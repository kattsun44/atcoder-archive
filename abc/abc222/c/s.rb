n, m = gets.chomp.split(" ").map(&:to_i)
a = (n * 2).times.with_index.map {|_, i| [0, i+1, gets.chomp]}

# m ラウンド行う
m.times do |i|
  n.times do |k|
    # i - 1 ラウンド終了時点の 2k 位と 2k + 1 位で試合をする
    x, y = a[2*k], a[2*k+1]
    xx, yy = x[2][i], y[2][i] # じゃんけんの手
    next if xx == yy # あいこの場合

    # 勝った方に1を足す
    if xx == "G"
      yy == "C" ? x[0] += 1 : y[0] += 1
    elsif xx == "C"
      yy == "P" ? x[0] += 1 : y[0] += 1
    elsif xx == "P"
      yy == "G" ? x[0] += 1 : y[0] += 1
    end
  end
  # 勝数順にソート
  a.sort_by! do |v1, v2|
    [-v1, v2]
  end
end

a.each do |aa|
  puts aa[1]
end
