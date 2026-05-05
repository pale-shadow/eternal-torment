# Use the flags previously defined for debug-enabled assembly
AM_ASFLAGS = --gstabs

# Define the standalone assembly binaries to build
bin_PROGRAMS = hello funk_test main_asm

# Source mappings for each binary
hello_SOURCES = hello.s
funk_test_SOURCES = ../funk.s
main_asm_SOURCES = main.s fileio.s gpiomem.s mainmem.s shift.s

# Clean up any leftover manual build artifacts
CLEANFILES = $(OBJ) $(EXEC) prompt.txt