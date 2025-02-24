x = gets.to_i
yen, ans = 100, 0

while yen < x do
  yen += yen / 100
  ans += 1
end

puts ans
