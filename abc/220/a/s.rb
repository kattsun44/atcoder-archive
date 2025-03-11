a, b, c = gets.chomp.split.map(&:to_i)

ans = -1

while c <= b
  if a <= c
    ans = c
    break
  end
  c *= 2
end

puts ans
