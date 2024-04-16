package 백준_입출력방법;

import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class 자바 {
    public static void main(String[] args) throws Exception {
        //표준입력을 파일로 설정
        System.setIn(new java.io.FileInputStream("input.txt"));
        Example example = new Example();
        // example.직접입력1();
        example.StringBuilder_출력();
        
    }

    static class Example {

        // sc.nextByte()
        // sc.nextShort()
        // sc.nextInt()
        // sc.nextFloat()
        // sc.nextLong()
        // sc.nextDouble()
        // sc.nextBoolean()
        public void 직접입력1() {
            Scanner sc = new Scanner(System.in);

            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println("a : " + a + ", b : " + b);
            System.out.println(a + b);

            sc.close();
        }

        public void 직접입력2() {
            Scanner sc = new Scanner(System.in);

            // next()는 공백을 기준으로 입력을 받는다.
            // example : hello world
            String a = sc.next();
            String b = sc.next();

            System.out.println("a : " + a);
            System.out.println("b : " + b);

            sc.close();
        }

        public void 직접입력3() {
            Scanner sc = new Scanner(System.in);

            // nextLine()은 개행문자를 기준으로 입력을 받는다.
            // example : hello world \n its java time
            String a = sc.nextLine();
            String b = sc.nextLine();

            System.out.println("a : " + a);
            System.out.println("b : " + b);

            sc.close();
        }

        public void 여러_값을_받는_경우() {
            Scanner sc = new Scanner(System.in);

            int n = sc.nextInt(); // 입력받을 값의 개수
            int[] arr = new int[n];

            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }

            for (int i = 0; i < n; i++) {
                System.out.println(arr[i]);
            }

            sc.close();
        }

        public void BufferedReader_사용() throws IOException {
            /*
             * BufferedReader를 사용하면 더 빠르게 입력을 받을 수 있다.
             * BufferedReader는 예외처리를 해줘야 한다.
             * BufferedReader는 문자열로 입력을 받기 때문에 형변환을 해줘야 한다.
             * BufferedReader는 공백을 포함한 문자열을 입력받을 수 있다.
             * BufferedReader는 개행문자를 포함한 문자열을 입력받을 수 있다.
             */
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            int n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                System.out.println(a + b);
            }

            br.close();
        }

        public void BufferedWriter_출력() throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

            int n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                int s = Integer.parseInt(st.nextToken());

                for (int j = 0; j < s; j++) {
                    bw.write("=");
                    bw.newLine();
                }

                bw.flush();
            }

        }

        public void StringBuilder_출력() throws NumberFormatException, IOException {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            StringBuilder sb = new StringBuilder();

            int n = Integer.parseInt(br.readLine());
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                int s = Integer.parseInt(st.nextToken());
                for (int j = 0; j < s; j++) {
                    sb.append("=");
                }
                sb.append("\n");
            }

            System.out.println(sb);
        }

    }

}
