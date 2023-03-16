#include <iostream>
#include <cstdlib>
#include <locale>
using namespace std;




int main(int argc, char** argv) {
	setlocale(LC_ALL, "Portuguese");
	
	string string;
	int n;
	
	cout<<"Insira uma String: " << endl;
	cin>> string;
	
	n= string.length();
	
	for(int i=n-1; i>=0; i--){
		cout<<string[i];
	}
	cout<<endl;
	
	
	return 0;
}
