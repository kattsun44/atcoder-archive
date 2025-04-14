s1 = gets.chomp
s2 = gets.chomp

ans = (s1[0] == "." && s2[1] == ".") || (s1[1] == "." && s2[0] == ".") ? "No" : "Yes"

puts ans
