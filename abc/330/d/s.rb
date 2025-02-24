n = gets.to_i
s = n.times.map { gets.chomp.split("") }

ans = 0

# 行・列ごとの o の数を数える
row_counts, col_counts = [], []
n.times do |i|
  row_counts << s[i].count { _1 == "o" }
  col_counts << s.count { _1[i] == "o" }
end

s.each_with_index do |s_row, i|
  s_row.each_with_index do |cell, j|
    next if cell == "x" # L字の付け根が x になることはないためスキップ

    # 自分自身を除いた行列ごとのカウント数をかけたものが条件を満たす三つ組の数
    ans += (row_counts[i] - 1) * (col_counts[j] - 1)
  end
end

puts ans
