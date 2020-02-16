#include<stdio.h>
#include<conio.h>

void main() {
   FILE *f;
   char s;
   clrscr();
   f=fopen("new.txt","r");
   while((s=fgetc(f))!=EOF) {
      printf("%c",s);
   }
   fclose(f);
   getch();
}
