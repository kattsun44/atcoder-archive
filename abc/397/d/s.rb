require 'prime'

n = gets.to_i

primes = n.prime_division


def main(primes)
  if primes.size == 0
    puts -1
    return
  end

  primes.each do |p|
    a, b = p.sort
    1.upto(b) do |y|
      (y+1).upto(b) do |x|
        c = x-y
        d = x**2 + x*y + y**2
        next if c % 2 == 1 && d % 2 == 0
        if c == a && d == b
          puts "#{x} #{y}"
          return
        end
      end
    end
  end
end

main(primes)
