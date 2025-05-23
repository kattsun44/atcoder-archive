S = gets.chomp.split("")

index = S.rindex("a")
puts index ? index + 1 : -1
