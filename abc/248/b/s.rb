a, b, k = gets.chomp.split.map(&:to_i)

count = 0

while a < b
  a = a * k
  count += 1
end

puts count
