public class EvalObject {

    public void object1() {
        TestClass myTestClass = new TestClass(); // Create an object
        myTestClass.tryMe();
    }
}

private class TestClass { // TestClass for object declaration
    TestClass() {
        System.out.println("hello");
    }

    public void tryMe() {

    }
}
