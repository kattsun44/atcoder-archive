n, k = gets.chomp.split(" ").map(&:to_i)
p = n.times.map { gets.chomp.split(" ").map(&:to_i).sum }

p.each do |pi|
  rank = p.count { _1 > pi + 300 } + 1
  puts rank <= k ? "Yes" : "No"
end
