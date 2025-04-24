s = gets.chomp.split("")

puts s.permutation(3).map(&:join).uniq.size
