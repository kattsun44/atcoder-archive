a,b=gets.chomp.split(" ").map(&:to_i)

if a >= 9 || b >= 9
  print(":(\n")
else
  print("Yay!\n")
end