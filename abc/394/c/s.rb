s = gets.chomp

puts s.gsub(/W+A/) { |w| 'A' + 'C' * (w.length - 1) }
