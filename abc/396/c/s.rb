n, m = gets.chomp.split.map(&:to_i)
b = gets.chomp.split.map(&:to_i).sort.reverse
w = gets.chomp.split.map(&:to_i).select { _1 > 0}.sort.reverse

# 0以上のbを足す
ans = b.select { _1 > 0 }.sum

# 0以上のbの数まで1以上のwを足す
count = b.count { _1 >= 0 }
ans += w[0...count].sum

b = b[count..]
w = w[count..]

[b&.size.to_i, w&.size.to_i].min.times do |i|
  diff = b[i] + w[i]
  if diff > 0
    ans += diff
  else
    break
  end
end

puts ans
