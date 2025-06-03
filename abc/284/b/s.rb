t = gets.to_i

t.times do
  _ = gets.to_i
  a = gets.chomp.split.map(&:to_i)
  puts a.count { _1.odd? }
end

