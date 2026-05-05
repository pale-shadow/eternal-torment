class Fixnum
  alias real_to_s to_s
  def to_s
    case
    when (self%3)==0 && (self%5)==0 then 'fizzbuzz'
    when (self%3)==0 then 'fizz'
    when (self%5)==0 then 'buzz'
    else self.real_to_s
    end
  end
end

puts (1..100).to_a
