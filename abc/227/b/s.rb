n = gets.to_i
s = gets.chomp.split(" ").map(&:to_i)
ans = n

s.each do |ss|
  right = false
  1.upto(ss) do |a|
    1.upto(ss) do |b|
      right = true if 4 * a * b + 3 * a + 3 * b == ss
    end
  end
  ans -= 1 if right
end

puts ans
