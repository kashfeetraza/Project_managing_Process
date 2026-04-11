//#include<iostream>
//using namespace std;
//
//class bscs
//{
//    int roll;
//    int section;
//    public:
//     void setid(void){
//        cout<<"Enter The roll no. of student :";
//        cin>>roll;
//     }
//     void getid(void){
//        cout<<"The id of this student is "<<roll<<endl;
//
//     }
//};
//int main(){
//    bscs b[5];
//    for (int i = 0; i < 5; i++)
//    {
//        b[i].setid();
//        b[i].getid();
//    }
    
    
//    return 0;
//}



#include <iostream>
using namespace std;

class bankdeposit
{
    int principal_amount;
    int years;
    float interest_rate;
    float return_value;

    public:
     bankdeposit(){};
     bankdeposit(int p, int y ,float r);
     bankdeposit(int p, int y ,int r);
     void show(){
        cout<<"The amount was "<<principal_amount<<endl<<" return value after "<<years<<endl<<
        " is "<<return_value<<endl;
     }

};

bankdeposit ::   bankdeposit(int p, int y ,float r){
    principal_amount = p;
    years = y;
    interest_rate = r;
    return_value = principal_amount;
    for(int i=0;i<y;i++){
        return_value =return_value*(1+interest_rate);
    }
    
}

bankdeposit ::  bankdeposit(int p, int y ,int r){
    principal_amount = p;
    years = y;
    interest_rate = float(r)/100;
    return_value = principal_amount;
    for(int i=0;i<y;i++){
        return_value =return_value*(1+interest_rate);
    }
    
}
int main()
{
    bankdeposit fb1,fb2,fb3;
    int p,y;
    float r;
    int R;

    cout<<"Enter the amount p , y and r"<<endl;
    cin>>p>>y>>r;
    fb1 = bankdeposit(p ,y , r);
    fb1.show();

    cout<<"Enter the amount p , y and r"<<endl;
    cin>>p>>y>>R;
    fb2 = bankdeposit(p ,y , R);
    fb2.show();
    return 0;
}
