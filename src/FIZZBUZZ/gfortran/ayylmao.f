PROGRAM ayylmao
    implicit none
    integer ::i
    character(len=7) :: str

! Loop through integers 1 through 100
! Multiples of 3 print Ayy
! Multiples of 5 print Lmao
! Multiples of both print AyyLmao
! 15 is the lowest common multiple of 3, and 5
!    and thus is a shortcut to AyyLmao
    do i=1,100
        if (modulo(i, 15) == 0) then
            print *, 'AyyLmao'
        else if (modulo(i, 3) == 0) then
            print *, 'Ayy'
        else if (modulo(i, 5) == 0) then
            print *, 'Lmao'
        else
            write (str, '(i7)') i
            str = adjustl(str)
            print *, str
        end if
    end do
END PROGRAM ayylmao
