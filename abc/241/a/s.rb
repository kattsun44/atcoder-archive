a = gets.chomp.split.map(&:to_i)
ans = 0

3.times do
  ans = a[ans]
end

puts ans
