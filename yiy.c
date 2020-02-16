#include <stdio.h>

struct cell{
  char name[40];
  int finger_num[10];
  int leg_fin_num[10];
  char *cool_ptr;
}body;

int main(void){
  char n,c;
  int f,l;
  char cool[] = {"dasai","soso","cool","best"};
  body.cool_ptr = cool;

  printf("名前を入力してください");
  scanf("%s\n", body.name);

  while((n = getchar()) !=EOF){
    (//構造体に入力値をメンバーの名前として代入//)
    if (n = "\n"){
      return 0;
    }
    return 0;
  }

  printf("手の指の合計数を入力してください");
  scanf("%d\n", body.finger_num);
  printf("足の指の合計数を入力してください");
  scanf("%d\n", body.finger_num);
  printf("あなたのかっこよさを4段階で評価してください");
  scanf("%s\n", cool);


}
