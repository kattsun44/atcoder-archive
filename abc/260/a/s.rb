s = gets.chomp.split("")

puts s.tally.select { _2 == 1 }.keys[0] || -1
