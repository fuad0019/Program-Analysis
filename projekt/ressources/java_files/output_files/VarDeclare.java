public class VarDeclareTest {
    
public int t;
public int k;
    
public int DeclareIntWithReturn() {
int var0 = 5;
return var0;}


public void DeclareIntWithParams(int var0, int var1) {
int var2 = var0;
int var3 = var1;}


public void UsingAGlobalVariable() {
int var0 = this.t;}


public void DeclareString() {
String var0 = "hej";}


public void AssignObject() {
TestClass var0 = new TestClass();}


public void methodCallOnObject() {
TestClass var0 = new TestClass();
var0.tryMe();}


public void constructObject() {
new TestClass();}


public void ifStatements() {
int var0 = 0;
if (var0 < 1){
int var1 = 10;
int var2 = 1;
}}


}