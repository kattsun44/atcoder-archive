q = gets.to_i


cards = [0] * 100
q.times do
  type, x = gets.chomp.split.map(&:to_i)

  if type == 1
    cards << x
  else
    puts cards.pop
  end
end
