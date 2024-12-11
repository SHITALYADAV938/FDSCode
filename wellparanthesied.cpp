#include <iostream>
#include <stack>
#include <string>

using namespace std;

// Function to check if the given character is an opening parenthesis
bool isOpening(char ch) {
    return (ch == '(' || ch == '{' || ch == '[');
}

// Function to check if the given character is a closing parenthesis
bool isClosing(char ch) {
    return (ch == ')' || ch == '}' || ch == ']');
}

// Function to check if the opening and closing parentheses match
bool isMatchingPair(char opening, char closing) {
    return (opening == '(' && closing == ')') ||
           (opening == '{' && closing == '}') ||
           (opening == '[' && closing == ']');
}

// Function to check if the expression is well-parenthesized
bool isWellParenthesized(const string& expression) {
    stack<char> s;

    for (char ch : expression) {
        if (isOpening(ch)) {
            s.push(ch);
        } else if (isClosing(ch)) {
            if (s.empty() || !isMatchingPair(s.top(), ch)) {
                return false;
            }
            s.pop();
        }
    }

    // If stack is empty, all parentheses are balanced
    return s.empty();
}

int main() {
    string expression;

    cout << "Enter an expression: ";
    getline(cin, expression);

    if (isWellParenthesized(expression)) {
        cout << "The expression is well-parenthesized." << endl;
    } else {
        cout << "The expression is not well-parenthesized." << endl;
    }

    return 0;
}
