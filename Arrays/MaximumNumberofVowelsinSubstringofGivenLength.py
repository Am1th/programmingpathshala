t = int(input())

while t > 0:
    s, k = input().split()
    k = int(k)
    cnt, max_cnt = 0, 0
    n = len(s)

    for i in range(k):
        if s[i] in 'aeiou':
            cnt += 1
    max_cnt = max(cnt, max_cnt)

    for j in range(k, n):
        if s[j] in 'aeiou':
            cnt += 1
        if s[j - k] in 'aeiou':
            cnt -= 1
        max_cnt = max(cnt, max_cnt)
    print(max_cnt)
    t -= 1

# can convert string to list and do but not required because strings can be subscripted in python

# can create vowel array, and check like below
# for char in s:
#     if char in vowelarray:
#         cnt+=1


# in java can use set
"""
public static void main (String[] args) throws java.lang.Exception

    {

        // your code goes here

         BufferedReader br  =  new BufferedReader(new InputStreamReader(System.in));





        for(int t  = Integer.parseInt(br.readLine().trim()); t > 0; t--){

            String[] sk = br.readLine().trim().split(" ");



            int k= Integer.parseInt(sk[1]);

            String s = sk[0];



            Set<Character> v = Set.of('a','e','i','o','u');



            //first window

            int ctr = 0, y = 0; 

            while(y < k){

                char c  = s.charAt(y);

                if(v.contains(c)) ctr++;

                y++;

            }

            int max = ctr;

            for(int x = 0; y < s.length(); y++,x++){

                if(v.contains(s.charAt(x))) ctr--;

                if(v.contains(s.charAt(y))) ctr++;



                max = Math.max(ctr,max);



            }

            System.out.println(max);



        }

    }
"""

# below is java code conversion for the python code i wrote
"""
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt(); // Read the number of test cases
        sc.nextLine(); // Consume the newline character after the integer input

        while (t > 0) {
            String[] inputs = sc.nextLine().split(" ");
            String s = inputs[0]; // The string input
            int k = Integer.parseInt(inputs[1]); // The integer k

            int cnt = 0, max_cnt = 0;
            int n = s.length();

            // Count vowels in the first k characters
            for (int i = 0; i < k; i++) {
                if (isVowel(s.charAt(i))) {
                    cnt++;
                }
            }
            max_cnt = Math.max(cnt, max_cnt);

            // Slide the window and calculate the vowel count
            for (int j = k; j < n; j++) {
                if (isVowel(s.charAt(j))) {
                    cnt++;
                }
                if (isVowel(s.charAt(j - k))) {
                    cnt--;
                }
                max_cnt = Math.max(cnt, max_cnt);
            }
            System.out.println(max_cnt); // Output the result for the current test case
            t--; // Decrease the number of test cases
        }

        sc.close(); // Close the scanner
    }

    // Helper function to check if a character is a vowel
    private static boolean isVowel(char c) {
        return "aeiou".indexOf(c) != -1;
    }
}

"""
