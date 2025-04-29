require "time"

k = gets.to_i

t = Time.parse("21:00") + k * 60

puts t.strftime("%H:%M")
