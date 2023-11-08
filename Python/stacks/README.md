# Stack Data Structure

## A Basic Stack

You should implement a `Stack` that offers the following functions:

* `push` adds an element to the top of the stack
* `pop` removes and returns the top element of the stack

Beyond those most essentials, implement the following:

* `count` returns the number of elements on the stack
* `peek` returns the value of the top element without removing it
* `empty` returns a true if the stack is empty, false if not

### Implementation Challenge

Your implementation language might already have a `Stack` data structure or `Array` functions that do all the hard work for you.

But what if, instead of using those, you implemented your `Stack` using a `LinkedList`?

It would be wise to implement once the easy way to make sure you understand everything, then reimplement using the `LinkedList`.

## Stack in Practice

Now that you understand how a `Stack` works we can apply it to a common technical challenge, matching elements.

### Well-Formed Strings, Round 1

You are given a string made up entirely of open and close parentheses, like this: `(()()())()`

Implement a `validate` method that returns `true` if the parentheses are properly nested, `false` if not. Proper nesting means:

* Each open `(` has a matching close `)`

### Well-Formed Strings, Round 2

In Round 2, build on your implementation from Round 1 with these additional expecations:

* The strings contain parentheses (`(` and `)`), square brackets (`[` and `]`), and curly braces (`{` and `}`)
* Each open must have a matching close of the same type
* Types may not be interleved, so `(){}` is valid but `({)}` is not
* Any characters in the string other than these six are ignored

### HTML/XML Parsing

Take this concept and apply it to a basic HTML parser.

#### Level 1

Given a test string made up of a paragraph, ensure it has:

* An opening `<p>` and a closing `<p>`
* Any opening `<span>` has a closing `</span>`
* Any opening `<code>` has a matching `</code>`

#### Level 2

Given a test string of the body of an HTML page, ensure it:

* An opening `<body>` and matching `</body>`
* Any opening `<p>` has a matching `</p>`
* Any opening `<ul>` or `<ol>` has a matching `</ul>` or `</ol>`
* Any opening `<li>` has a matching `</li>`
* And covers the tags from Level 1

#### Level 3

Now consider deeper context for validity:

* The string must start and end with the `body` tags
* `span` and `code` tags must appear inside a `p` or `li`
* `li` must appear inside an `ul` or `ol`
* `ul` and `ol` must be inside the body but not inside a `p`
* One or more `p` blocks may appear inside a `li`