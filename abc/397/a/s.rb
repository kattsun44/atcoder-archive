x = gets.to_f

case
when x >= 38.0
  puts 1
when x >= 37.5 && x < 38.0
  puts 2
else
  puts 3
end
