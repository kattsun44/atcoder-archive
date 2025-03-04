n = gets.to_i
a = gets.chomp.split.map(&:to_i)
ans = 0

a.sort.each do |i|
  ans += 1 if ans == i
end

puts ans
