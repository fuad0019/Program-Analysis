public class EvalDecompiler {
    
public int ga;
    
public void return1() {
return;}


public String return2() {
return "hej";}


public float return3() {
return 3.4f;}


public boolean return4() {
return 1;}


public int return5() {
int var0 = 5;
return var0;}


public int return6(int var0) {
return var0;}


public void arith1() {
int var0 = 6;
int var1 = 0;
int var2 = 9;
int var3 = 1;
return;}


public void arith2(int var0, int var1) {
int var2 = var0 + var1;
int var3 = var0 - var1;
int var4 = var0 * var1;
int var5 = var0 / var1;
return;}


public void arith3() {
int var0 = 5;
int var1 = 5;
int var2 = var0 + var1;
int var3 = var0 - var1;
int var4 = var0 * var1;
int var5 = var0 / var1;
return;}


public void arith4() {
int var0 = 5;
int var1 = 5;
int var2 = 5;
int var3 = var0 + var1 + var2;
int var4 = var0 - var1 - var2;
int var5 = var0 * var1 * var2;
int var6 = var0 / var1 / var2;
return;}


public void if1(int var0, int var1) {
if (var0 > var1){
return;

}
return;}


public void if2(int var0, int var1) {
if (var0 == var1){
return;

}

}
return;}


public void if3(int var0, int var1) {
if (var0 < var1){
return;

}

}

}
return;}


public void if4(int var0, int var1) {
if (var0 != var1){
return;

}

}

}

}
return;}


public void if5(int var0, int var1) {
if (var0 == var1){
return;

}

}

}

}

}
return;}


public void if6() {
int var0 = 4;
int var1 = 4;

}

}

}

}

}}


public void loop1() {
int var0 = 0;

}

}

}

}

}
while (var0 < 5){
var0 = var0 + 1;
}
return;}


public void loop2() {
int var0 = 0;
while (5 > var0){
var0 = var0 + 1;
}
return;}


public void loop3() {
int var0 = 1;
while (var0 == 2){
var0 = var0 + 1;
}
return;}


public void loop4() {
int var0 = 1;
while (var0 != 2){
var0 = var0 + 1;
}
return;}


public void loop5() {
int var0 = 0;}


public void object1() {
TestClass var0 = new TestClass();
return;}


public void global1() {
int var0 = this.ga;
return;}


public void method1() {
return;}


private void method2() {
return;}


}