
 .def _subb
 .ref _d

 .data
w .word 0FFFFh, 0FFA9h, 8765h, 4320h

 .text
 .asg *SP(#0), var

_subb:
 PSH mmap(ST1_55)
 BSET SATA

 SUB T1, T0

 MOV mmap(ST0_55), T2

 AND 0x400, T2

 MOV T2, HI(AC0)

 SFTL AC0, #-11

 MOV HI(AC0), T2

 SUB T2, T0

 POP mmap(ST1_55)
 RET
