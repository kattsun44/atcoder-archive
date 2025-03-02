n = gets.to_i
t = gets.chomp.split("")

x, y, turn = 0, 0, 0

t.each do |tt|
  if tt == "R"
    turn += 1
  else
    x += 1 if turn % 4 == 0
    y -= 1 if turn % 4 == 1
    x -= 1 if turn % 4 == 2
    y += 1 if turn % 4 == 3
  end
end

puts [x, y].join(" ")
