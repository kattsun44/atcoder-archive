n, k = gets.chomp.split(" ").map(&:to_i)
p = n.times.map { gets.chomp.split(" ").map(&:to_i).sum }

# 3 日目終了時点での合計点を昇順にソート
rank = p.sort.reverse

p.each do |pi|
  # k-1 番目 (=k位) の点数以上であれば Yes
  puts rank[k-1] <= pi + 300 ? "Yes" : "No"
end
