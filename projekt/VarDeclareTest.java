public class VarDeclareTest {

    public int DeclareIntWithReturn() {
        int a = 5;
        return a;
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

}