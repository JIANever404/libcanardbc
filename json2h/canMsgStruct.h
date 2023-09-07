#ifndef _CANMSGSTRUCT_CANSTRUCT_H
#define _CANMSGSTRUCT_CANSTRUCT_H

typedef struct
{
    unsigned long long signalname1;
    unsigned long long signalname2;
    unsigned long long signalname4;
} CarEngine_canVal;
#define CarEngine_canVal_period (50)
#define CarEngine_canVal_msgid (1)

typedef struct
{
    unsigned long long signalname5;
    unsigned long long signalname7;
    unsigned long long signalname8;
} CarDoor_canVal;
#define CarDoor_canVal_period (100)
#define CarDoor_canVal_msgid (2)

typedef struct
{
    unsigned long long signalname9;
} battery_canVal;
#define battery_canVal_period (2000)
#define battery_canVal_msgid (3)

typedef struct
{
    unsigned long long signalname9;
    unsigned long long signalname10;
} something_else_canVal;
#define something_else_canVal_period (10000)
#define something_else_canVal_msgid (4)

#endif
