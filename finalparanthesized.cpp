#include<iostream>
using namespace std;
class stack{
    char s[25];
    int top;
    public:
    stack(){
        top=-1;
    }
    bool isempty(){
        return top==-1;
    }
    void push(char val){
        
        if(top<24){
            s[++top]=val;
        }
        else{
            cout<<"stack is full"<<endl;
        }
    }
    char pop(){
        if(!isempty()){
            return s[top--];
        }
        cout<<"empty"<<endl;
        cout<<'\0';
    }

};
class paranthesis{
    char expn[25];
    stack obj;
    public:
    void read(){
        cout<<"enter expression:";
        cin>>expn;
    }
    void checkexpn(){
        for (int i = 0; expn[i] != '\0'; i++) {
            if(expn[i]=='{' || expn[i]=='[' || expn[i]=='('){
                obj.push(expn[i]);
            }
            else if(expn[i]=='}' || expn[i]==']' || expn[i]==')'){
                char ch=obj.pop();
                if((expn[i]=='}' && ch!= '{') ||
                (expn[i]==']'  && ch!='[')||
                (expn[i]==')' && ch!='(')){
                    cout<<"exp not well"<<endl;
                    return;
                }
            }
            
        }
        if(obj.isempty()){
            cout<<"expression is paranthesized"<<endl;
        }
        else{
            cout<<"expression is not wp"<<endl;
        }
    }
};
int main(){
    paranthesis pnts;
    pnts.read();
    pnts.checkexpn();
    return 0;
}