import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_var_201(self):
        input = """
function A(a:integer):integer;
var a:array[1 .. 2] of real;
begin

end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        

    def test_var_202(self):
        input = """
Var       
    Num1, Num2, Sum : Integer;
Procedure main();
Begin {no semicolon}
	Write("Input number 1:"); 
	Readln(Num1);
	Writeln("Input number 2:");
	Readln(Num2);
	Sum := Num1 + Num2; {addition} 
	Writeln(Sum);
	Readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,202))
        

    def test_var_203(self):
        input = """
Var name, surname: String;
Procedure main();
Begin
	write("Enter your name:");
	readln(name);
	write("Enter your surname:");
	readln(surname);
	writeln();{new line}
	writeln();{new line}
	writeln("Your full name is: ",name," ",surname);
	readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))


    def test_var_204(self):
        input = """
Var 
	surname: String;
procedure main();
Begin
	Write("Enter your surname:");
	readln(surname);
	writeln();
	writeln();
	Writeln("Your full name is: ",name," ",surname);
	readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))
        

    def test_var_205(self):
        input = """
Var Sel: String;
    N1,N2, Total : Real;
    YN : String;  { this is a character variable type, which holds single characters ONLY }
procedure main();
Begin
	Total := 0;  { always initialise integer/real variables }
	GotoXy(4,3);
	Writeln("1.Addition");
	GotoXy(4,4);
	Writeln("2.Subtraction");
	GotoXy(4,5);
	Writeln("3.Exit");
	GotoXy(6,8);
	Write("Select: ");
	Sel := Readkey();

	If Sel = "1" {condition} Then 
	Begin  {more than one statement}
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 + N2;
		Writeln("Addition: ",N1," + ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end { Closing the if statement }

	If Sel = "2" Then { note that here we do not use an assignment statement } 
	Begin 
		ClrScr();
		Write("Input No.1:");
		Readln(N1);
		Write("Input No.2:");
		Readln(N2);
		Total := N1 - N2;
		Write("Subtraction: ");
		Write(N1," - ",N2," = ",Total);
		Write("Press any key to continue...");
		Readkey();
	end  { Closing the if statement }

	If Sel = "3" Then 
	Begin
		ClrScr();
		Write("Are you sure?(Y/N)");
		YN := Readkey();
		If YN = "y" Then Halt(); { 1 instruction, so no need of Begin..End }
		If YN = "n" Then Goto1(); { the goto statement is not recommended for frequent use }
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,205))
        

    def test_if_206(self):
        input = """
Var
	SEL : Integer;
	YN : String;
procedure main();
Begin
	Writeln("[1]. PLAY GAME");
	WRITELN("[2]. LOAD GAME");
	WRITELN("[3]. MULTIPLAYER");
	WRITELN("[4]. EXIT GAME");
	Writeln("note: Do not press anything except");
	Writeln("numbers; otherwise an error occurs!");
	Readln(SEL);
	
	If SEL = 1 Then
	Begin
		Writeln("You will soon be able to create");
		Writeln("games using Pascal Programming :-)");
		Delay(2000);
		Goto(Ret);
	end

	If SEL = 2 Then
	Begin
		Writeln("Ahhh... no saved games");
		Delay(2000);
		Goto(Ret);
	end

	If SEL = 3 Then
	Begin
		Writeln("networking or 2 players?");
		Delay(2000);
		Goto(Ret);
	end

	If SEL = 4 Then
	Begin
		Writeln("Are you sure you want to Exit?");
		YN := Readkey;
		If YN = "y" Then
		Begin
			Writeln("Good Bye...");
			Delay(1000);
			Halt(); {EXIT PROGRAM}
		end

		If YN = "n" Then
			Goto(Ret);
	end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,206))
        

    def test_while_207(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not ((n1 = "0") AND (n2 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If (n1 = "0") AND (n2 = "0") Then Halt(0);
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,207))
        

    def test_or_208(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not ((n1 = "0") OR (n2 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If (n1 = "0") OR (n2 = "0") Then Halt(0);
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,208))
        

    def test_not_209(self):
        input = """
Var n1, n2 : string;
procedure main();
Begin
	Writeln("Enter two numbers: (\\\"\\\"0\\\"\\\" & \\\"\\\"0\\\"\\\" to exit)");
	While not (NOT (n1 = "0")) do
    Begin
		Write("No.1: ");
		Readln(n1);
		Write("No.2: ");
		Readln(n2);
		If NOT (n1 = "0") Then Halt(0);
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,209))
        

    def test_and_210(self):
        input = """
Var age : Integer;
procedure main();
Begin
	While (age > 0) AND (age <= 100) Do
    Begin
		Write("Enter age (1 - 100): ");
		Readln(age);
		If (age < 1) Then
			Writeln("Age cannot be less than 1...");
		Else If (age > 100) Then
			Writeln("Age cannot be greater than 100...");
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,210))
        

    def test_bool_211(self):
        input = """
Var 
	bool : Boolean;
	A, B : Integer;
Procedure main();
Begin
	A := 10;
	B := 20;
	bool := False;
	bool := (A = 10) OR (B = 10);
	Writeln(bool); { outputs TRUE }
	bool := (A = 10) AND (B = 10);
	Writeln(bool); { outputs FALSE }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,211))
        

    def test_bool_212(self):
        input = """
Var quit : Boolean;
    a    : String;
Procedure main();
Begin
	While NOT (quit = True) Do
    Begin
		Writeln("Type \\\"\\\"exit\\\"\\\" to quit:");
		Readln(a);
		If a = "exit" Then 
			quit := True;
    End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,212))
        

    def test_for_213(self):
        input = """
Procedure DrawLine(); 
{This procedure helps me to avoid the rewriting the for loops}
Var Counter : Integer;
Begin
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196)); 
	End
End

Procedure Main();
Begin
	GotoXy(10,5);
	DrawLine();
	GotoXy(10,6);
	DrawLine();
	GotoXy(10,7);
	DrawLine();
	GotoXy(10,10);
	DrawLine();
	Readkey();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,213))
        

    def test_for_214(self):
        input = """
Procedure DrawLine(X : Integer; Y : Integer);
{ the declaration of the variables in brackets are called parameters }
Var Counter : Integer; { this is called a local variable }
Begin
	GotoXy(X,Y); {here I use the arguments of X and Y}
	textcolor(green);
	For Counter := 1 to 10 do
	Begin 
		Write(chr(196));
	End
End

Procedure main();
Begin
	DrawLine(10,5);
	DrawLine(10,6);
	DrawLine(10,7);
	DrawLine(10,10);
	Readkey();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,214))
        

    def test_procedure_215(self):
        input = """
Procedure Square(Index : Integer; Result : Integer);
Begin
	Result := Index * Index;
End

Var
	Res : Integer;

Procedure Main();
Begin
	Writeln("The square of 5 is: ");
	Square(5, Res);
	Writeln(Res);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,215))
        

    def test_string_216(self):
        input = """
Var
	UserFile : String;
	FileName, TFile : String;

Procedure Main();
Begin
	Writeln("Enter the file name (including its full path) of the text file (without the extension):");
	Readln(FileName); { A .txt file will be assigned to a text variable }
	Assign(UserFile, FileName + ".txt");
	Reset(UserFile); { "Reset(x)" - means open the file x and reset cursor to the beginning of file }
	While NOT Eof(UserFile) Do
    Begin
		Readln(UserFile,TFile);
		Writeln(TFile);
	End
	Close(UserFile);
	Readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,216))
        

    def test_string_217(self):
        input = """
Var
	FName, Txt : String;
	UserFile   : String; 

Procedure Main();
Begin
	FName := "Textfile";
	Assign(UserFile, "C:\\\\" + FName + ".txt"); {assign a text file}
	Rewrite(UserFile); {open the file "fname" for writing}
	Writeln(UserFile, "PASCAL PROGRAMMING");
	Writeln(UserFile, "if you did not understand something,");
	Writeln(UserFile, "please send me an email to:");
	Writeln(UserFile, "victorsaliba@hotmail.com");
	Writeln("Write some text to the file:");
	Readln(Txt);
	Writeln(UserFile, "");
	Writeln(UserFile, "The user entered this text:");
	Writeln(UserFile, Txt);
	Close(UserFile);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,217))
        

    def test_string_218(self):
        input = """
Var
	UFile : String;

Procedure main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	ReWrite(UFile); 
	Writeln(UFile, "How many sentences " + "are present in this file?");
	Close(UFile);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,218))
        

    def test_string_219(self):
        input = """
Var
	UFile : String;

Procedure Main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	Append(UFile); 
	Writeln(UFile, "How many sentences, "+"are present in this file?");
	Close(UFile);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,219))
        

    def test_string_220(self):
        input = """
Var
	UFile : String; { or it could be of "file" type}

Procedure Main();
Begin
	Assign(UFile, "C:\\\\ADDTEXT.TXT");
	Erase(UFile); 
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,220))
        

    def test_string_221(self):
        input = """
Var
	t : String;
	s : String;

Procedure main();
Begin
	Assign(t, "C:\\\\ABC.DEF");
	{$I-}   { disable i/o error checking }
	Reset(t);
	{$I+}   { enable again i/o error checking - important }
	If (IOResult <> 0) Then
	Begin
		Writeln("The file required to be opened is not found!");
		Readln();
	End Else 
	Begin
		Readln(t,s);
		Writeln("The first line of the file reads: ",s);
		Close(t);
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,221))
        

    def test_string_222(self):
        input = """
Var
	NewDir : String; { for searching the dir and create a new one, if it does not exist }
	F : String;

Procedure Main();
Begin
	{ search for the dir }
	NewDir := FSearch("C:\\\\Pascal Programming", GetEnv("")); 
	{ create a new one, if it does not exist }
	If NewDir = "" Then
		CreateDir("C:\\\\Pascal Programming"); 
	Assign(F,"C:\\\\Pascal Programming\\\\pascal-programming.txt");
	{$I-} ReWrite(F); {$I+} { disable and enable back again I/O error checking } 
	{ write to text file } 
	Writeln(F,"http://pascal-programming.info/"); 
	{$I-} Close(F); {$I+}
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,222))
        

    def test_string_223(self):
        input = """
Var
	f : String; { file var of type byte }
	sz : Integer;  { var for the size }

Procedure Main();
Begin
	Assign(f,"C:\\\\anyfile.txt");
	{$I-} Reset(f); {$I+}
	If (IOResult <> 0) Then
 	Begin     { file found? }
  		Writeln("File not found.. exiting");
  		Readln();
 	End Else
 	Begin
			{ Return the file size in Kilobytes }
  		sz := Round(FileSize(f)/1024);
  		Writeln("Size of the file in Kilobytes: ",sz," Kb");
  		Readln();
  		Close(f); 
 	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,223))
        

    def test_array_224(self):
        input = """
Var
	myVar : Integer;
	myArray : Array[1 .. 5] of Integer;

Procedure Main();
Begin
	myArray[2] := 25;
	myVar := myArray[2];
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,224))
        

    def test_array_225(self):
        input = """
Var
	i : Integer;
	myIntArray : Array[1 .. 20] of Integer;
	myBoolArray : Array[1 .. 20] of Boolean;

Procedure Main();
Begin
	For i := 1 to Length(myIntArray) do
	Begin
		myIntArray[i] := 1;
		myBoolArray[i] := True;
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,225))
        

    def test_string_226(self):
        input = """
Var
    myString : String;

Procedure Main();
Begin
	myString := "Hey! How are you?";
	Writeln("The length of the string is ", byte(myString[0]));
	Write(myString[byte(myString[0])]);
	Write(" is the last character.");
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,226))
        

    def test_string_227(self):
        input = """
Var
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	Write("The word \\"How\\" is found at char index ");
	Writeln(Pos("How", S));
	If Pos("Why", S) <= 0 Then
		Writeln("\\"Why\\" is not found.");
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,227))
        

    def test_string_228(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey there! How are you?";
	S := Copy(S, 5, 6); { "there!" }
	Write(S);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,228))
        

    def test_string_229(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey Max! How are you?";
	Delete(S, 4, 4); { "Hey! How are you?" }
	Write(S);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,229))
        

    def test_string_230(self):
        input = """
Var 
	S : String;

Procedure main();
Begin
	S := "Hey! How are you?";
	Insert(" Max", S, 4);
	Write(S);
  { "Hey Max! How are you?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,230))
        

    def test_string_231(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "Hey!";
	S2 := " How are you?";
	Write(Concat(S1, S2)); { "Hey! How are you?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,231))
        

    def test_string_232(self):
        input = """
Var 
	S1, S2 : String;

Procedure main();
Begin
	S1 := "Hey!";
	S2 := " How are you?";
	Write(S1 + S2); { "Hey! How are you?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,232))
        

    def test_string_233(self):
        input = """
Var 
   S : String;
   i : Integer;

Procedure main();
Begin
	S := "Hey! How are you?";
	For i := 1 to length(S) do
		S[i] := UpCase(S[i]);
	Write(S); { "HEY! HOW ARE YOU?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,233))
        

    def test_string_234(self):
        input = """
Var 
   S : String;

Procedure main();
Begin
	S := "Hey! How are you?";
	Write(UpCase(S)); { "HEY! HOW ARE YOU?" }
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,234))
        

    def test_string_235(self):
        input = """
Var 
	S : String;
	i : Real;

Procedure main();
Begin
	i := -0.563; 
	Str(i, S);
	Write(S); 
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,235))
        

    def test_string_236(self):
        input = """
Var 
	S     : String;
	error : Integer;
	R     : Real;

Procedure main();
Begin
	S := "-0.563"; 
	Val(S, R, error);
	If error > 0 Then
  	Write("Error in conversion.");
	Else
		Write(R); 
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,236))
        

    def test_complex_237(self):
        input = """
Procedure BubbleSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, temp : Integer;

Begin
	For i := size-1 DownTo 1 do
		For j := 2 to i do
			If (numbers[j-1] > numbers[j]) Then
			Begin
				temp := numbers[j-1];
				numbers[j-1] := numbers[j];
				numbers[j] := temp;
			End

End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,237))
        

    def test_complex_238(self):
        input = """
Procedure InsertionSort(numbers : Array[1 .. 100] of Integer; size : Integer);
Var
	i, j, index : Integer;


Begin
	For i := 2 to size-1 do
	Begin
		index := numbers[i];
		j := i;
		While ((j > 1) AND (numbers[j-1] > index)) do
		Begin
			numbers[j] := numbers[j-1];
			j := j - 1;
		End
		numbers[j] := index;
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,238))
        

    def test_complex_239(self):
        input = """
Procedure QSort(numbers : Array [1 .. 100] of Integer; left : Integer; right : Integer);
Var 
	pivot, l_ptr, r_ptr : Integer;

Begin
	l_ptr := left;
	r_ptr := right;
	pivot := numbers[left];

	While (left < right) do
	Begin
		While ((numbers[right] >= pivot) AND (left < right)) do
			right := right - 1;

		If (left <> right) Then
		Begin
			numbers[left] := numbers[right];
			left := left + 1;
		End

		While ((numbers[left] <= pivot) AND (left < right)) do
			left := left + 1;

		If (left <> right) Then
		Begin
			numbers[right] := numbers[left];
			right := right - 1;
		End
	End

	numbers[left] := pivot;
	pivot := left;
	left := l_ptr;
	right := r_ptr;

	If (left < pivot) Then
		QSort(numbers, left, pivot-1);

	If (right > pivot) Then
		QSort(numbers, pivot+1, right);
End

Procedure QuickSort(numbers : Array [1 .. 100] of Integer; size : Integer);
Begin
	QSort(numbers, 0, size-1);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,239))
        

    def test_complex_240(self):
        input = """
Var
	myStack : Array[1 .. 100] of Integer;
	topPointer : Integer;


Procedure InitStack();
Begin
	topPointer := 0;
End
//We now implemement the IsEmpty() and IsFull() functions.

Function IsEmpty() : Boolean;
Begin
	IsEmpty := False;
	If (topPointer = 0) Then
		IsEmpty := true;
End

Function IsFull() : Boolean;
Begin
	IsFull := False;
	If ((topPointer + 1) = STACK_SIZE) Then
		IsFull := True;
End
//Here are the implementations of the Pop() and Push() functions and making use of the functions that we have just implemented.

Function Pop() : Integer;

Begin
	Pop := nil;

	If not IsEmpty Then
	Begin
		Pop := myStack[topPointer];
		topPointer := topPointer - 1; 
	End
End

Procedure Push(item : Integer);
Begin
	If not IsFull Then
	Begin
		myStack[topPointer+1] := item;
		topPointer := topPointer + 1;
	End
End

//Finally, we implement the utility function GetSize(). Although one can access the current size of the stack using the global variable topPointer, it is of good practice to make use of functions instead of global variables.

Function GetSize() : Integer;
Begin
	GetSize := topPointer;
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,240))
        

    def test_complex_241(self):
        input = """
Var Counter : Integer; { loop counter declared as integer }

Procedure main();
Begin
	For Counter := 1 to 7 do { it"s easy and fast! }
		Writeln("for loop");
	Readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,241))
        

    def test_complex_242(self):
        input = """
Var 
	Counter : Integer;  { will be used as a loop counter }

Procedure main();
Begin

	For Counter := 1 to 5 do 
	Begin      
		gotoxy(25, 5 + Counter);
		Writeln("I");
	End

	For Counter := 5 Downto 1 do
	Begin  {an example of "downto" instead of "to", note the "gotoxy(_,_)"}
		gotoxy(32, 11 - Counter);
		Writeln("I");
	End

	For Counter := 1 to 6 do
	Begin
		gotoxy(25 + Counter, 11);
		Writeln("-");
	End

	For Counter := 6 Downto 1 do
	Begin
		gotoxy(32 - Counter, 5);
		Writeln("-");
	End

	{--------------The Corners(+)---------------}
	Gotoxy(25,5);
	Writeln("+");
	GotoXy(25,11);
	Writeln("+");
	GotoXy(32,5);
	Writeln("+");
	GotoXy(32,11);
	Writeln("+");
	GotoXy(45,7); 
	Write("Made with For Loops :)");
	Readln();
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,242))
        

    def test_complex_243(self):
        input = """
Var Ch : String;

Procedure main();
Begin
	Writeln("Press \\"\\"q\\"\\" to exit...");
	Ch := Readkey();
	While Ch <> "q" do 
	Begin
		Writeln("Please press \\"\\"q\\"\\" to exit.");
		Ch := Readkey();
	End
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,243))
        

    def test_complex_244(self):
        input = """
Function Factorial(n : Integer) : Integer;
Var
	Result : Integer;
	i : Integer;

Begin
	Result := n;
	If (n <= 1) Then
		Result := 1;
	Else
	For i := n-1 DownTo 1 do
		Result := Result * i; 
	Factorial := Result;
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,244))
        

    def test_complex_245(self):
        input = """
Function Factorial(n : Integer) : Integer;
Var
	Result : Integer;

Begin
	If n = 1 Then 
		Factorial := 1;
	Else
		Factorial := n*Factorial(n-1);
End
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,245))
        

    def test_complex_246(self):
        input = """
var
age, weekdays : integer;
taxrate, net_income: real;
choice, isready: boolean;
name, surname : string;
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,246))
        

    def test_complex_247(self):
        input = """
var
firstname, surname: string;

procedure main();
begin
   writeln("Please enter your first name: ");
   readln(firstname);
   
   writeln("Please enter your surname: ");
   readln(surname);
   
   writeln();
   writeln(message, " ", firstname, " ", surname);
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,247))
        

    def test_complex_248(self):
        input = """
procedure main();
var a:integer;
begin
a := a = a and then b;
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,248))
        

    def test_complex_249(self):
        input = """
var
{ local variable declaration }
   a:integer;

procedure main();
begin
   a:= 10;
   (* check the boolean condition using if statement *)
   
   if( a < 20 ) then
      (* if condition is true then print the following *) 
      writeln("a is less than 20 " );
   writeln("value of a is : ", a);
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,249))
        

    def test_if_250(self):
        input = """
var
   { local variable definition }
   a : integer;

procedure main();
begin
   a := 100;
   (* check the boolean condition *)
   if( a < 20 ) then
      (* if condition is true then print the following *)
      writeln("a is less than 20" );
   
   else
      (* if condition is false then print the following *) 
      writeln("a is not less than 20" );
      writeln("value of a is : ", a);
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,250))
        

    def test_if_251(self):
        input = """
var
   { local variable definition }
   a : integer;

procedure main();
begin
   a := 100;
   (* check the boolean condition *)
   if (a = 10)  then
      (* if condition is true then print the following *)
      writeln("Value of a is 10" );
   
   else if ( a = 20 ) then
      (* if else if condition is true *)
      writeln("Value of a is 20" );
   
   else if( a = 30 ) then 
      (* if else if condition is true  *)
      writeln("Value of a is 30" );
   
   else
      (* if none of the conditions is true *)
      writeln("None of the values is matching" );
      writeln("Exact value of a is: ", a );
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,251))
        

    def test_if_252(self):
        input = """
var
   { local variable definition }
   a, b : integer;

procedure main();
begin
   a := 100;
   b:= 200;
   
   (* check the boolean condition *)
   if (a = 100) then
      (* if condition is true then check the following *)
      if ( b = 200 ) then
         (* if nested if condition is true  then print the following *)
         writeln("Value of a is 100 and value of b is 200" );
   
   writeln("Exact value of a is: ", a );
   writeln("Exact value of b is: ", b );
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,252))
        

    def test_while_253(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   while  a < 20  do
   
   begin
      writeln("value of a: ", a);
      a := a + 1;
   end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,253))
        

    def test_for_254(self):
        input = """
var
   a: integer;

procedure main();
begin
   for a := 10  to 20 do
   
   begin
      writeln("value of a: ", a);
   end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,254))
        

    def test_for_255(self):
        input = """
var
   i, j:integer;

procedure main();
begin
   for i := 2 to 50 do
   
   begin
      for j := 2 to i do
         if (i mod j)=0  then
            break; {* if factor found, not prime *}
      
      if(j = i) then
         writeln(i , " is prime" );
   end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,255))
        

    def test_break_256(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   (* while loop execution *)
   while  a < 20 do
   
   begin
      writeln("value of a: ", a);
      a:=a +1;
      
      if( a > 15) then
         (* terminate the loop using break statement *)
      break;
   end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,256))
        

    def test_continue_257(self):
        input = """
var
   a: integer;

procedure main();
begin
   a := 10;
   
   while not ( a = 20 ) do
   begin
      if( a = 15) then
      
      begin
         (* skip the iteration *)
         a := a + 1;
         continue;
      end
      
      writeln("value of a: ", a);
      a := a+1;
   end
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,257))
        

    def test_function_258(self):
        input = """
function max(num1, num2: integer): integer;

var
   (* local variable declaration *)
   result: integer;

begin
   if (num1 > num2) then
      result := num1;
   
   else
      result := num2;
   max := result;
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,258))
        

    def test_function_259(self):
        input = """
var
   a, b, ret : integer;

(*function definition *)
function max(num1, num2: integer): integer;
var
   (* local variable declaration *)
   result: integer;

begin
   if (num1 > num2) then
      result := num1;
   
   else
      result := num2;
   max := result;
end

begin
   a := 100;
   b := 200;
   (* calling a function to get max value *)
   ret := max(a, b);
   
   writeln( "Max value is : ", ret );
end
        """
        expect = "Error on line 20 col 0: begin"
        self.assertTrue(TestParser.test(input,expect,259))
        

    def test_procedure_260(self):
        input = """
procedure findMin(x, y, z: integer; m: integer); 
(* Finds the minimum of the 3 values *)

begin
   if x < y then
      m := x;
   else
      m := y;
   
   if z <m then
      m := z;
end { end of procedure findMin }  
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,260))
        

    def test_procedure_261(self):
        input = """
var
   a, b, c,  min: integer;
procedure findMin(x, y, z: integer; m: integer); 
(* Finds the minimum of the 3 values *)

begin
   if x < y then
      m:= x;
   else
      m:= y;
   
   if z < m then
      m:= z;
end { end of procedure findMin }  

procedure main();
begin
   writeln(" Enter three numbers: ");
   readln( a, b, c);
   findMin(a, b, c, min); (* Procedure call *)
   
   writeln(" Minimum: ", min);
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,261))
        

    def test_complex_262(self):
        input = """
var
   num, f: integer;
function fact(x: integer): integer; (* calculates factorial of x - x! *)

begin
   if x=0 then
      fact := 1;
   else
      fact := x * fact(x-1); (* recursive call *)
end; { end of function fact}

procedure main();
begin
   writeln(" Enter a number: ");
   readln(num);
   f := fact(num);
   
   writeln(" Factorial ", num, " is: " , f);
end
        """
        expect = "Error on line 11 col 3: ;"
        self.assertTrue(TestParser.test(input,expect,262))
        

    def test_complex_263(self):
        input = """
var
   i: integer;
function fibonacci(n: integer): integer;

begin
   if n=1 then
      fibonacci := 0;
   
   else if n=2 then
      fibonacci := 1;
   
   else
      fibonacci := fibonacci(n-1) + fibonacci(n-2);
end

procedure main();
begin
   for i:= 1 to 10 do
   
   write(fibonacci (i), "  ");
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,263))
        

    def test_complex_264(self):
        input = """
var
   a, b : integer;
(*procedure definition *)
procedure swap(x, y: integer); 

var
   temp: integer;

begin
   temp := x;
   x:= y;
   y := temp;
end

procedure main();
begin
   a := 100;
   b := 200;
   writeln("Before swap, value of a : ", a );
   writeln("Before swap, value of b : ", b );
   
   (* calling the procedure swap  by value   *)
   swap(a, b);
   writeln("After swap, value of a : ", a );
   writeln("After swap, value of b : ", b );
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,264))
        

    def test_easy_265(self):
        input = """
var
   a, b, c: integer;

procedure main();
begin
   (* actual initialization *)
   a := 10;
   b := 20;
   c := a + b;
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,265))
        

    def test_easy_266(self):
        input = """
var
   a, b, c: integer;
procedure display();

var
   a, b, c: integer;
begin
   (* local variables *)
   a := 10;
   b := 20;
   c := a + b;
   
   writeln("Winthin the procedure display");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
end

procedure main();
begin
   a:= 100;
   b:= 200;
   c:= a + b;
   
   writeln("Winthin the program exlocal");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   display();
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,266))
        

    def test_complex_267(self):
        input = """
var
   a, b, c: integer;
procedure display();
var
   x, y, z: integer;

begin
   (* local variables *)
   x := 10;
   y := 20;
   z := x + y;
   
   (*global variables *)
   a := 30;
   b:= 40;
   c:= a + b;
   
   writeln("Winthin the procedure display");
   writeln(" Displaying the global variables a, b, and c");
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   writeln("Displaying the local variables x, y, and z");
   
   writeln("value of x = ", x , " y =  ",  y, " and z = ", z);
end

procedure main();
begin
   a:= 100;
   b:= 200;
   c:= 300;
   
   writeln("Winthin the program exlocal");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   
   display();
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,267))
        

    def test_complex_268(self):
        input = """
var
   a, b, c: integer;
procedure display();

var
   a, b, c: integer;

begin
   (* local variables *)
   a := 10;
   b := 20;
   c := a + b;
   
   writeln("Winthin the procedure display");
   writeln(" Displaying the global variables a, b, and c");
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
   writeln("Displaying the local variables a, b, and c");
   
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);
end

procedure main();
begin
   a:= 100;
   b:= 200;
   c:= 300;
   
   writeln("Winthin the program exlocal");
   writeln("value of a = ", a , " b =  ",  b, " and c = ", c);   
   
   display();
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,268))
        

    def test_string_269(self):
        input = """
var
   greetings: string;
   name: array [1 .. 10] of integer;
   organisation: string;

procedure main();
begin
   greetings := "Hello ";
   message := "Good Day!";
   
   writeln("Please Enter your Name");
   readln(name);
   
   writeln("Please Enter the name of your Organisation");
   readln(organisation);
   
   writeln(greetings, name, " from ", organisation);
   writeln(message); 
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,269))
        

    def test_string_270(self):
        input = """
var
   str1, str2, str3 : string;
   str4: string;
   len: integer;

procedure main();
begin
   str1 := "Hello ";
   str2 := "There!";
   
   (* copy str1 into str3 *)
   str3 := str1;
   writeln("appendstr( str3, str1) :  ", str3 );
   
   (* concatenates str1 and str2 *)
   appendstr( str1, str2);
   writeln( "appendstr( str1, str2) " , str1 );
   str4 := str1 + str2;
   writeln("Now str4 is: ", str4);
   
   (* total lenghth of str4 after concatenation  *)
   len := byte(str4[0]);
   writeln("Length of the final string str4: ", len); 
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,270))
        

    def test_bool_271(self):
        input = """
var
exit: boolean;

choice: integer;

procedure main();
begin
   writeln("Do you want to continue? ");
   writeln("Enter Y/y for yes, and N/n for no");
   readln(choice);

if(choice = "n") then
   exit := true;
else
   exit := false;

if (exit) then
   writeln(" Good Bye!");
else
   writeln("Please Continue");

readln();
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,271))
        

    def test_array_272(self):
        input = """
var
   n: array [1 .. 10] of integer;   (* n is an array of 10 integers *)
   i, j: integer;

procedure main();
begin
   (* initialize elements of array n to 0 *)        
   for i := 1 to 10 do
       n[ i ] := i + 100;   (* set element at location i to i + 100 *)
    (* output each array element"s value *)
   
   for j:= 1 to 10 do
      writeln("Element[", j, "] = ", n[j] );
end
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,272))
        

    def test_complex_273(self):
        input = """
  VAR X, Y1, Y2,  First, Last, Incr, Factor: REAL;
  Q1, Q2, Step:  INTEGER;
  PROCEDURE main();
  BEGIN
  { Input plot  parameters }
  Write("Enter  first value: ");
  Read(First);
  Write("Enter  last value: ");
  Read(Last);
  Write("Enter  scale factor: ");
  Read(Factor);
  Write("Enter an  increment: ");
  Read(Incr);
  WriteLn();
  { Draw  horizontal Y axis }
  FOR Step := 0 TO  MaxY DO
  IF (Step MOD 5 =  0) THEN
  Write("+");
  ELSE
  Write("-");
  Write(" Y ");
  WriteLn();
  { Do the Plot on  its side }
  X := First;
  WHILE X <=  Last DO BEGIN
  Y1 :=  SIN(3.14159 * X / 180.0);
  Y1 := Factor *  Y1;
  Q1 := ROUND(Y1);
  Y2 := 0.005 * X;
  Y2 := Factor *  Y2;
  Q2 := ROUND(Y2);
  FOR Step := 0 TO  MaxY DO
  IF Step = 0 THEN
  Write( "|");
  ELSE
  IF Step = Q1  THEN
  Write( "*");
  ELSE
  IF Step = Q2  THEN
  Write( "+");
  ELSE
  Write( " ");
  WriteLn();
  X := X + Incr;
  END { WHILE }
  Write("X");
  END { SidePlotXY  }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,273))
        

    def test_complex_274(self):
        input = """
  VAR First,  Second, Left, Right: BOOLEAN;
  PROCEDURE  WriteBool(Val: BOOLEAN);
  BEGIN
  IF Val THEN
  Write("TRUE ");
  ELSE
  Write("FALSE ");
  END { WriteBool  }
  PROCEDURE Main();
  BEGIN
  { Write Header }
  WriteLn("Proof  of DeMorgan theorem ");
  WriteLn();
  WriteLn("First  Second Left Right ");
  WriteLn("-----  ------ ----- ----- ");
  { Loop through  all truth value combinations }
  FOR First :=  FALSE TO TRUE DO
  FOR Second :=  FALSE TO TRUE DO BEGIN
  { Write out  Input values of First, Second }
  WriteBool(First);
  WriteBool(Second);
  { Separate Input  values from the output }
  Write(" ");
  Left := (NOT  First) AND (NOT Second);
  Right := NOT(First OR Second);
  { Write out the  new values of Left, Right }
  WriteBool(Left);
  WriteBool(Right);
  WriteLn();
  END { Inner FOR  }
  END { TruthTable  }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,274))
        

    def test_string_275(self):
        input = """
  (* Demonstrates  some String actions *)
  (* that involve  names of people *)
  VAR FirstName,  LastName, FullName: STRING;
  Count,  NameCount, Gap: INTEGER;
  PROCEDURE main();
  BEGIN
  Space := "  ";
  Hyphen := "-";
  Greeting :=  "Hello there ";
  Write("Enter the  number of names: ");
  ReadLn(NameCount);
  WriteLn();
  WHILE NameCount  >0 DO BEGIN
  Write("Enter a  name, last name first: ");
  Read(FullName);
  Gap :=  POS(Space, FullName); { NOTE }
  IF Gap > 0  THEN BEGIN
  LastName :=  Copy(FullName, 1, Gap);
  Delete(FullName,  1, Gap); { NOTE }
  FirstName :=  FullName;
  IF Length(LastName) <= 4 THEN
  WriteLn("That is  a short last name");
  IF Pos(Hyphen,  LastName) <> 0 THEN
  WriteLn("That is  a hyphenated name");
  IF FirstName =  "Bill" THEN { etc., etc. }
  WriteLn("Bill is  a good name ");
  FullName :=  FirstName + Space + LastName;
  WriteLn(Greeting,  FullName);
  WriteLn();
  END { IF }
  NameCount :=  NameCount - 1;
  END { WHILE }
  END { NameParse  }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,275))
        

    def test_easy_276(self):
        input = """
PROCEDURE main(); 
  BEGIN (* To De-Militarize Time *)
  Read(MilTime);
  Hours := MilTime  DIV 100;
  Minutes :=  MilTime MOD 100;
  Write(Hours,  Minutes);
  END (* of  De-Militarizing Time *)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,276))
        

    def test_complex_277(self):
        input = """
  (* Problem of  Interest on a loan *)
  (* Computes: the  Balloon Payment total interest *)
  VAR
  Amount,  Duration, Payment, Interest,
  Balance, Time,  IntSum: INTEGER;
  Rate: REAL;
  PROCEDURE main();
  BEGIN
  (* Input  necessary information *)
  Write("Enter  amount of loan: ");
  Read(Amount);
  Write("Enter  payment amount: ");
  Read(Payment);
  Write("Enter the  duration in months: ");
  Read(Duration);
  WriteLn("Enter  annual interest rate ");
  Write("as a  decimal percent: ");
  Read(Rate);
  Rate :=  Rate/1200; (* Convert to monthly *)
  (* Compute the  Ballon Payment *)
  Balance :=  Amount;
  IntSum := 0;
  Time := 1;
  WHILE Time <  Duration DO BEGIN
  Interest :=  TRUNC(Balance * Rate);
  Balance :=  Balance + Interest;
  Balance :=  Balance - Payment;
  IntSum := IntSum  + Interest;
  Time := Time +  1;
  (* Begin trace  ************************)
  Write(Time);
  Write(" Balance  = ");
  WriteLn(Balance);
  (* End trace  **************************)
  END (* WHILE *)
  (* Output all  required Results *)
  Write("Balloon  Balance is: ");
  WriteLn(Balance);
  Write("Total  interest is : ");
  WriteLn(IntSum);
  END (* Loan *)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,277))
        

    def test_complex_278(self):
        input = """
  VAR Pennies:  INTEGER;
  Tendered, Cost,  Remainder: REAL;
  PROCEDURE Main();
  BEGIN
  (* Input  necessary information *)
  Write("Enter cost  of item: ");
  Read(Cost);
  Write("Enter  amount tendered: ");
  Read(Tendered);
  (* Compute the  change in pennies *)
  Remainder :=  Tendered - Cost;
  Pennies := 0;
  WHILE Remainder  > 0 DO BEGIN
  Remainder :=  Remainder - 0.01;
  Pennies :=  Pennies + 1;
  END (* WHILE *)
  (* Output all  required Results *)
  Write("Cost is:  ");
  Write(Cost);
  Write(" Amount  tendered is: ");
  Write(Tendered);
  Write(" Change  is: ");
  WriteLn(Pennies);
  END (*  BadChanger *)
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,278))
        

    def test_complex_279(self):
        input = """
  { An Extended  Payroll program
  }
  { Selection  nested in Else branch of outer
  Selection }

  VAR Hours, Pay: INTEGER;
  PROCEDURE main();
  BEGIN
  RegularRate := 10;
  ExtraRate := 15;
  DoubleRate := 20;
  BaseHours := 40;
  ExtraHours := 20;
  DoubleTimeStart  := BaseHours + ExtraHours;
  BasePay :=  RegularRate * BaseHours;
  ExtraPay :=  ExtraRate * ExtraHours;
  Write("Enter  hours");
  Read(Hours);
  WriteLn();
  IF Hours >  DoubleTimeStart THEN
  Pay := BasePay +  ExtraPay +
  DoubleRate *  (Hours -
  DoubleTimeStart);
  ELSE
  IF Hours <=  BaseHours THEN
  Pay :=  RegularRate * Hours;
  ELSE
  Pay := BasePay +
  ExtraRate *  (Hours -
  BaseHours);
  Write("The gross  pay is ");
  Write(Pay);
  WriteLn();
  END {  ExtendedPay }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,279))
        

    def test_complex_280(self):
        input = """
  { An Extended  Payroll program }
  { Decision  nested in Else branch of outer Decision }
  { Normal  indentation }
  VAR Hours, Pay: INTEGER;
  PROCEDURE main();
  BEGIN
  RegularRate := 10;
  ExtraIncrease :=  5;
  DoubleIncrease :=  5;
  BaseHours := 40;
  ExtraHours := 20;
  HoursInWeek := 7 * 24;
  DoubleTimeStart  := BaseHours + ExtraHours;
  Write("Enter  hours: ");
  Read(Hours);
  WriteLn();
  IF Hours >= 0  THEN { regular pay}
  Pay :=  RegularRate * Hours;
  IF Hours >  BaseHours THEN { add extra pay }
  Pay := Pay +  ExtraIncrease * (Hours - BaseHours);
  IF Hours >  DoubleTimeStart THEN { add double pay }
  Pay := Pay +  DoubleIncrease *
  (Hours - DoubleTimeStart);
  IF (Hours <  0) OR (Hours > HoursInWeek) THEN
  Pay := 0;
  WriteLn("The  gross pay is ", Pay);
  END {  NewExtendedPay }

        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,280))
        

    def test_random_281(self):
        input = """
procedure main();
begin
    writeln("71a1c003a2b855d85582c8f6c7648c49d3fe836408a7e1b5d9b222448acb3c1b");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 281))


    def test_random_282(self):
        input = """
procedure main();
begin
    writeln("27e1615212f3c6ea846ed6c412df1361ce97f006ee20bb5aa2483a3b61d5cadd");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 282))


    def test_random_283(self):
        input = """
procedure main();
begin
    writeln("e0850a775c17a87060c0cf6efad1020e0cbef5a44ba942bef6add5776598de53");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 283))


    def test_random_284(self):
        input = """
procedure main();
begin
    writeln("1e68ed4e3d58a51096a7feea3947f40debf1fd9246ec977eb62ab93c81823ad9");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 284))


    def test_random_285(self):
        input = """
procedure main();
begin
    writeln("a0d177b4967a6d99f4ff117defe1c0d23d4e78ca4630febcb948ee9e4520eff3");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 285))


    def test_random_286(self):
        input = """
procedure main();
begin
    writeln("00328ce57bbc14b33bd6695bc8eb32cdf2fb5f3a7d89ec14a42825e15d39df60");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 286))


    def test_random_287(self):
        input = """
procedure main();
begin
    writeln("d7cdaa5ca0582076c8e772cce739e32c5077cfd24f2ea33f04bb754594989a56");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 287))


    def test_random_288(self):
        input = """
procedure main();
begin
    writeln("23c657f2efda7731a3c1990b25f318fa2eb1332208f97ab9cc2a7eac70ab5a76");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 288))


    def test_random_289(self):
        input = """
procedure main();
begin
    writeln("af180e4359fc6179dc953abdcbdcaf7c146b53e1bee2b335e50dead11ccefa07");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 289))


    def test_random_290(self):
        input = """
procedure main();
begin
    writeln("09895de0407bcb0386733daa14bdb5dfa544505530c634334a05a60f161b71fc");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 290))


    def test_random_291(self):
        input = """
procedure main();
begin
    writeln("33512007840ced1bb0aab68f47cb5f702abd494a15f26bcbe26a1e47af03d841");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 291))


    def test_random_292(self):
        input = """
procedure main();
begin
    writeln("6db6eb4af1e18ab81d3878e44672185d60ca8c988c9e2f7783de220735534c33");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 292))


    def test_random_293(self):
        input = """
procedure main();
begin
    writeln("7cb676d57114874e00c536916e6dcad2a5d3cb8c9a5abc06335df359cd9a6ef9");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 293))


    def test_random_294(self):
        input = """
procedure main();
begin
    writeln("2cfc8ccbd7c0b17615323b41e815651ff2ae9ffae45a4599c0499b98ff940429");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 294))


    def test_random_295(self):
        input = """
procedure main();
begin
    writeln("9cfd3c755be26b4e1645918e2a64a26e3d851ede421e0b257f783b443bc443d1");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 295))


    def test_random_296(self):
        input = """
procedure main();
begin
    writeln("a0f8b2c4cb1ac82abdb37f0fe5203b97be556c4468c83bba18684d620fd8eaf9");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 296))


    def test_random_297(self):
        input = """
procedure main();
begin
    writeln("4c15f47afe7f817fd559e12ddbc276f4930c5822f2049088d6f6605bec7cea56");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 297))


    def test_random_298(self):
        input = """
procedure main();
begin
    writeln("76ebdb6d45c61ca12e622118cc90939ade672adf7890aa2b246405d4884dd75a");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 298))


    def test_random_299(self):
        input = """
procedure main();
begin
    writeln("308831041ea4863c3f87d222c31f759411898c874a9006b4bd6c745858b8f3bd");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 299))


    def test_random_300(self):
        input = """
procedure main();
begin
    writeln("983bd614bb5afece5ab3b6023f71147cd7b6bc2314f9d27af7422541c6558389");
end
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 300))

