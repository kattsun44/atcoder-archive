require 'set'
n = gets.chomp.to_i
s = Set[]

n.times do
  s << gets
end

pp s.size
