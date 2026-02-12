AS = as
LD = ld
GDB = gdb

SRC = program.s
OBJ = program.o
EXEC = program

# Define assembly flags, including debug options
# --gstabs includes stabs debugging symbols, compatible with GDB
ASFLAGS = --gstabs

.PHONY: all clean debug

all: $(EXEC)

$(EXEC): $(OBJ)
	$(LD) $(OBJ) -o $(EXEC)

$(OBJ): $(SRC)
	$(AS) $(ASFLAGS) $< -o $@

clean:
	rm -f $(OBJ) $(EXEC)

debug: all
	$(GDB) $(EXEC)
