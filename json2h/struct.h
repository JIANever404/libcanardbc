#ifndef _STRUCT_H_
#define _STRUCT_H_

typedef struct
{
    uint64_t signalname1;
    uint64_t signalname2;
    uint64_t signalname4;
} CarEngine;
#define CarEngine_signalname3 (0)
#define CarEngine_period (50)
#define CarEngine_msgid (1)

typedef struct
{
    uint64_t signalname5;
    uint64_t signalname7;
    uint64_t signalname8;
} CarDoor;
#define CarDoor_signalname6 (0)
#define CarDoor_period (100)
#define CarDoor_msgid (2)

typedef struct
{
    uint64_t signalname9;
} battery;
#define battery_signalname10 (0)
#define battery_period (2000)
#define battery_msgid (3)

#endif
