a, b, c = gets.chomp.split("")

puts [a,b,c].join.to_i + [b,c,a].join.to_i + [c,a,b].join.to_i
