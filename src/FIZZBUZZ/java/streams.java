import java.util.stream.IntStream;

/**
 * FizzBuzz implementation utilizing Java Streams for declarative sequence 
 * transformation. Targeted for the JVM runtime on 'chonk' and Jetson nodes.
 */
public class fizzbuzz {
    public static void main(String[] args) {
        IntStream.rangeClosed(1, 100)
            .mapToObj(i -> {
                if (i % 15 == 0) return "FizzBuzz";
                if (i % 3 == 0)  return "Fizz";
                if (i % 5 == 0)  return "Buzz";
                return String.valueOf(i);
            })
            .forEach(System.out::println);
    }
}