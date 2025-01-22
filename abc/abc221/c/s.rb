n = gets.chomp.split("").sort { |a, b| b <=> a }

a, b = n[0...n.length/2], n[n.length/2..n.length]
c, d = n[0..n.length/2], n[n.length/2+1..n.length]
e, f = n.select.with_index { |_, i| i.even? }, n.select.with_index { |_, i| i.odd? }
g = n.select.with_index { |_, i| i.even? }[0...-1]
h = n.select.with_index { |_, i| i.odd? } << n[-1]

puts [a.join.to_i * b.join.to_i, c.join.to_i * d.join.to_i, e.join.to_i * f.join.to_i, g.join.to_i * h.join.to_i].max
