require "prime"

def divisors(n)
  prime_factors = n.prime_division
  divisors = [1]

  prime_factors.each do |prime, exponent|
    new_divisors = []
    (0..exponent).each do |exp|
      power = prime ** exp
      divisors.each do |d|
        new_divisors << d * power
      end
    end
    divisors = new_divisors
  end

  divisors.sort
end

a, b = gets.chomp.split.map(&:to_i)

puts divisors(100).each.any? { [*a..b].include?(_1) } ? "Yes" : "No"
