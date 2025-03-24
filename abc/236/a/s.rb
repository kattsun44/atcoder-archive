s = gets.chomp
a, b = gets.chomp.split.map(&:to_i)

puts s[...a-1] + s[b-1] + s[a...b-1] + s[a-1] + s[b..]
