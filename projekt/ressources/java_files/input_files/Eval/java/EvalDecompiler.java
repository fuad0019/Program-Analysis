public class EvalDecompiler {

    public int ga = 5;

    public void return1() { // Tester return void
        return;
    }

    public String return2() { // Tester return string
        return "hej";
    }

    public float return3() { // Tester Return float
        return 3.4f;
    }

    public boolean return4() { // Tester Return bool
        return true;
    }

    public int return5() { // Tester return int og variable declaration
        int a = 5;
        return a;
    }

    public int return6(int a) { // Tester return param
        return a;
    }

    // ____________________ARITHMETIC_________________________________//

    public void arith1() {
        int a = 3 + 3;
        int b = 3 - 3;
        int c = 3 * 3;
        int d = 3 / 3;
    }

    public void arith2(int a, int b) {
        int c = a + b;
        int d = a - b;
        int e = a * b;
        int f = a / b;
    }

    public void arith3() {
        int a = 5;
        int b = 5;
        int c = a + b;
        int d = a - b;
        int e = a * b;
        int f = a / b;
    }

    public void arith4() {
        int a = 5;
        int b = 5;
        int c = 5;
        int d = a + b + c;
        int e = a - b - c;
        int f = a * b * c;
        int g = a / b / c;

    }

    // _______________________IF_ELSE______________________________//

    public void if1() {
        if (2 > 1) {
            return;
        }
        if (2 == 2) {
            return;
        }
    }

    public void if2(int a, int b) {
        if (a > b) {
            return;
        } else {
            return;
        }
    }

    public void if3(int a, int b) {
        if (a == b) {
            return;
        } else {
            return;
        }
    }

    public void if4(int a, int b) {
        if (a < b) {
            return;
        } else {
            return;
        }
    }

    public void if5(int a, int b) {
        if (a != b) {
            return;
        } else {
            return;
        }
    }

    public void if6() {
        int a = 5;
        int b = 4;
        if (a > b) {
            return;
        } else {
            return;
        }
    }

    public void if7() {
        int a = 5;
        int b = 4;
        if (a < b) {
            return;
        } else {
            return;
        }
    }

    public void if8() {
        int a = 5;
        int b = 4;
        if (a == b) {
            return;
        } else {
            return;
        }
    }

    public void if9() {
        int a = 5;
        int b = 4;
        if (a != b) {
            return;
        } else {
            return;
        }
    }

    // _______________________LOOPS______________________________//

    public void loop1() {
        int a = 0;
        while (a < 5) {
            a = a + 1;
        }
    }

    public void loop2() {
        int a = 0;
        while (5 > a) {
            a = a + 1;
        }
    }

    public void loop3() {
        int a = 0;
        while (a == 0) {
            a = a + 1;
        }
    }

    public void loop4() {
        int a = 0;
        while (a != 0) {
            a = a + 1;
        }
    }
    // ________________________OBJECT_____________________________//

    public void object1() {
        TestClass myTestClass = new TestClass(); // Create an object
    }

    // ________________________GLOBAL_VARIABLE_____________________________//
    public void global1() {
        int a = ga;
    }

    // ________________________METHODS_____________________________//
    public void method1() { // Public

    }

    private void method2() { // Private

    }
}