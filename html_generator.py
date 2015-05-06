﻿MYNOTES = [
  <body>
  <h1>Introduction to Programming Notes</h1>
  <div class="lesson">
    <h2>Stage 1 - Lesson 1: The Basics of the Web and HTML</h2>
    <div class="concept">
      <div class="concept-title">
        How the Web Works
      </div>
      <div class="concept-description">
        <p>
          The Web is a system of interlinked, hypertext documents accessed through the Internet. It enables the retreival and display of text and media to your computer. The web is based on different technologies that make it possible for users to locate and share
          information through the Internet. These include Web browsers, hypertext Markup Language (HTML) and Hypertext Transfer Protocol (HTTP). To access webpages, you must use a Web browser usually referred to as a browser. Web browsers provide the
          software interface that enables you to use your mouse to click hyperlinked resources on the World Wide Web.
        </p>
      </div>
    </div>
    <div class="concept">
      <div class="concept-title">
        HTML
      </div>
      <div class="concept-description">
        <p>
          HTML stands for <em>Hypertext Markup Language.</em> It is the language of Web pages that tells a browser how to display certain elements, such as text and images through use of codes and symbols. HTML is standard when it comes to creating Web
          Pages that can be posted on the Internet. Since HTML is a markup langauge, you will need to know the various tags and elements it uses.
        </p>
      </div>
    </div>
    <div class="concept">
      <div class="concept-title">
        Tags and Elements
      </div>
      <div class="concept-description">
        <p>
          HTML documents are made of HTML <b>elements</b>. When writing HTML, we tell browsers the type of each element by using HTML <b>tags</b>. However, there is a difference when you refer to HTML elements and HTML tags. The differnce is that HTML
          documents contain only tags; but when they are accessed on a browser, the HTML documents are then parsed so that they can be displayed. The tags are there in the HTML document, but HTML elements appear after the document has been parsed. Simply
          put, HTML tags are the markup language that is used in HTML, these are generally the start or opening tag and the closing or ending tag. The tags are enclosed in angle brackets
          <>. HTML elements, on the other hand, include the content.
        </p>
      </div>
    </div>
    <div class="concept">
      <div class="concept-title">
        Why computers are Stupid
      </div>
      <div class="concept-description">
        <p>
          Computers are stupid because they interpret instructions literally. This makes them very unforgiving since a small mistake by a programmer can cause huge problems in a program. Programmers need to write <em>exactly</em> the way a computer understands
          (also known as correct "syntax").
        </p>
      </div>
    </div>
    <div class="concept">
      <div class="concept-title">
        Inline vs. Block Elements
      </div>
      <div class="concept-description">
        <p>
          HTML elements are either <b>inline</b> or <b>block</b>. A block-level element is an element that creates large blocks of content like paragraphs or page divisions. They start new lines of text when you use them, and can contain other blocks
          as well as inline elements and text data. An inline element is an element that defines text or data in the document. They don't start new line when you use them, and they generally only contain onther inline tags and text or data.
        </p>
      </div>
    </div>
    <div class="lesson">
      <h2>Stage 1 - Lesson 2: Creating a Structured Document with HTML</h2>
      <div class="concept">
        <div class="concept-title">
          Developer Tools (in the Browser)
        </div>
        <div class="concept-description">
          <p>
            Developer tools allows us to manipulate DOM elements, CSS Styles, JavaScript and other useful information from the same window often in real time. For instance, if a button isn't working or an image in the layout isn't in the right place, these tools
            help you resolve the issues. These tools are part of a browser in most cases.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          The "tree-like structure" of HTML
        </div>
        <div class="concept-description">
          <p>
            The "tree-like structure" comes from the fact that HTML elements can have other elements inside of them. A tree structure or tree diagram is a way of representing the hierarchical nature of a structure in a graphical form. It is named a "tree structure"
            because the classic representation resembles a tree, even though the chart is generally upside down compared to an actual tree, with the "root" at the top and the "leaves" at the bottom.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          The relationship between indented HTML and Boxes
        </div>
        <div class="concept-description">
          <p>
            Most HTML paragraphs don't have an initial identation. You can use <em>margin</em> or <em>padding</em> to push paragraphs to the right, but that affects the entire paragraph, not just the first line. The box model controls the area around
            text. All HTML elements can be considered boxes. In CSS, the term "box model" is used when talking about design and layout. The CSS box model is essentially a box that wraps around HTML elements, and it consits of: margins, borders, padding,
            and the actual content.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Text Editors (for programming)
        </div>
        <div class="concept-description">
          <p>
            A text editor is a program that helps you type text similar to document editors, such as Microsoft Word or Corel WordPerfect, but without all the extra formatting functions that document editors have. Note that technically you could use a text editor
            like Notepad, TextEdit, etc... As long as your file names end in .html your browser will know to read them as HTML. But these text editors are meant for writing documents for other people to read. They are notdesigned for writing computer
            code. Trying to use one of these text editors will be almost impossible.
          </p>
        </div>
      </div>
    </div>
    <div class="lesson">
      <h2> Stage 1 - Lesson 3: Adding CSS Style to HTML Structure</h2>
      <div class="concept">
        <div class="concept-title">
          Avoiding Repetition
        </div>
        <div class="concept-description">
          <p>
            Cascading Style Sheets known as CSS helps to create a uniform look across several pages on a web site. Instead of having to define each style for each block of text with a page of HTML, commonly used styles would only need to be defined once in a CSS
            document. Once the style has been defined in the style sheet, it can bused by any page that references that CSS file. This avoids code repetition throughout your document.
          </p>
          <p>
            <a href="https://developer.mozilla.org/en-US/docs/web/CSS/Reference">CSS Reference</a> pages can be found throughout the web giving you all of the CSS properties you can use. Think of CSS as adding style to headings too, similar to how we
            can do this in Word, giving headings different styles. In HTML you would identify each heading of your document by calling these tags as h1, h2, h3, etc. In addition, you can also add border boxes with the CSS Style Box Sizing border, this
            would make both the border and lay-out. I'm still a little lost on this part, so I'll have to do more research. For now I used basic border CSS styles.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          CSS
        </div>
        <div class="concept-description">
          <p>You can have several CSS files or sheets that will be referenced in HTML. All of them will be used to find out the visible style for your own web page. With CSS the most specific rule is applied to every element. The concept of most specific
            rule applies to cascading. You keep going down and down into the rules until you find the one that describes the element and then that rule is what gets applied. <a href="http://en.wikipedia.org/wiki/Cascading_Style_Sheets#Inheritance">Inheritance</a>            is a key feature in CSS.
          </p>
          In CSS you first write what is called a "selector" this defines what elements of the page a particular style will apply to. You can select an HTML tag and that rule will apply to all tags on the page. For example if you want to add a particular font to
          all the paragraphs this can be done by writing "p { }" within the style framework of CSS.
          </p>
          <p>
            Another way to add style is to select elements by class. For example if you want to write a style that applies to the class "description" this is done by typing ".description { }" and insert the attributes inside the bracket. In addition you define logical
            divisions within a document by adding the
            < div> element. This means that when you use a
              < div> element, you are indicating that the enclosed content is a specific section of the page. It is typically used to position portions of the page.
          </p>
        </div>
      </div>
    </div>
    <div class="lesson">
      <h2> Stage 2 - Lesson 1: Introduction to "Serious" Programming</h2>
      <div class="concept">
        <div class="concept-title">
          Programming and Computers
        </div>
        <div class="concept-description">
          <p>
            Programming is the core of computer science. Most machines are designed to do just one thing. Without a program a computer is less useful than let’s say a toaster. The program is what tells the computer what to do; and the power of the computer is that
            unlike a toaster, which is designed to only do a few things, a computer can do anything.
          </p>
          <p>
            A computer is a universal machine; we can program it to do essentially any computation. So anything that we can imagine, anything that we can figure out how to write a program for we can make the computer do; and what the program needs to be is a very
            precise sequence of steps. The computer by itself does not know how to do anything, it has a few simple instructions that it can execute; and to make a program do something useful we need to put those instructions together in a way that does
            what we want.
          </p>
          <p>
            So we can turn the computer into a web browser, a server, a game playing machine, almost into anything we can imagine – at least any computation that we want to do. The power of the computer is that it can execute those steps extremely fast, so we can
            execute billions of instructions in one second, the program gives us a way to tell the computer what steps to take.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Getting Started with Python
        </div>
        <div class="concept-description">
          <p>
            Programs give computers a precise sequence of steps to perform to execute mechanically.
          </p>
          There are many different languages for programming computers – the language we are going to learn in this course is a language which is called Python Programming Language. Python gives us a high level language that we can use to write programs and that
          means instead of our program running directly on the computer, the programs that we write will be the input to the Python program which runs on the computer.
          </p>
          <p>
            Why Python is – is called an interpreter-- that means it runs our programs, it interprets them, executes the program that we wrote in the Python language by running a program in a language that the computer can understand directly.
          </p>
          <p>
            There are two parts to the Python programming environment you will see in a web browser. The top part is an editor, where you can write and edit code. The bottom part is an output window, where you can see the results of running your code. We can see
            the value of something in Python by using print like this:
          </p>
          <div class="marginleft">
            <p>
              print 3
            </p>
          </div>
          <p>
            This prints out the value of 3. The expression after the print can be any value Python expression. Here are some examples:
            <ul class="a">
              <li>1+ 1 (addition)</li>
              <li>2 – 1 (substraction)</li>
              <li>2 * 6 (multiplication)</li>
            </ul>
          </p>
          <div class="concept-description">
            <p>
              We can compose expressions to make more complicated expressions like, 52 * 3 +12 * 9.
            </p>
            <p>
              We can also use parentheses to group expressions: (52 * 3) + (12 * 9) is different from 52 * (3 + 12) * 9. For example, this code prints out the the number of hours in a day: print 365 * 24 * 60 * 60
            </p>
          </div>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Programming Languages:
        </div>
        <div class="concept-description">
          <p>
            There are many reasons why a designed language like Python is better for writing programs than a natural language like English. One problem with natural languages is that they are ambiguous. Hence, not everyone will interpret the same phrase the same
            way. To program computers, it is important that we know exactly what our programs mean, and that the computer will run them with the meaning we intended. Another problem with natural language is that they are very verbose. To say something
            with the level of precision needed for a computer to be able to follow it mechanically would require an awful lot of writing. We want our programs to be short so it is less work to write them, and so that it is easier to read and understand
            them.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Grammar
        </div>
        <div class="concept-description">
          <p>
            Compared to a natural language, like English, programming languages like Python adhere to a strict grammatical structure. In English, even if a phrase is written or spoken incorrectly, it can still be understood with the help of context or other cues.
            On the other hand, in a programming language like Python, the code must match the language grammar exactly. The Python interpreter has no idea what to do with input that is not in the Python language, so it produces an error.
          </p>
          <p>
            Like English, Python has a grammar that defines what strings are in the language. In English we can make lots of sentences that are not completely grammatical and people still understand them, but there is some underlying grammar behind the language.
            English has rule that says you can make a sentence by combining a Subject w/a Verb followed by an Object. Almost every language has a rule sort of like this, the order of the subject, verb and object might be different, but there is a way
            to combine those three things to form a sentence. The subject could be a noun, the object could also be a noun, and the verb could be lots of other things (eat, like, etc.). All of this will allow us to write sentences from the parts of the
            words that we know.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Backus-Naur Form
        </div>
        <div class="concept-description">
          <p>The way we are writing grammar here is a notation called Backus-Naur Form, and this was invented by John Backus. John Backus was the lead designer of the Fortran programming language back in the 1950’s at IBM. This was one of the first widely
            used programming languages. And the way they describe the Fortan language was with lots of examples and text explaining what they meant. This worked ok and many programs were able to understand it and guess correctly what it meant but was
            not nearly precise enough and when it came time to design a later language which was the language called Algal it became clear that this informal way of describing languages wasn’t precise enough and John Backus invented the notation that
            we are using here to describe languages.
          </p>
          <p>
            The purpose of Backus-Naur form is to be able to precisely describe exactly the language in a way that’s very simple and very concise. So each role has the form like then where on the left side there is a non-terminal – this means something that we are
            not finished with.
          </p>
          <p>
            Once we get to a terminal we are done, we are finished, there is nothing else we can replace it with. So all the rules have this form
            <non-terminal>→replacement. We can form a sentence by starting with some form of “non-terminal” usually whichever one is written at the top left, and then by following the rules we keep replacing non-terminals with their replacements until we’re left with
              only terminals.
          </p>
          <p>
            The important thing about a replacement grammar is that we can describe an infinitely large language with a small set of precise rules. They python grammar is must stricter. In python the code must match the language grammar exactly.
          </p>
        </div>
      </div>
    </div>
    <div class="lesson">
      <h2>Stage 2 - Lesson 2: Variable and Strings</h2>
      <div class="concept">
        <div class="concept-title">
          Variable
        </div>
        <div class="concept description">
          If we used names to keep track of values instead of writing out big numbers – Python provides a way to do this, it’s called a “Variable.” We can use a variable to create a name and use that name to refer to a variable. So the way to introduce a variable
          is using an “Assignment Statement.”
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Assignment Statement
        </div>
        <div class="concept-description">
          <p>
            An Assigment Statement is is the name you give your expression: NAME = EXPRESSION. After the Assignment Statement, the name that is on the left side refers to the value that the expression has. The name can be any sequence of letter or numbers as well
            as underscores as long as it starts with a letter or an underscore. Here’s an example, we can create the name speed_of_light and we can assign to it the value of the speed of light in meters per second so after that assignment, the name speed
            of light refers to that value.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          String
        </div>
        <div class="concept-description">
          <p>
            A String is just a sequence of characters surrounded by quotes. It starts with a single quote, has a sequence of characters and anything we can type on the keyboard can be in a string and ends with another single quote. The String is the sequence of characters
            between the single quotes.
          </p>
          <p>
            If we want we can double quotes instead. If we use double quotes then the double quote starts the string, we can have a sequence of characters, and a double quote that ends the string. The only requirement is if we start the string with a single quote,
            it has to end with a single quote. If we start the string with a double quote it has to end with a double quote. And that is actually a handy property because that means we can have the other kind of quote within our string. The string would
            start with a double quote, it contains a single quote inside it but because we started with a double quote that single quote doesn’t end the string, that single quote is just like another character in the string. The string continues until
            the closing double quote.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Indexing Strings
        </div>
        <div class="concept-description">
          <p>
            So one of the things we can do with strings that we can’t do with numbers is we can extract sub-sequences from the strings. So remember what a string is – is a sequence of characters, if we have a string we can use the square brackets to extract parts
            of that string.
          </p>
          <p>
            So if we had the string ‘udacity’ and we use the square bracket with the value 0:
          </p>
          <p>
            ‘uadicity’ [0] - that would select the zero(est) character from the string, the characters of the string are indexed starting from zero, so the result of index 0 is the string with just the letter ‘U’ - - the expression inside the square bracket can be
            anything that evaluates to a number so we could have 1 + 1 in the brackets and 1 + 1 evaluates to the number 2 and at position two you would find the letter ‘A’ - so the value of this would be the string containing the single letter ‘A’.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Selecting Sub-Sequences
        </div>
        <div class="concept-description">
          <p>
            So there are lots more things we can do with strings, the next thing I’m going to talk about is selecting subsequences from strings. We’ve used indexing where we have a string, we have our square bracket, we have some expression that produces one number
            and we have our closed square bracket and that will give us the one-character string. At whatever position the number refers to in the string here.
          </p>
          <p>
            The other thing we can do with square brackets is select a sub-sequence of the string, instead of just having one expression here, what we can have is an expression, this also something that should evaluate to a number, followed by a colon, followed by
            another expression.
          </p>
          <p>
            Both of these expressions are numbers and this will evaluate to a string that is a subsequence of the characters in the input string. We’ll call the string ‘s’ , the value of first number we’ll call ‘start’ and the value of the second number we’ll call
            ‘stop’ – and what the result is – is a string that is a subsequence of all the characters in ‘s’ – in the string that we have here – starting from position ‘start’ , so the number to the left of the colon and ending with position stop but
            not including that character, so it’s going to really include the character from position ‘start’ up through ‘stop’ – 1. So this construct allows us to select from any string a subsequence of continuous characters in that string.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Finding Strings in Strings
        </div>
        <div class="concept-description">
          <p>
            So I want to introduce one more operation on strings which we’ll find very useful. Which is the find method. To find some substring that we're looking for. The way we use finds is a little different than we’ve used other operators so far because find
            is actually a method and what that means is a built in procedure provided by Python. We’ll be able to define our own procedures soon.
          </p>
          <p>
            FIND is a procedure that operates on strings so we use it by having a string followed by .find., followed by a parenthesis, and then we pass in another string, which is the string that we want to find in the first string and that output of find is the
            position in the string where that sub-string is found - - the first occurrence of the string - - so if that string happens to occur more places than one in the input string, the result of find is always going to give us the position that‘s
            the number where the first occurrence of the sub-string occurs.
          </p>
          <p>
            So the output of using FIND will be the first position in the search string where the target string occurs. So that would be a number. If the target string is not found anywhere in the search string then the output will be negative one.
          </p>
          <p>
            There is one other interesting thing we can do with find and going back to the original description of find, we said, well .find returns the first position, there might be other occurrences and we might want to find those other occurrences. The way to
            find those other occurrences we can actually pass in an extra parameter so instead of just passing in one string we can pass in a second parameter which is going to be a number so when we pass in a number what FIND will output is the number
            of the position in the search string where the target string appears the first occurrence after that position.
          </p>
          <p>
            We’ll give the first occurrence where the target string appears in the search string but starting from whatever position we pass in as a number. If we pass in 0 it would start from the beginning that would mean the same thing as the original find, if
            we pass in the position later down the line, it would start from there and would still output the same value we found before – if we start right after that then it wouldn’t find the occurrence because this occurrence starts after that position,
            it would go to the next target.
          </p>
        </div>
      </div>
    </div>
    <div class="lesson">
      <h2>Stage 2 - Lesson 3: Input>Function>Output</h2>
      <div class="concept">
        <div class="concept-title">
          A Function is a Procedure
        </div>
        <div class="concept-description">
          <p>
            How do functions take input and produce output and what role do the keywords def and return have to do with this process? We haven’t really talked about how to use a procedure, until we can actually make them until we can actually use them.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Using Procedures
        </div>
        <div class="concept-description">
          <p>
            The way to use a procedure we need the name of the procedure, followed by a left paren., followed by a list of inputs and there could be any number of inputs but it has to match the number of inputs the procedure expects. These inputs are sometimes called
            operands, they are sometimes called arguments– but we are just going to call them inputs.
          </p>
          </p>
          So we have actually done something quite similar to this in unit 1 we used find on strings and with find you would pass in one or two inputs, the first input was a string, that was the string you were looking for, that’s the first input, and the second
          input could be a number, the position where you start looking for that string. And so we use find in many ways in unit one as well you used it yourself in the homework for unit 1.
          </p>
          <p>
            Find is a little different from the procedures that you define yourself. First of all it’s built in. The other thing that was different is that instead of just having .find we had another input that was the string we were doing the .find in, let’s say
            it was in the variable “page” that’s really another input to .find – we’ll talk in a later class about why that is done differently but it’s very similar to calling a procedure where one of the inputs is on the left the other two on the right
            - - it’s a different from that and we won’t get into that in this course but in a later course we’ll learn more about what this really means. For all the procedures that you define yourself we won’t have any object invoked in one, we’ll just
            have the procedure to call and the arguments, or operand, or inputs to pass in.
          </p>
          <p>
            So let’s see how that works with a simple procedure, I’m going to define the procedure rest of string, and we’ll give it the parameter (s) so that means it takes one input and we are going to use the name (s) to refer to the value of that input and we’ll
            make it return a string from the first character to the end, so we’ll use the string indexing operator return s[1:], this will evaluate it to the string with the first letter removed so all string from the position 1 until the end of the string
            - - and that’s what will return, so that’s the output of “rest of string” is that new string that starts from the second letter from the input string because we used s[1] and remember we start with 0, 1, 2, etc. so 1 is the second letter.
          </p>
          <p>
            Here’s an example of how to use this particular procedure so we could call it directly, we could say:
          </p>
          <p>
            Print rest_of_string -- (so that is our procedure) – now we are going to have our paren. and we are going to pass in an input – there is one parameter in the rest_of_string so we need one input path to pass in and it should be a string so we’ll pass in
            the string (‘audacity’).
          </p>
          <p>
            What happens when we call a procedure like this is that execution will jump into the body of the procedure so we can think of what the interpreter is doing now instead of running code on the “rest_of_string” it will move, it will jump to run the code
            inside the procedure it will assign to the parameters the values passed in as the inputs so we can think of this as there being an assignment that is now the value of ‘s’ is the value of the input that was passed in (‘audacity’) and now we
            are going to evaluate the body of the procedure.
          </p>
          <p>
            In this case there is only one statement which is the return statement, we’re going to find the value s[1:], the result of that is going to be the string ‘udacity’ and then we got to the return what return means is where we are going to jump back. We
            are going to jump back to where we called the procedure but now we actually have a result. So when we jump back , the value of whatever the rest_of_string(‘audacity’) evaluates to, is whatever value we returned. In this case it is the string
            ‘udacity.’
          </p>
          <p>
            Now we can define and use procedures. This is a very powerful concept anything that anyone does in programming computers is all about defining procedures and using procedures. We can think of our procedures in terms of mapping inputs to outputs.
          </p>
        </div>
      </div>
    </div>
    <div class="lesson">
      <h2>Stage 2 - Lesson 4: Control Flow & Loops: If and While</h2>
      <div class="concept">
        <div class="concept-title">
          Equality Comparisons
        </div>
        <div class="concept-description">
          <p>
            We are going to make code behave a different way based on decisions. The first thing is to figure out how we are going to make comparisons, so we have a way to test and decide what we should do. Python provides lots of different operators for providing
            comparisons. ul class = "a">
            <li>
              < (Less than sign) </li>
                <li>> (Greater than sign)</li>
                <li>
                  <=( Less than or equals to)</li>
                    </ul>
          </p>
          <p>
            All of these operate on numbers so we can have a
            <number> followed by a comparison operator, followed by another number. The output would be a Boolean value, it’s either that value TRUE or the value FALSE.
          </p>
          <h3>Equality Comparison Examples</h3>
          <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/254906/Lesson_2.4_Equality_Comparisons.png" alt="Equality Comparison Ex" style="width:304px;height:228px">
          </p>
          <p>
            <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/254906/Lesson_2.4_Equality_Comparisons_Test_Run.png" alt="Equality Comparison Test Run" style="width:304px;height:228px">
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          If Statements
        </div>
        <div class="concept-description">
          <p>Now that we can make comparisons, we want to use them to make decisions, to make our code do something different depending on the result of the comparison the way to do that is to use an “If” statement.
          </p>
          <p>
            The structure of an “if” statement is we have the key word IF, followed by a comparison, we’ll call that the
            <Test Expression>: (followed by a colon). Inside the “if” we have the BLOCK, and the block is the code that will run when the test expression is true. If the test expression doesn’t evaluate to true then the block doesn’t execute and similar to the “procedure”
              definitions, we know the end of the “IF” because of indentation. All of the statements inside of the “block” are executed only when the test expression is true, the next statement that is not indented is going to be executed whether or not
              the test expression is true.
          </p>
          <p>
            See example: We are going to define a procedure = absolute, it will take one input which is going to be a number, and then inside the body of “absolute” we are going to use an “if” statement , we’ll use an “if” test where we are testing if the value of
            “x” is less than “0” – and then in the block we are going to have one statement which changes the value of “x” to be “-x” -- the next statement, which will happen after the “if” will return “x” (depending on whether the test was true of false)
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Control Flow & Loops: If and While > OR
        </div>
        <div class="concept-description">
          <p>
            If the first expression evaluates to TRUE, the value is TRUE and the second expression is not evaluated. If the first expression evaluates to FALSE, the value is the value of the second expression.
          </p>
          <p>
            <b> < Expression > </b> OR <b>< Expression > </b>
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Control Flow & Loops: If and While > While Loops
        </div>
        <div class="concept-description">
          <p>
            New construct we are going to learn is Loops, is to do thing over and over again. The first loop is the WHILE loop – key word “while” followed by a
            <test expression> (followed by a colon): -- then inside we have a
              <block> and the block is a sequence of instructions, very similar to the “if” statement. With the “if” statement the block expression will execute 0 or 1 times; however, with the “while” statement the block can execute any number of times, it keeps
                going as long as the test expression is true.
          </p>
          <p>
            Example:
          </p>
          <p>
            Initializing the variable “i” = we give it the value 0.
          </p>
          <p>
            Then we have the “while” and the test expression says i
            < 10=s o that means that as long as this evaluates to true, we’ll evaluate the block and what the block does is print i and then adds 1 to i. </p>
              <p>
                <img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/254906/Lesson_2.4_While_Loops.png" alt="While Loops" style="width:304px;height:228px">
              </p>
              <p>
                So then we evaluate i and we see that i is less than 10. Which means the test expression is True (i &lt; 10), from there we’ll enter the block – and print "i" - - so we’ll see the value of “0” printed since i = 0. From there we'll do the assignment so
                we are saying 0 = 0+1 which is 1 – now if it was an “if” statement we would stop; but because this is a “while” statement we keep going -- we go back and test again to see if i is less than 10 but now the value of i is 1. Which is also
                1 &lt; 10, so we continue, but when we print i the next time we’ll see the value of 1, we go back and test again, this time making the value of i to 1 which would then make it 2. Keep going back to the expression, over and over again until
                you reach the test expression 10 &gt; 10 which would result in a false statement, and from there you are done with the loop.
              </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Control Flow & Loops: If and While > Block Statements
        </div>
        <div class="concept-description">
          <p>
            One more thing to learn about “why” loops, and that’s the Break statement - - “break” gives us a way to stop the loop even while the test condition is true. Typical structure of a loop with a break:
          </p>
          <p>
            <b> while &lt;test expression></b>: &lt;Block&gt; --- {we are going to look inside this block to see what kinds of thing could be here}
          </p>
          <p>
            &lt;Block&gt;: it could be &lt;code> and then an “if” statement and that will have another test expression and that’s where we’ll call that the “Break Test” -- that’s a test expression that’s checking whether or not it’s time to take a break and when
            the “break test” is true what we have is “break” - - which by itself is all we need. What “break” means is stop executing the “why” loop, jump up and continue with the code after that.
          </p>
          <pre>
        def print_numbers (n):		
        i = 1				 
        while  i = &lt;n:			     
           print  I			          
           i = i + 1			
				
        def print_numbers (n):
         i = 1
            while True: 
              if i > n:
               break
               
        print i
        i = i + 1
    </pre>
          </p>
        </div>
      </div>
    </div>
    <div class="lesson">
      <h2>Stage 2 - Lesson 5: Debugging</h2>
      <div class="concept">
        <div class="concept-title">
          What is a Bug?
        </div>
        <div class="concept-description">
          <p>
            Sometimes when you try something in code it just doesn’t work the first time, these errors are called bugs. We need to develop a strategy to systematically getting rid of bugs. It’s about building a correct mental model of how that system works so that
            you can find out what isn’t working.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Examine Error Messages
        </div>
        <div class="concept-description">
          <p>
            Sometimes it’s really obvious that the code has a bug, because the bug makes the code crash; and when it crashes it usually gives some kind of error message. Error messages can be confusing, but they do give some kind of information besides “it didn’t
            work – try something different.”
          </p>
          <p>
            Specifically, when Python code crashes the message it gives is called a “Traceback.” The Traceback tells you what line it crashed on, what file it was running, and it got there. The information Traceback gives you especially the line number and function
            name can focus your attention on the part of the code that might be going wrong even if the root of that problem isn’t on that exact line it’s somewhere upstream of that line.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Work from a Working Example
        </div>
        <div class="concept-description">
          <p>
            You can look at example code to give you a model of what to write, then you can write code that is based on the example code but you can change it to do what you want it to do. Make random changes until it works, but If that doesn’t work then simple copy
            and paste the sample code replacing your code within the sample code, then go and find out where the bug was in your original code.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Making Sure the Examples Work
        </div>
        <div class="concept-description">
          <p>
            When working with example code, you do have to exercise with some care or you could inherit bugs from the sample code. Sometimes the example work didn’t work to begin with so in that case your code would have never of worked. You can find out why it didn’t
            work or else find a better example.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Check Intermediate Results
        </div>
        <div class="concept-description">
          <p>
            Bugs that don’t crash your program can be a lot trickier than the ones that do when a function calculates an incorrect value finding out where it went wrong often involves splitting the function up into smaller pieces and looking what the values are and
            variables in each of those pieces. One basic way to do this is to introduce print statements that output the variables where you can see them. Once you have done debugging in this fashion, remember to take the print statements out.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Keep and Compare Old Versions
        </div>
        <div class="concept-description">
          <p>
            If you have something almost but not quite working and you are getting frustrated, you may want to throw it away and try again. Sometimes you are close on your first try and your second try isn’t as close, then you want to be able to get back to the first
            version. For short functions, you can make this easier by commenting out the old version. In Python, just put a hash mark before each line of the function or you can turn it into a big string by putting triple quotes (' ’ ’) around it. Text
            editors do have an undo feature but it doesn’t usually let you go back between multiple different versions of your code so it’s not really good enough to let you compare different versions of code. Undo is good for when you accidentally mess
            something up and immediately notice, but you can’t rely on undo alone to compare different versions of code or to get back to a previous version you had.
          </p>
        </div>
      </div>
    </div>
    <div class="lesson">
      <h2>Stage 2 - Lesson 6: Structured Data: Lists & For Loops</h2>
      <div class="concept">
        <div class="concept-title">
          Strings and Lists
        </div>
        <div class="concept-description">
          <p>
            The closest thing you have seen to structured data so far is the <b>string</b> type introduced in Unit 1, and used in many of the procedures in Unit 2. A string is considered a kind of structured data because you can break it down into its
            characters and you can operate on sub-sequences of a string. This unit introduces <b>lists</b>, a more powerful and general type of structured data. Compared to a string where all of the elements must be characters, in a list the elements
            can be anything you want such as characters, strings, numbers or even other lists. The table below summarizes the similarities and differences between strings and lists.
          </p>
          <IMG class="displayed" img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/254906/Lesson_2.6_String_and_Table_List.png" alt="String and List Table" style="width:320px;height:220px">
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Nested Lists
        </div>
        <div class="concept-description">
          <p>
            So far, all of the elements in our lists have been of the same type: strings, numbers, etc. However, there are no restrictions on the types of elements in a list. Elements of a list can be any type you want, you can also mix and match different types
            of elements in a list.
          </p>
          <IMG class="displayed" img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/254906/Lesson_2.6_Nested_Lists_example_1.png" alt="Nested List example1" style="width:320px;height:220px">
          </p>
          <p>
            This list provides information about the names of the Beatles band members, as well as when they were born. Try putting this into your interpreter. When you are typing your code into the interpreter and you want to separate data onto two lines, do so
            after a comma to make it clear to the interpreter that this is still one list.
          </p>
          <IMG class="displayed" img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/254906/Nested_Lists_ex2.png" alt="Nested List example2" style="width:320px;height:220px">
          </p>
          <p>
            You can also use indexing again on the list that results to obtain an inner element:
          </p>
          <IMG class="displayed" img src="https://s3-us-west-2.amazonaws.com/s.cdpn.io/254906/nested_list_ex3.png" alt="Nested List example3" style="width:220px;height:120px">
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Mutation
        </div>
        <div class="concept-description">
          <p>
            <b>Mutation</b> means changing the value of an object. Lists support mutation. This is the second main difference between strings and lists.
          </p>
          <p>
            It might have seemed like we could change the value of strings:
            <br>
            <br> s = '<b>H</b>ello'
            <br> s = '<b>Y</b>ello'
          </p>
          <p>
            However, this expression changes the value the variable s refers to, but does not change the value of the string 'Hello'. As another example, consider string concatenation: s = s + '<b>w</b>'
          </p>
          <p>
            This operation may look like it is changing the value of the string, but that's not what happens. It is not modifying the value of any string, but instead is creating a new string, 'Yellow', and assigning the variable s to refer to that new string.
          </p>
          <p>
            Lists can be mutated, thus changing the value of an existing list. Here is a list: p = ['<b>H</b>', 'e', 'l', 'l', 'o']
          </p>
          <p>
            Mutate a list by modifying the value of its elements: p[0] = '<b>Y</b>'
          </p>
          <p>
            This expression replaces the value in position 0 of p with the string 'Y'. After the assignment, the value of p has changed:
            <br>
            <br> print p ['Y', 'e', 'l', 'l', 'o']
            <br> p[4] = '!'
            <br> print p
            <br> ['Y', 'e', 'l', 'l', '!']
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          Aliasing
        </div>
        <div class="concept-description">
          <p>
            Now that you know how a mutation modifies an existing list object, you will really be able to see how this is differs from strings when you introduce a new variable.
          </p>
          <p>
            p = ['H', 'e', 'l', 'l', 'o']
            <br> p[0] = 'Y'
            <br> q = p
          </p>
          <p>
            After this assignment, p and q refer to the same list: ['Y', 'e', 'l', 'l', 'o'].
          </p>
          <p>
            Suppose we use an assignment statement to modify one of the elements of
          </p>
          <p>
            q:5
            <br> [4] = '!'
          </p>
          <p>
            This also changes the value of p:
          </p>
          <p>
            print p
            <br> ['Y', 'e', 'l', 'l', 'o']
          </p>
          <p>
            After the q = p assignment, the names p and q refer to the same list, so anything we do that mutates that list changes that value both variables refer to.
          </p>
          <p>
            It is called aliasing when there are two names that refer to the same object. Aliasing is very useful, but also can be very confusing since one mutation can impact many variables. If something happens that changes the state of the object, it affects the
            state of the object for all names that refer to that object.
          </p>
          <p>
            <b>Strings are Immutable</b>. Note that we cannot mutate strings, since they are immutable objects. Try mutating a string in the interpreter:
          </p>
          <p>
            s = 'Hello'
            <br> s[0] = 'Y'
            <br>
            <em> 'str' object does not support item assignment</em>
          </p>
          <p>
            <b>Mutable and Immutable Object</b>. The key difference between mutable and immutable objects, is that once an object is mutable, you have to worry about other variables that might refer to the same object. You can change the value of that
            object and it affects not just variable you think you changed, but other variables that refer to the same object as well.
          </p>
          <p>
            Here is another example:
          </p>
          <p>
            p = ['J', 'a', 'm', 'e', 's']
            <br> q = p
            <br> p[2] = 'n'
          </p>
          <p>
            Both p and q now refer to the same list: ['J', 'a', 'n', 'e', 's']. What happens if you assign p a new value, as in: p = [0, 0, 7].
          </p>
          <p>
            In this case, the value of p will change, but the value of q will remain the same. The assignment changes the value the name p refers to, which is different from mutating the object that p refers to.
          </p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          List Operations
        </div>
        <div class="concept-description">
          <p>
            <b>Append:</b> The append method adds a new element to the end of a list. The append method mutates the list that it is invoked on, it does not create a new list. The syntax for the append method is: &lt;list>.append(&ls;element>)
          </p>
          <p>
            For example, assume you want to end up with four stooges in your list, instead of just three:
            <br> stooges = ['Moe', 'Larry', 'Curly']
            <br> stooges.append('Shemp')
            <br> ['Moe', 'Larry', 'Curly', 'Shemp']
          </p>
          <p>
            <b>Concatenation.</b> The + operator can be used with lists and is very similar to how it is used to concatenate strings. It produces a new list, it does not mutate either of the input lists.
            <br>
            <b>&lt;list> + &lt;list> → &lt;list></b>
          </p>
          <p>
            For example: 7
            <br> [0, 1] + [2, 3] → [0, 1, 2, 3]
          </p>
          <p>
            <b>Length.</b> The len operator can be used to find out the length of an object. The len operator works for many things other than lists, it works for any object that is a collection of things including strings. The output from len is the
            number of elements in its input.
            <br> len(&lt;list>) → &lt;number>
          </p>
          <p>
            For example, len([0,1]) → 2. Note that len only counts the outer elements:
            <br> len(['a', ['b', ['c', 'd']]]) → 2
            <br> since the input list contains two elements: 'a' and ['b', ['c', 'd']].
          </p>
          <p>
            When you invoke len on a string, the output is the number of elements in the string.
            <br> len("Udacity") → 7
          </p>
          <p>
        </div>
      </div>
      <div class="concept">
        <div class="concept-title">
          For Loops
        </div>
        <div class="concept-description">
          <p>
            In Python there is a more convenient way to loop through the elements of a list: the for loop. The syntax looks like this:
            <br> for <b>&lt;name></b> in <b>&lt; list></b>:
            <br>
            <b>&lt;block></b>
          </p>
          <p>
            The loop goes through each element of the list in turn, assigning that element to the <b>&lt;name></b> and evaluating the <b>&lt;block></b>. Using the for loop, we can use less code than we needed using the <em>while</em> loop to define the
            procedure print_all_elements:
            <br> def print_all_elements(p):
            <br> for e in p:
            <br> print e
          </p>
          <p>
            Let's walk-through what happens when you apply this for loop to a list:
            <br> mylist = [1, 2, 3]
            <br> print_all_elements(mylist)
          </p>
          <p>
            When you pass in mylist to print_all_elements the variable p will refer to the list that contains the three elements, 1, 2 and 3. When the loop is executed, the variable e is assigned to the first element in the list, and the body of the loop will print
            the first element. So, for the first iteration the value of e will be 1. The block is executed, printing out 1. Since there are more elements in the list, execution continues, assigning 2 to the e. Again, the block is executed, but this time
            it prints out 2. Execution continues for the third iteration, which prints out 3. There are no more elements in the list, so the for loop is complete and execution continues with the next statement (in this case, there is no following statement,
            so execution finishes).
          </p>
        </div>
      </div>
      <div>
        <div class="lesson">
          <h2>Stage 2 - Lesson 7: How to Solve Problems</h2>
          <div class="concept">
            <div class="concept-title">
              Understanding a Problem
            </div>
            <div class="concept-description">
              <p>
                Understanding a Computational Problem: What all computational problems have in common is that they have inputs and they have desired outputs.
              </p>
              <p>
                A problem is defined by a set of possible inputs (usually an infinite set) and the relationship between those inputs and the desired outputs. So that means a solution to a problem is a PROCEDURE that can take any input in that SET and produce as output,
                the desired output that satisfies the relationship that we want.
              </p>
              <p>
                In the above problem the output is the number of days between the birthday and the current day. So the first step in understanding a problem is to ensure that we know what the possible inputs are.
              </p>
            </div>
          </div>
          <div class="concept">
            <div class="concept-title">
              Rules to Solving Problems
            </div>
            <div class="concept-description">
              <p>Rule 1: Always ask: What are the inputs? How are inputs represented?
              </p>
              <p>
                Rule 2: What are the outputs? Think about who the output should be specified and can we do more computations with the output.
              </p>
              <p>
                Rule 3: Solve the Problem. We have the inputs and outputs, but to see if we understand the relationship of the problem and will work it with examples. Consider systematically how a human would solve the problem.
              </p>
            </div>
          </div>
          <div class="concept">
            <div class="concept-title">
              Algorithm Pseudo Code
            </div>
            <div class="concept-description">
              <p>
                We can write down an Algorithm that will systematically solve the problem. This will be written as “pseudo code” - - this means we will not be worrying about the details of how to write exactly correct python. We are trying to get the idea down and see
                if it makes sense.
              </p>]
htmlcode = MYNOTES
def get_title(concept):
    start_location = concept.find('title:')
    end_location = concept.find('description:')  
    title = concept[start_location+len('title:') : end_location-1]
    return title
         
def get_description(concept):
    start_location = concept.find('description:')  
    description = concept[start_location+len('description:'):]
    return description
         
def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept):
    start_location = concept.find('TITLE:')
    end_location = concept.find('DESCRIPTION:')
    title = concept[start_location+7 : end_location-1]
    return title

def get_description(concept):
    start_location = concept.find('DESCRIPTION:')
    description = concept[start_location+13 :]
    return description

print htmlcode
