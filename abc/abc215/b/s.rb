n = gets.chomp.to_i
ans = 0

while 2 ** ans <= n
  ans += 1
end

puts [ans - 1, 0].max
