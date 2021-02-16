#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <conio.h>
#include <windows.h>
#define TABLE_X 12  // 테이블 X축
#define TABLE_Y 16  // 테이블 Y축
#define LEFT 75     // 왼쪽으로 이동
#define RIGHT 77    // 오른쪽으로 이동
#define UP 72       // 시계방향 회전
#define DOWN 80     // 반시계방향 회전
#define SPACEBAR 32 // 아래쪽으로 이동

clock_t startDropT, endT, startGroundT;
int x = 8, y = 0; // 블럭의 위치
int nowblock;
int nxtblock;        // 블럭 모양 0~6
int blockVector = 0; // 블럭 방향
int key;
int level = 0;

void init();
void move(int x, int y);
void randomBlock();
int Check(int x, int y);
void dropBlock();
void blockToground();
void removeLine();
void drawMap();
void drawBlock();
void drawNxtblock();
void inputKey();

int block[7][4][4][4] = {
    // block[도형의 종류][도형의 방향]
    // block1
    {{{0, 0, 0, 0}, {0, 1, 0, 0}, {0, 1, 1, 1}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 1, 0, 0}, {0, 1, 0, 0}}, {{0, 0, 0, 0}, {1, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 1, 0}, {0, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}},
    // block2
    {{{0, 0, 0, 0}, {0, 0, 1, 0}, {1, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 1, 0, 0}, {0, 1, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 1, 1}, {0, 1, 0, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 1, 0}}},
    // block3
    {{{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}},
    // block4
    {{{0, 0, 0, 0}, {1, 1, 1, 1}, {0, 0, 0, 0}, {0, 0, 0, 0}}, {{0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 1, 0}}, {{0, 0, 0, 0}, {0, 0, 0, 0}, {1, 1, 1, 1}, {0, 0, 0, 0}}, {{0, 1, 0, 0}, {0, 1, 0, 0}, {0, 1, 0, 0}, {0, 1, 0, 0}}},
    // block5
    {{{0, 0, 0, 0}, {0, 1, 0, 0}, {1, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 1, 0, 0}, {0, 1, 1, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 1, 1}, {0, 0, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 1, 0}}},
    // block6
    {{{0, 0, 0, 0}, {0, 1, 1, 0}, {0, 0, 1, 1}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 0, 1, 0}, {0, 1, 1, 0}, {0, 1, 0, 0}}, {{0, 0, 0, 0}, {1, 1, 0, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 1, 0}, {0, 1, 1, 0}, {0, 1, 0, 0}, {0, 0, 0, 0}}},
    // block7
    {{{0, 0, 0, 0}, {0, 1, 1, 0}, {1, 1, 0, 0}, {0, 0, 0, 0}}, {{0, 1, 0, 0}, {0, 1, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 0, 1, 1}, {0, 1, 1, 0}, {0, 0, 0, 0}}, {{0, 0, 0, 0}, {0, 1, 0, 0}, {0, 1, 1, 0}, {0, 0, 1, 0}}}};
int table[TABLE_Y][TABLE_Y] = { // 테이블
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}};
int main()
{
    init();
    startDropT = clock();
    nxtblock = rand() % 7;
    randomBlock();
    while (1)
    {
        drawNxtblock();
        drawMap();
        drawBlock();
        dropBlock();
        blockToground();
        removeLine();
        inputKey();
        level++;
    }
    return 0;
}
void init()
{
    CONSOLE_CURSOR_INFO cursorinfo;
    cursorinfo.bVisible = 0;
    cursorinfo.dwSize = 1;
    SetConsoleCursorInfo(GetStdHandle(STD_OUTPUT_HANDLE), &cursorinfo);
    srand(time(NULL));
}
void move(int x, int y)
{
    COORD p;
    p.X = x;
    p.Y = y;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), p);
}
void randomBlock()
{
    nowblock = nxtblock;
    nxtblock = rand() % 7;
}
int check(int x, int y)
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (block[nowblock][blockVector][i][j] == 1)
            {
                int chk = table[i + y][j + x / 2];
                if (chk == 1 || chk == 2) // 벽일 때, 블럭일 때
                    return 1;
            }
        }
    }
    return 0;
}
void dropBlock()
{
    endT = clock();
    if ((float)(endT - startDropT) >= 800 - level / 1000)
    {
        if (check(x, y + 1))
            return;
        y++;
        startDropT = clock();
        startGroundT = clock();
        system("cls");
    }
}
void blockToground()
{
    if (check(x, y + 1))
    {
        if ((float)(endT - startGroundT) > 1000)
        {
            for (int i = 0; i < 4; i++)
            {
                for (int j = 0; j < 4; j++)
                {
                    if (block[nowblock][blockVector][i][j] == 1)
                    {
                        table[i + y][j + x / 2] = 2;
                    }
                }
            }
            x = 8;
            y = 0;
            randomBlock();
        }
    }
}
void removeLine()
{
    for (int i = 15; i >= 0; i--)
    {
        int cnt = 0;
        for (int j = 1; j < 11; j++)
            if (table[i][j] == 2)
                cnt++;
        if (cnt >= 10)
        {
            for (int j = 0; i - j >= 0; j++)
            {
                for (int x = 1; x < 11; x++)
                {
                    if (i - j - 1 >= 0)
                        table[i - j][x] = table[i - j - 1][x];
                    else
                        table[i - j][x] = 0;
                }
            }
        }
    }
}
void drawMap()
{
    move(0, 0);
    for (int i = 0; i < 16; i++)
    {
        for (int j = 0; j < 12; j++)
        {
            if (table[i][j] == 1)
            {
                move(j * 2, i);
                printf("□");
            }
            else if (table[i][j] == 2)
            {
                move(j * 2, i);
                printf("■");
            }
        }
    }
}
void drawBlock()
{
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (block[nowblock][blockVector][i][j] == 1)
            {
                move(x + j * 2, y + i);
                printf("■");
            }
        }
    }
}
void drawNxtblock()
{
    for (int i = 0; i < 6; i++)
    {
        for (int j = 1; j < 6; j++)
        {
            if (i == 0 || i == 5 || j == 5)
            {
                move(22 + j * 2, i);
                printf("□");
            }
        }
    }
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            if (block[nxtblock][0][i][j] == 1)
            {
                move(24 + j * 2, 1 + i);
                printf("■");
            }
        }
    }
}
void inputKey()
{
    if (_kbhit())
    {
        key = _getch();
        switch (key)
        {
        case UP: // UP
            blockVector++;
            if (blockVector >= 4)
                blockVector = 0;
            if (check(x, y))
                blockVector--;
            if (blockVector < 0)
                blockVector = 3;
            startGroundT = clock();
            break;
        case DOWN: // UP
            blockVector--;
            if (blockVector < 0)
                blockVector = 3;
            if (check(x, y))
                blockVector++;
            if (blockVector >= 4)
                blockVector = 0;
            startGroundT = clock();
            break;
        case LEFT: // lEFT
            if (check(x - 2, y) == 0)
            {
                x -= 2;
                startGroundT = clock();
            }
            break;
        case RIGHT: // RIGHT
            if (check(x + 2, y) == 0)
            {
                x += 2;
                startGroundT = clock();
            }
            break;
        case SPACEBAR: // down
            if (check(x, y + 1) == 0)
                y++;
            break;
        }
        system("cls");
    }
}