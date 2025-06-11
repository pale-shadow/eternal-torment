.data
ayy: 
  .string "ayy\n"
lmao: 
  .string "lmao\n"

.global main
main: 
  movl	$SYS_write,%eax
  movl	$STDOUT,%ebx
  movl	$ayy,%ecx
  movl	$12,%edx
  int	$0x80

  ret
