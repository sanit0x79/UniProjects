/* Concatenate multiple variables and literal strings
string firstName = "Bob";
string greeting = "Hello";
string message = greeting + " " + firstName + "!";
Console.WriteLine(message);
*/
/* Avoiding Intermediate variables
string firstName = "Bob";
string greeting = "Hello";
Console.WriteLine(greeting + " " + firstName + "!");
*/
/* String Interpolation
string firstName = "Bob";
string greeting = "Hello";
string message = $"{greeting} {firstName}!";
Console.WriteLine(message);
*/
/* Use string interpolation to combine a literal string and a var value
string firstName = "Bob";
string message = $"Hello {firstName}!";
Console.WriteLine(message);
*/
/* Use string interpolation with multiple variables and literal strings
int version = 11;
string updateText = "Update to Windows";
string message = $"{updateText} {version}";
Console.WriteLine(message);
*/
/* Avoid intermediate variables
int version = 11;
string updateText = "Update to Windows";
Console.WriteLine($"{updateText} {version}!");
*/ 
/* Combine verbatim literals and string interpolation
string projectName = "First-Project";
Console.WriteLine($@"C:\Output\{projectName}\Data");
*/

string projectName = "ACME";
string englishLocation = $@"c:\Exercise\{projectName}\data.txt";
Console.WriteLine($"View English output:\n\t\t{englishLocation}\n");

string russianMessage = "\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0443\u0441\u0441\u043a\u0438\u0439 \u0432\u044b\u0432\u043e\u0434";
string russianLocation = $@"c:\Exercise\{projectName}\ru-RU\data.txt";
Console.WriteLine($"{russianMessage}:\n\t\t{russianLocation}\n");

