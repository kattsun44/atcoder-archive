n = gets.chomp.split("").sort.reverse
len = n.size

ans = 0
(1 << len-1).times do |bit|
  s1, s2 = [], []
  len.times do |i|
    s1 << n[i] if bit[i] == 1
    s2 << n[i] if bit[i] == 0
  end
  ans = [s1.join.to_i * s2.join.to_i, ans].max
end

puts ans
