s = gets.chomp.split("")

t = s.tally

puts t["v"] + (t["w"] || 0) * 2
