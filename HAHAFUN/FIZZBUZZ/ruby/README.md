# ruby

type "irb" to get prompt, then:

0.upto(100){|i|p"AyyLmao#{i}"[i%3<1?0:i%5<1?4:7,i%15<1?7:3]}
