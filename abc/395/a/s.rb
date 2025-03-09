n = gets.to_i
a = gets.chomp.split.map(&:to_i)

puts a.sort == a && a.uniq.size == a.size ? "Yes" : "No"
