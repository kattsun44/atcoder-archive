n, k, a = gets.chomp.split.map(&:to_i)

index = 0
k.times do |i|
  index = (a - 1 + i) % n
end

puts [*1..n][index]
