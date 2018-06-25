#include<stdio.h>
struct hotel
{
char item[20];
int qty;
float price;
};

void main()
{
struct hotel h[10];
int i=0,n=1,ch;
float amt,gst,tot=0;
do{
printf("Enter item name,quantity and price\n");
scanf("%s%d%f",h[i].item,&h[i].qty,&h[i].price);
printf("Next item [1/0]\n");
scanf("%d",&ch);
if(ch==1)
{
i++,n++;
}
}while(ch==1);
printf("\t\tHOTEL PARADISE\n");
printf("\t\t--------------\n");
printf("\tITEM\tQUANTITY\tPRICE\tAMOUNT\n");
for(i=0;i<n;i++)
{
amt=h[i].qty*h[i].price;
tot=tot+amt;
printf("\t%s\t%d\t\t%.2f\t%.2f\n",h[i].item,h[i].qty,h[i].price,amt);
}
gst=tot*18/100;
printf("\t\t\tTOTAL:%.2f\n",tot);
printf("\t\t\tGST:%.2f\n",gst);
printf("\t\t\tBILL:%.2f\n",tot+gst);
printf("\t\t**THANK YOU -- VISIT AGAIN**\n");
}
