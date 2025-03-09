x = gets.to_i
case x
when .. 39
  puts 40 - x
when 40 .. 69
  puts 70 - x
when 70 .. 89
  puts 90 - x
else
  puts "expert"
end
