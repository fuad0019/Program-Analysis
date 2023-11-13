public class VarDeclareTest {


    public int t = 5;
    public int k = 7;


    public int DeclareIntWithReturn() {
        int a = 5;
        return a;
    }

    public void DeclareIntWithParams(int a, int b){
        int c = a;
        int d = b;
    }

    public void DeclareString() {
        String a = "hej";
    }

    public void AssignObject() {
        TestClass test = new TestClass();
    }

    public void methodCallOnObject() {
        TestClass test = new TestClass();

        test.tryMe();
    }

    public void constructObject() {
        new TestClass();

    }

    public void ifStatements() {
        int counter = 0;
        if (counter < 1) {

            int a = 10;

        }

        String b = "hello";
    }

    public void ifElseStatements() {
        int counter = 0;
        if (counter != 1) {

            int a = 10;

        }

        else {
            String b = "hello";
        }

    }

    public void loopWithBasicBlocks() {
        int counter = 0;
        while (counter < 10) {
            String a = "hello";
            counter++;

        }
    }

}