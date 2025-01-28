s = gets.chomp
ss = []

s.length.times do |i|
  ss << s[-i..] + s[...-i]
end

puts ss.sort.first
puts ss.sort.last
