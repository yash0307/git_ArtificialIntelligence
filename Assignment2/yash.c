/**
	Yash Patel
**/
#include <stdio.h>
#include <limits.h>
int direction = 0;
float max(float a,float b,float c,float d)
{
	float max1 =a;
	direction =1;
	if(max1 < b)
	{
		max1 = b;
		direction =2;
	}
	if(max1 < c)
	{
		max1 = c;
		direction =3;
	}
	if(max1 < d)
	{
		max1 = d;
		direction =4;
	}
	return max1;
}
float Up(int i,int j,float Utility[4][3])
{
	if(i==0 && j==0)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[0][0] + 0.1*Utility[0][1];
	}
	if(i==0 && j==1)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[0][1] + 0.1*Utility[0][2];
	}
	if(i==0 && j==2)
	{
		return 0.1*Utility[0][2]+ 0.8*Utility[0][2] + 0.1*Utility[0][1];
	}
	if(i==1 && j==1)
	{
		return 0.1*Utility[1][0]+ 0.8*Utility[0][1] + 0.1*Utility[1][2];
	}
	if(i==1 && j==0)
	{
		return 0.1*Utility[1][0]+ 0.8*Utility[0][0] + 0.1*Utility[1][1];
	}

	if(i==1 && j==2)
	{
		return 0.1*Utility[1][1]+ 0.8*Utility[0][2] + 0.1*Utility[1][2];
	}
	if(i==2 && j==0)
	{
		return 0.1*Utility[2][0]+ 0.8*Utility[1][0] + 0.1*Utility[2][1];
	}
	if(i==2 && j==1)
	{
		return 0.1*Utility[2][0]+ 0.8*Utility[1][1] + 0.1*Utility[2][2];
	}
	if(i==2 && j==2)
	{
		return 0.1*Utility[2][1]+ 0.8*Utility[1][2] + 0.1*Utility[2][2];
	}
	if(i==3 && j==0)
	{
		return 0.1*Utility[3][1]+ 0.8*Utility[2][0] + 0.1*Utility[3][0];
	}
	if(i==3 && j==1)
	{
		return 0.1*Utility[3][0]+ 0.8*Utility[2][1] + 0.1*Utility[3][1];
	}
}
float Down(int i,int j,float Utility[4][3])
{
	if(i==0 && j==0)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[1][0] + 0.1*Utility[0][1];
	}
	if(i==0 && j==1)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[1][1] + 0.1*Utility[0][2];
	}
	if(i==0 && j==2)
	{
		return 0.1*Utility[0][2]+ 0.8*Utility[1][2] + 0.1*Utility[0][1];
	}
	if(i==1 && j==1)
	{
		return 0.1*Utility[1][0]+ 0.8*Utility[2][1] + 0.1*Utility[1][2];
	}
	if(i==1 && j==0)
	{
		return 0.1*Utility[1][0]+ 0.8*Utility[2][0] + 0.1*Utility[1][1];
	}

	if(i==1 && j==2)
	{
		return 0.1*Utility[1][1]+ 0.8*Utility[2][2] + 0.1*Utility[1][2];
	}
	if(i==2 && j==0)
	{
		return 0.1*Utility[2][0]+ 0.8*Utility[3][0] + 0.1*Utility[2][1];
	}
	if(i==2 && j==1)
	{
		return 0.1*Utility[2][0]+ 0.8*Utility[3][1] + 0.1*Utility[2][2];
	}
	if(i==2 && j==2)
	{
		return 0.1*Utility[2][1]+ 0.8*Utility[2][2] + 0.1*Utility[2][2];
	}
	if(i==3 && j==0)
	{
		return 0.1*Utility[3][1]+ 0.8*Utility[3][0] + 0.1*Utility[3][0];
	}
	if(i==3 && j==1)
	{
		return 0.1*Utility[3][0]+ 0.8*Utility[3][1] + 0.1*Utility[3][1];
	}

}
float Left(int i,int j,float Utility[4][3])
{

	if(i==0 && j==0)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[0][0] + 0.1*Utility[1][0];
	}
	if(i==0 && j==1)
	{
		return 0.1*Utility[0][1]+ 0.8*Utility[0][0] + 0.1*Utility[1][1];
	}
	if(i==0 && j==2)
	{
		return 0.1*Utility[0][2]+ 0.8*Utility[0][1] + 0.1*Utility[1][2];
	}
	if(i==1 && j==1)
	{
		return 0.1*Utility[0][1]+ 0.8*Utility[1][0] + 0.1*Utility[2][1];
	}
	if(i==1 && j==0)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[1][0] + 0.1*Utility[2][0];
	}

	if(i==1 && j==2)
	{
		return 0.1*Utility[0][2]+ 0.8*Utility[1][1] + 0.1*Utility[2][2];
	}
	if(i==2 && j==0)
	{
		return 0.1*Utility[1][0]+ 0.8*Utility[2][0] + 0.1*Utility[3][0];
	}
	if(i==2 && j==1)
	{
		return 0.1*Utility[1][1]+ 0.8*Utility[2][0] + 0.1*Utility[3][1];
	}
	if(i==2 && j==2)
	{
		return 0.1*Utility[1][2]+ 0.8*Utility[2][1] + 0.1*Utility[2][2];
	}
	if(i==3 && j==0)
	{
		return 0.1*Utility[2][0]+ 0.8*Utility[3][0] + 0.1*Utility[3][0];
	}
	if(i==3 && j==1)
	{
		return 0.1*Utility[2][1]+ 0.8*Utility[3][0] + 0.1*Utility[3][1];
	}

}
float Right(int i,int j,float Utility[4][3])
{
	if(i==0 && j==0)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[0][1] + 0.1*Utility[1][0];
	}
	if(i==0 && j==1)
	{
		return 0.1*Utility[0][1]+ 0.8*Utility[0][2] + 0.1*Utility[1][1];
	}
	if(i==0 && j==2)
	{
		return 0.1*Utility[0][2]+ 0.8*Utility[0][2] + 0.1*Utility[1][2];
	}
	if(i==1 && j==1)
	{
		return 0.1*Utility[0][1]+ 0.8*Utility[1][2] + 0.1*Utility[2][1];
	}
	if(i==1 && j==0)
	{
		return 0.1*Utility[0][0]+ 0.8*Utility[1][1] + 0.1*Utility[2][0];
	}

	if(i==1 && j==2)
	{
		return 0.1*Utility[0][2]+ 0.8*Utility[1][2] + 0.1*Utility[2][2];
	}
	if(i==2 && j==0)
	{
		return 0.1*Utility[1][0]+ 0.8*Utility[2][1] + 0.1*Utility[3][0];
	}
	if(i==2 && j==1)
	{
		return 0.1*Utility[1][1]+ 0.8*Utility[2][2] + 0.1*Utility[3][1];
	}
	if(i==2 && j==2)
	{
		return 0.1*Utility[1][2]+ 0.8*Utility[2][2] + 0.1*Utility[2][2];
	}
	if(i==3 && j==0)
	{
		return 0.1*Utility[2][0]+ 0.8*Utility[3][1] + 0.1*Utility[3][0];
	}
	if(i==3 && j==1)
	{
		return 0.1*Utility[2][1]+ 0.8*Utility[3][1] + 0.1*Utility[3][1];
	}
}
int main()
{
	float U[4][3]={0},Udash[4][3]={0};
	float p;
	printf("ENTER YOUR TEAM NUMBER\n");
	scanf("%f",&p);
	Udash[0][1]=p;
	Udash[1][0]=-1*p;
	int i,j;
	float k=0;
	while(k!=15)
	{
		printf("\nITERATION: %f\n",k);
		k++;
		for(i=0;i<4;i++)
		{
			for(j=0;j<3;j++)
			{
				U[i][j]=Udash[i][j];
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<3;j++)
			{
				if(i==0 && j==1)
					continue;
				if(i==3 && j==2 )
					continue;
				if(i==1 && j==0)
					continue;
				else		
				{	
					float q=max(Up(i,j,U),Down(i,j,U),Left(i,j,U),Right(i,j,U));
					Udash[i][j]=-1*p/20+q;
					if(k==9){
						if(direction==1)
							printf("UP");
						if(direction==2)
							printf("DOWN");
						if(direction==3)
							printf("LEFT");
						if(direction==4)
							printf("RIGHT");
						printf("\n");
					}
				}
			}
		}
		for(i=0;i<4;i++)
		{
			for(j=0;j<3;j++)
			{
				printf("%f  ",Udash[i][j]); 
			}
			printf("\n");
		}

	}
	return 0;
}