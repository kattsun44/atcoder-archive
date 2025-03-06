a, b = gets.chomp.split.map(&:to_i)

ratio = 1 / Math.sqrt(a ** 2 + b ** 2)

puts [a, b].map { _1 * ratio }.join(" ")
